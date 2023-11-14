# -*- coding: utf-8 -*-
"""NLP_Laba_5_Zemlyanova.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17xde8g0lsFeclE4evZVR67mvarhHFGz9
"""

pip install transformers

from sys import argv
import numpy as np
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

np.random.seed(42)
torch.manual_seed(42)

def generate(
    model, tok, text,
    do_sample=True, max_length=100, repetition_penalty=5.0,
    top_k=5, top_p=0.95, temperature=1,
    num_beams=None,
    no_repeat_ngram_size=3
):
    input_ids = tok.encode(text, return_tensors="pt")
    out = model.generate(
        input_ids,
        max_length=max_length,
        repetition_penalty=repetition_penalty,
        do_sample=do_sample,
        top_k=top_k, top_p=top_p, temperature=temperature,
        num_beams=num_beams, no_repeat_ngram_size=no_repeat_ngram_size
    )
    return list(map(tok.decode, out))

# Загрузка
def load_tokenizer_and_model(model_name_or_path):
    return GPT2Tokenizer.from_pretrained(model_name_or_path), GPT2LMHeadModel.from_pretrained(model_name_or_path)

""" Cлова для работы "значит" и "помощь"."""

# Запуск
tok, model = load_tokenizer_and_model("sberbank-ai/rugpt3large_based_on_gpt2")
generated = generate(model, tok, "Многие семьи не могут позволить себе дорогостоящее лечение. Существуют различные фонды. Если это не ваш ребенок, это не", num_beams=10)
print(generated[0])