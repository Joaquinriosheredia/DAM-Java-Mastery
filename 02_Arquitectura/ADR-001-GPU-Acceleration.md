# ADR-001: GPU Acceleration for Local LLM Inference Pipeline

**Status:** Accepted  
**Date:** 2026-01-15  
**Author:** Joaquín Ríos Heredia  
**Context:** Authority Engine v21.0 — Local AI Pipeline + AWS Cloud

---

## Context

Authority Engine v21.0 requires generating Staff Engineer-level technical documentation at production speed. The pipeline processes requests through a local LLM (Ollama + Qwen 7b) before deploying outputs to AWS Lambda + S3.

During initial benchmarking, inference speed was measured at **7.48 tokens/second** — completely unviable for a production pipeline targeting automated, unattended document generation at scale.

**System specs:**
- CPU: AMD Ryzen (multi-core)
- GPU: NVIDIA RTX 4060 (8GB VRAM)
- RAM: 32GB
- OS: Ubuntu 24.04
- Runtime: Ollama 0.x + Qwen 7b (4-bit quantized)

---

## Problem

The pipeline was running entirely on CPU despite the RTX 4060 being available. Root cause analysis identified two issues:

1. **Ollama was not detecting the GPU** — missing CUDA environment configuration
2. **Blocking I/O calls** in the Python pipeline were creating artificial bottlenecks between inference steps, preventing async utilisation of available hardware

Symptoms:
- `nvidia-smi` showed 0% GPU utilisation during inference
- CPU at 100% across all cores
- Inference speed: 7.48 tok/s
- Pipeline throughput: ~1 document per 8-10 minutes

---

## Decision

**Force GPU acceleration via explicit CUDA configuration in Ollama + eliminate blocking calls in the Python pipeline.**

### Changes made:

**1. GPU activation:**
```bash
# Verified CUDA availability
nvidia-smi
nvcc --version

# Set explicit GPU layer offloading in Ollama
ollama run qwen:7b --gpu-layers 35
```

**2. Pipeline refactor — blocking → async:**
```python
# BEFORE: blocking sequential calls
response = ollama.generate(model=MODEL, prompt=prompt)
result = process_response(response)

# AFTER: non-blocking with explicit GPU context
async def generate_with_gpu(prompt: str) -> str:
    response = await asyncio.to_thread(
        ollama.generate,
        model=MODEL,
        prompt=prompt,
        options={"num_gpu": 35, "num_thread": 8}
    )
    return response['response']
```

**3. Measurement protocol:**
```python
import time

start = time.perf_counter()
response = ollama.generate(model=MODEL, prompt=benchmark_prompt)
elapsed = time.perf_counter() - start

tokens = len(response['response'].split())
tok_per_sec = tokens / elapsed
print(f"Inference speed: {tok_per_sec:.2f} tok/s")
```

---

## Results

| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Inference speed | 7.48 tok/s | 48.55 tok/s | **+549% (6x)** |
| GPU utilisation | 0% | 87-94% | +87-94pp |
| CPU utilisation | 100% | 22-35% | -65-78pp |
| Doc generation time | ~8-10 min | ~1.5-2 min | **-75%** |
| Pipeline viability | ❌ Not viable | ✅ Production | — |

---

## Alternatives Considered

| Option | Reason Rejected |
|--------|----------------|
| Upgrade to larger GPU | Unnecessary cost — RTX 4060 had sufficient VRAM for Qwen 7b 4-bit |
| Switch to cloud inference (OpenAI API) | Increased cost, latency, and external dependency — local inference preferred for control and cost |
| Switch to smaller model (Qwen 3b) | Quality degradation unacceptable — Staff Engineer documentation requires 7b minimum |
| CPU optimisation (threading) | Tested — diminishing returns above 8 threads, max 12 tok/s achievable |

---

## Consequences

**Positive:**
- Pipeline viable for production unattended operation
- 47 Staff Engineer documents generated and deployed to AWS S3 with average quality score 99/100
- Full automation: local generation → S3 → GitHub with single command
- CPU freed for orchestration tasks while GPU handles inference

**Negative / Trade-offs:**
- Pipeline now requires NVIDIA GPU with CUDA support — not portable to CPU-only environments
- Mitigation: AWS Lambda fallback handles lightweight post-processing; heavy inference remains local

---

## Observability

Post-optimisation the pipeline exposes the following metrics for monitoring:

```python
# Metrics tracked per document generation
metrics = {
    "inference_speed_tok_per_sec": float,
    "gpu_utilisation_pct": float,
    "quality_score": int,          # 0-100 via integrated auditor
    "generation_time_seconds": float,
    "model": str,
    "document_category": str
}
```

Alerting thresholds:
- `inference_speed < 30 tok/s` → GPU not properly utilised, investigate CUDA config
- `quality_score < 85` → Document fails auditor, not published to S3/GitHub

---

## References

- [Ollama GPU documentation](https://github.com/ollama/ollama/blob/main/docs/gpu.md)
- [NVIDIA CUDA Installation Guide](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/)
- Authority Engine v21.0 source: `08_IA_Agentes/Authority_Engine/`
- AWS Lambda deployment config: `05_SRE_DevOps/AWS/`
