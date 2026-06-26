"""
Vertical-slice validation tests for the Accountant persona.

These are scenario-level checks — they verify that the adapter layer
produces the right prompt shapes and parameter values, not that the LLM
outputs any specific string.
"""

import pytest
from engine.adapter import (
    apply_temperature_floor,
    build_feel_prompt,
    get_persona_overrides,
    should_trigger_risk_warning,
)


def test_feel_prompt_injection_accountant():
    base = "You are the accountant."
    result = build_feel_prompt(base, "accountant")
    assert "账本逻辑" in result
    assert "条目形式" in result


def test_feel_prompt_passthrough_other_persona():
    base = "You are Iris."
    result = build_feel_prompt(base, "iris")
    assert result == base


def test_risk_warning_triggered_on_financial_keywords():
    assert should_trigger_risk_warning("我把所有钱都投入了") is True
    assert should_trigger_risk_warning("我要签合同") is True
    assert should_trigger_risk_warning("你好啊") is False


def test_temperature_floor_accountant():
    assert apply_temperature_floor(0.8, "accountant") == pytest.approx(0.15)
    assert apply_temperature_floor(0.05, "accountant") == pytest.approx(0.05)


def test_temperature_passthrough_other_persona():
    assert apply_temperature_floor(0.8, "iris") == pytest.approx(0.8)


def test_persona_overrides_accountant():
    overrides = get_persona_overrides("accountant")
    assert overrides["max_reply_length"] == 60
    assert overrides["monologue_style"] == "ledger"
    assert overrides["risk_warning_enabled"] is True


def test_persona_overrides_other_persona():
    overrides = get_persona_overrides("iris")
    assert overrides == {}
