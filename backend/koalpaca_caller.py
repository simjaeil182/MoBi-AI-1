from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def call_koalpaca(prompt, max_tokens=150, temperature=0.7, top_p=0.9):
    try:
        model_id = "beomi/KoAlpaca-Polyglot-5.8B"
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.float16,
            device_map="auto"
        )
        inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
        outputs = model.generate(
            inputs.input_ids,
            max_new_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
        return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    except Exception as e:
        return f"[KoAlpaca Error] {e}"
