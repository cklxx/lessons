# 第 11 章：推理加速与生产级部署

> 让模型“跑得快、成本低、可水平扩展”：vLLM/TensorRT-LLM、量化（AWQ/GPTQ）与 TGI 部署实战。[45][46][48][49]

!!! note "关于复现、目录与 CI"
    本章中出现的 `make ...`、`CI`、以及示例目录/文件路径（例如 `path/to/file`）均为落地约定，用于说明如何把方法落实到你自己的工程仓库中。本仓库仅提供文档，读者需自行实现或用等价工具链替代。

## 章节定位
本章解决“上线后又慢又贵”的问题。你将对比不同推理引擎与量化方案，完成容器化部署，并通过压测与观测确保 SLA。[45][48]

## 你将收获什么
- vLLM 与 TensorRT-LLM 部署脚本，包含批处理、KV cache 与并发配置。[45][46]
- 量化流水线（AWQ/GPTQ/QLoRA 推理），在消费级 GPU 上达成可用吞吐。[48]
- TGI/KServe 部署模板，接入网关、鉴权、限流与观测。

## 方法论速览
1. **推理引擎选择：** 依据模型大小、硬件与延迟目标选择 vLLM（高吞吐）或 TensorRT-LLM（低延迟）。[45][46]
2. **量化策略：** 评估 AWQ/GPTQ 对精度与延迟的影响，配合 INT4/INT8 部署。[48]
3. **部署与观测：** 容器化 + API 网关 + metrics/logging/tracing，确保可水平扩展。[49]

## 实战路径
### 1. 量化与导出
```bash
python3 -m awq.entry --model_path llama-7b --w_bit 4 --q_group_size 128 \
  --run_awq --dump_quant
```
- 记录量化前后 perplexity/ROUGE 变化；若下降超阈值则调整 bitwidth。

### 2. 引擎对比
- vLLM：配置 `--tensor-parallel-size`、`--max-num-batched-tokens`，适合高吞吐。[45]
- TensorRT-LLM：编译 engine，适合低延迟场景；注意 warmup 与 engine 版本。[46]

### 3. 容器化部署
- 使用 TGI/fastapi 作为入口，加入 JWT/AK/SK 鉴权与速率限制。
- 通过 Prometheus + Grafana 观测 QPS、P95、OOM、队列长度。

### 4. 压测
- 使用 `wrk`/`hey`/`locust` 发压，记录吞吐与延迟；发现抖动时调整批处理/并发。
- 对比不同量化与 engine 组合，选出性价比最高的配置。

## 复现检查（落地建议）
- `make infer-quant`：执行 AWQ/GPTQ 量化并输出精度对比表。
- `make infer-serve`：启动 vLLM/TensorRT-LLM + 网关，运行健康检查。
- `make infer-bench`：压测并产出延迟/吞吐/成本图表。

## 常见陷阱
- **KV cache 爆内存：** 长上下文时需限制最大序列或启用分页注意力。
- **量化失真：** 低 bitwidth 导致幻觉增多，需结合评测阈值控制。
- **健康检查不足：** 未监控 GPU/CPU/队列长度，问题难以定位。

## 延伸练习
- 对同一模型分别使用 vLLM 与 TensorRT-LLM，比较延迟—吞吐曲线与成本。
- 尝试在边缘设备上部署 INT4 量化模型，测算能耗与响应时间。

## 交付物与验收（落地建议）
- 量化脚本与评估报告；推理引擎配置文件与容器镜像。
- 压测报告与 SLA 目标对比；告警与自动扩缩容策略。
- 安全与鉴权配置（网关/令牌/速率限制）。

## 参考
详见本书统一参考文献列表：[`references.md`](references.md)。
