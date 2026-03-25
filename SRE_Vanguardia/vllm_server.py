```python
import argparse
from typing import Dict, List
import torch
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class RequestBody(BaseModel):
    input_text: str = "Hello, how are you?"
    max_new_tokens: int = 50
    top_k: int = 50
    temperature: float = 1.0
    top_p: float = 0.95

app = FastAPI()

# Load model and tokenizer
model_name = 'EleutherAI/pythia-160m'
tokenizer = AutoTokenizer.from_pretrained(model_name)
config = AutoConfig.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_config(config)

# Optimizations: Move to GPU if available.
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

@app.post("/generate/")
async def generate_text(request_body: RequestBody):
    # Tokenize the input text
    inputs = tokenizer.encode(request_body.input_text, return_tensors="pt").to(device)
    
    try:
        outputs = model.generate(
            inputs,
            max_length=request_body.max_new_tokens + len(inputs[0]),
            top_k=request_body.top_k,
            temperature=request_body.temperature,
            do_sample=True,
            top_p=request_body.top_p
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    # Decode the output tokens to text
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"generated_text": response_text}

if __name__ == "__main__":
    import uvicorn
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    uvicorn.run(app, host=args.host, port=args.port)

```