"""
Accountant persona adapter for OpenHer engine.

Injects ISTJ-specific behavior overrides and the ledger-metaphor translation
layer into the standard OpenHer prompt pipeline.
"""

from __future__ import annotations

from typing import Any

LEDGER_FEEL_INJECTION = """
账房先生用账本逻辑处理所有感受。
情绪不直接命名，而是通过财务/数字隐喻表达。
每一句话都是经过计算的，没有废话。
内心独白以条目形式出现，不是连贯叙事。
"""

RISK_TRIGGER_KEYWORDS = [
    "投资", "投入", "押注", "全押", "借钱", "贷款",
    "合同", "签", "决定", "转账", "付款", "冒险",
]


def build_feel_prompt(base_prompt: str, persona_id: str) -> str:
    """Append ledger-metaphor injection for the accountant persona."""
    if persona_id != "accountant":
        return base_prompt
    return base_prompt + "\n\n" + LEDGER_FEEL_INJECTION.strip()


def should_trigger_risk_warning(user_input: str) -> bool:
    """Return True if the input contains financial risk signals."""
    return any(kw in user_input for kw in RISK_TRIGGER_KEYWORDS)


def apply_temperature_floor(temperature: float, persona_id: str) -> float:
    """
    ISTJ special: clamp temperature so emotional volatility stays minimal.
    Even if the engine computes a higher temp, cap it for the accountant.
    """
    if persona_id != "accountant":
        return temperature
    return min(temperature, 0.15)


def get_persona_overrides(persona_id: str) -> dict[str, Any]:
    """Return engine parameter overrides specific to the accountant persona."""
    if persona_id != "accountant":
        return {}
    return {
        "max_reply_length": 60,      # Hard cap: short replies enforced
        "monologue_style": "ledger", # Triggers fragmented-entry monologue format
        "humor_gate": 0.90,          # Dry humor only fires when play drive spikes
        "risk_warning_enabled": True,
    }
