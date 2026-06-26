# 账房先生 · The Accountant

> OpenHer 首位男性角色 · ISTJ · 竖切 Demo

---

**账房先生**是 [OpenHer](https://github.com/xiaobinn-snowydog/OpenHer) 项目的首位男性人格角色，也是引擎对 ISTJ 类型和功能型人格的完整竖切验证。

他不是来哄你的。他是来帮你看清楚的。

---

## 角色概览

| 属性 | 值 |
|------|----|
| 姓名 | 账房先生 / The Accountant |
| 年龄 | 38岁 |
| MBTI | ISTJ |
| 语言 | 中文 |
| 定位 | 私人财务顾问 · 精算人格 |
| 核心驱力 | safety (0.85) — 风险管控是本能 |

他用账本逻辑处理一切，包括情感。当他说「这笔账，不对」，那是他表达担心的方式。当他说「这个……勉强算得过去」，那是他给出的最高认可。

---

## 仓库结构

```
the-accountant/
├── persona/
│   ├── personas/accountant/
│   │   ├── SOUL.md          # 人格定义：身份、驱力基线、引擎参数、语言风格
│   │   └── SHELL.md         # 外形定义：视觉描述、服装、姿态、控图 prompt
│   └── genesis/
│       └── genesis_accountant.json  # 15条对话种子
├── engine/
│   └── adapter.py           # ISTJ特化适配器：账本隐喻注入、温度上限、参数覆盖
├── tests/
│   └── test_accountant.py   # 场景验证测试
├── docs/
│   └── design.md            # 完整设计文档
└── README.md
```

---

## 竖切范围

本 Demo 覆盖完整实现层次：

- **人格定义层**：SOUL.md（驱力、引擎参数）+ SHELL.md（外形 prompt）
- **种子层**：15 条覆盖核心场景的对话种子（日常 / 财务决策 / 情感确认 / 压力场景）
- **引擎适配层**：ISTJ 特化参数注入、账本隐喻翻译层、财务风险触发机制
- **验证层**：适配器单元测试

不包含：图像生成、语音合成、完整 UI（复用 OpenHer 现有界面）。

---

## 快速开始

```bash
# 安装依赖（复用 OpenHer 主项目依赖）
pip install -r ../OpenHer/requirements.txt

# 运行验证测试
cd the-accountant
pytest tests/ -v
```

---

## 设计文档

详见 [`docs/design.md`](docs/design.md)，涵盖：
- 立项背景与选型依据
- 人格设计（MBTI 选型、驱力基线、引擎参数）
- 对话设计（语言规范、情绪翻译机制、关系演变曲线）
- 种子设计说明
- 引擎适配说明（男性角色适配、ISTJ 特化行为）
- 风险与注意事项
- 后续规划

---

## 关联项目

- [OpenHer](https://github.com/xiaobinn-snowydog/OpenHer) — 主引擎与完整角色库
