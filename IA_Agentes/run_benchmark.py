import argparse
from timeit import default_timer as timer
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import pandas as pd
import os

# Define benchmark functions for each model
def benchmark_grok_4():
    # Load Grok-4 Model and Tokenizer
    tokenizer = AutoTokenizer.from_pretrained("path_to_grok4_tokenizer")
    model = AutoModelForCausalLM.from_pretrained("path_to_grok4_model")

    start_time = timer()
    
    input_text = "Hello, how are you?"
    inputs = tokenizer(input_text, return_tensors='pt')
    output = model.generate(**inputs)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    elapsed_time = timer() - start_time
    print(f"Grok-4 Generated: {generated_text}")
    return elapsed_time

def benchmark_claude_4():
    # Load Claude 4 Model and Tokenizer
    tokenizer = AutoTokenizer.from_pretrained("path_to_claude4_tokenizer")
    model = AutoModelForCausalLM.from_pretrained("path_to_claude4_model")

    start_time = timer()
    
    input_text = "Hello, how are you?"
    inputs = tokenizer(input_text, return_tensors='pt')
    output = model.generate(**inputs)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    elapsed_time = timer() - start_time
    print(f"Claude-4 Generated: {generated_text}")
    return elapsed_time

def benchmark_qwen2_5():
    # Load Qwen 2.5 Model and Tokenizer
    tokenizer = AutoTokenizer.from_pretrained("path_to_qwen25_tokenizer")
    model = AutoModelForCausalLM.from_pretrained("path_to_qwen25_model")

    start_time = timer()
    
    input_text = "Hello, how are you?"
    inputs = tokenizer(input_text, return_tensors='pt')
    output = model.generate(**inputs)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    elapsed_time = timer() - start_time
    print(f"Qwen-2.5 Generated: {generated_text}")
    return elapsed_time

def main():
    parser = argparse.ArgumentParser(description='Run benchmarking for Grok-4, Claude 4, and Qwen2.5')
    parser.add_argument('--model', type=str, help="Model to run the benchmark on (grok-4, claude-4, qwen2.5)")
    
    args = parser.parse_args()
    
    if args.model == "grok-4":
        elapsed_time = benchmark_grok_4()
    elif args.model == "claude-4":
        elapsed_time = benchmark_claude_4()
    elif args.model == "qwen2.5":
        elapsed_time = benchmark_qwen2_5()

    # Log results
    result_data = {
        'model': [args.model],
        'elapsed_time': [elapsed_time]
    }
    
    df = pd.DataFrame(result_data)
    
    if os.path.exists('results.csv'):
        existing_results = pd.read_csv('results.csv')
        updated_results = pd.concat([existing_results, df])
        updated_results.to_csv('results.csv', index=False)
    else:
        df.to_csv('results.csv', index=False)

if __name__ == '__main__':
    main()