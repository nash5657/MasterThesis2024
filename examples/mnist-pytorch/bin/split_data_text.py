import os
from math import floor
import torch
import fire
# Assuming `load_dataset` and `tokenizer` are defined or imported earlier in your code
from datasets import load_dataset
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig, TrainingArguments, Trainer, AutoModelForCausalLM


model_name = "bigscience/bloomz-560m"
tokenizer = AutoTokenizer.from_pretrained(model_name)

def splitset(dataset, parts):
    n = len(dataset)  # Assuming dataset is a list or has len()
    local_n = floor(n / parts)
    result = []
    for i in range(parts):
        result.append(dataset[i * local_n: (i + 1) * local_n])
    return result

def split(out_dir='data_text', n_splits=2):
    # Load the dataset
    dataset = "fka/awesome-chatgpt-prompts"
    # Create the Dataset to create prompts.
    data = load_dataset(dataset)
    data = data.map(lambda samples: tokenizer(samples["prompt"]), batched=True)
    train_sample = data["train"].select(range(50))
    # Assuming you want to remove a column named 'act', adjust accordingly if your dataset doesn't have this column
    train_sample = train_sample.remove_columns('act')

    # Split the dataset
    data_splits = splitset(train_sample, n_splits)

    # Make dir
    if not os.path.exists(f'{out_dir}/clients'):
        os.makedirs(f'{out_dir}/clients')

    # Make splits and save them
    for i in range(n_splits):
        subdir = f'{out_dir}/clients/{str(i+1)}'
        if not os.path.exists(subdir):
            os.makedirs(subdir)
        # Assuming the data_splits are in a format that can be directly saved with torch.save
        torch.save(data_splits[i], f'{subdir}/dataset.pt')

if __name__ == '__main__':
    fire.Fire(split)
