# 第 5 章：后端核心模块实战

> 用 AI 快速搭建“能跑、能扩、能审计”的后端：认证授权、支付回调、安全基线与可观测性一次到位。[20][22][23]

!!! note "关于复现、目录与 CI"
    本章中出现的 `make ...`、`CI`、以及示例目录/文件路径（例如 `path/to/file`）均为落地约定，用于说明如何把方法落实到你自己的工程仓库中。本仓库仅提供文档，读者需自行实现或用等价工具链替代。

## 章节定位
本章回答“如何让产品可上线并守住底线”。重点涵盖用户体系、支付闭环、API 设计与日志监控，给出可移植的模块拆分、接口契约与安全基线建议（示例代码用于说明实现要点）。[20][22]

## 你将收获什么
- JWT/OAuth2 用户模块的参考实现要点，包含 RBAC 与审计日志设计。[22]
- Stripe/微信/支付宝的支付回调处理要点，覆盖签名校验、幂等与重放保护。[23]
- 观测性基线：结构化日志、分布式追踪、速率限制与 WAF 接入。

## 方法论速览
1. **身份与权限：** 统一身份源 + 细粒度 RBAC，接口默认最小权限；生成 OpenAPI 方便前后端并行。[22]
2. **支付安全：** 端到端签名验证 + 幂等键，失败重试与对账脚本，确保账实一致。[23]
3. **可观测性：** 结构化日志 + traces + metrics，默认开启速率限制与输入校验。

## 实战路径
### 1. 用户模块
```python
# FastAPI 登录示例
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from auth import issue_token, verify_user

app = FastAPI()

@app.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = verify_user(form.username, form.password)
    return issue_token(user)
```
- 使用 Pydantic 校验请求体，避免宽松解析导致注入。
- RBAC：角色—权限映射存入数据库，接口通过依赖注入校验权限。

### 2. 支付与对账
- Stripe/微信/支付宝：校验签名、记录幂等键（订单号+版本），回调幂等处理。
- 对账脚本每日运行，对比网关记录与内部账本差异；异常自动报警。

### 3. API 设计与限流
- OpenAPI 自动生成 SDK；接口应声明速率限制（如 IP/User/Token 多级）。
- 输入输出均使用 JSON Schema 校验，避免隐式类型转换。

### 4. 审计与可观测
- 日志统一使用 JSON（包含 trace_id/user_id）；错误事件写入审计表便于排查。
- 集成 Prometheus/Grafana：QPS、错误率、P95 延迟、支付成功率与退款率。

## 复现检查（落地建议）
- `make backend-dev`：启动本地栈（API + DB + Redis），跑通过 Auth/支付集成测试。
- `make backend-security`：运行 `bandit`/`semgrep`、JWT 过期测试、支付重放攻击模拟。
- `make backend-observe`：发压基准并生成延迟、错误率、追踪图。

## 常见陷阱
- **回调幂等缺失：** 重放导致重复扣费；必须使用幂等键与幂等锁。
- **权限过宽：** 默认开放所有角色，需最小权限策略并记录谁、何时、改了什么。
- **日志敏感信息：** 避免输出 token、密码、银行卡号；必要时脱敏与访问控制。

## 延伸练习
- 将用户模块改为外部 IdP（如 Auth0/Keycloak），比较延迟与安全性取舍。
- 为支付对账脚本添加“增量重试”与“异常票据”机制，模拟真实财务流程。

## 交付物与验收（落地建议）
- `services/api` 源码与 Docker Compose；集成测试、对账脚本、基准报告齐全。
- 安全扫描与审计日志样例；支付幂等与签名校验必须在 CI 有自动化测试。
- OpenAPI 文档与限流/配额策略说明。

## 参考
详见本书统一参考文献列表：[`references.md`](references.md)。
