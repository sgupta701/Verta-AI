# translator.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class Translator:
    def __init__(self):
        self.loaded_models = {}

    def load_model(self, model_name):
        if model_name not in self.loaded_models:
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
            self.loaded_models[model_name] = (tokenizer, model)
        return self.loaded_models[model_name]

    def translate(self, text, model_name, src_lang=None, tgt_lang=None):
        if not text.strip():
            return ""

        tokenizer, model = self.load_model(model_name)

        if "mbart" in model_name:
            tokenizer.src_lang = src_lang
            inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
            generated_tokens = model.generate(
                **inputs,
                forced_bos_token_id=tokenizer.convert_tokens_to_ids(tgt_lang),
                max_length=512
            )
            return tokenizer.decode(generated_tokens[0], skip_special_tokens=True)

        else:
            inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
            with torch.no_grad():
                outputs = model.generate(**inputs, max_length=512)
            return tokenizer.decode(outputs[0], skip_special_tokens=True)
