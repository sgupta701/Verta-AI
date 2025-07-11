# translator.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class Translator:
    def __init__(self):
        self.loaded_models = {}

    def load_model(self, model_name):
        if model_name not in self.loaded_models:
            try:
                tokenizer = AutoTokenizer.from_pretrained(model_name)
                model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
                self.loaded_models[model_name] = (tokenizer, model)
            except Exception as e:
                print("⚠️ Model loading failed:", e)
                raise e
        return self.loaded_models[model_name]

    def translate(self, text, model_name, src_lang=None, tgt_lang=None):
        if not text.strip():
            return ""

        tokenizer, model = self.load_model(model_name)

        # Helsinki-NLP models do not need src_lang / tgt_lang
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = model.generate(**inputs, max_length=512)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
