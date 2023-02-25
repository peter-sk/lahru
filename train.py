#!/usr/bin/env python3
from sys import argv
from datasets import load_dataset, DatasetDict
from transformers import GPT2Tokenizer,GPT2LMHeadModel, DataCollatorForLanguageModeling, TrainingArguments, Trainer
model_name = 'gpt2-da'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
collator = DataCollatorForLanguageModeling(tokenizer=tokenizer,mlm=False)
raw_dataset = load_dataset(f"data/{argv[1]}",data_files=f"{argv[1]}.jsonl.bz2").rename_column('text','input_ids')
#reduced_dataset = raw_dataset['train'].train_test_split(0.99,shuffle=False,seed=42)
train_testvalid = raw_dataset['train'].train_test_split(0.1,shuffle=False,seed=42)
test_valid = train_testvalid['test'].train_test_split(0.5,shuffle=False,seed=42)
dataset = DatasetDict({
    'train': train_testvalid['train'],
    'test': test_valid['train'],
    'valid': test_valid['test']
})
print(dataset)
num_embeddings = model.transformer.wte.num_embeddings
#tokenized_dataset = dataset.map(lambda row: tokenizer(row['input_ids'])).filter(lambda row: len(row) < 512 and all((x < num_embeddings for x in row['input_ids'])))
tokenized_dataset = dataset.map(lambda row: tokenizer(row['input_ids'])).filter(lambda row: len(row['input_ids']) < 1024 and all((x < num_embeddings for x in row['input_ids'])))
print(tokenized_dataset)
training_args = TrainingArguments(
    output_dir=model_name,
    overwrite_output_dir=True,
    per_device_train_batch_size=8,
    eval_steps=10000,
    save_steps=10000,
    logging_steps=10000,
    num_train_epochs=1,
    auto_find_batch_size=False,
    gradient_accumulation_steps=1,
    no_cuda=False,
    fp16=True
)
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=collator,
    train_dataset=tokenized_dataset['train'],
    eval_dataset=tokenized_dataset['test']
)
trainer.train()
trainer.save_model()
