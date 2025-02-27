#!/usr/bin/env python3
from sys import argv
from datasets import concatenate_datasets, load_dataset, DatasetDict
from transformers import GPT2TokenizerFast,GPT2LMHeadModel, DataCollatorForLanguageModeling, TrainingArguments, Trainer
args = argv[1:]
model_name = 'gpt2-da'
if args[0] == "--model":
    model_name = args[1]
    args = args[2:]
epochs = 1
if args[0] == "--epochs":
    epochs = int(args[1])
    args = args[2:]
steps = 1
if args[0] == "--steps":
    steps = int(args[1])
    args = args[2:]
resume = False
if args[0] == "--resume":
    resume = True
    args = args[1:]
tokenizer = GPT2TokenizerFast.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
collator = DataCollatorForLanguageModeling(tokenizer=tokenizer,mlm=False)
datasets = []
for arg in args:
    raw_dataset = load_dataset(f"data",data_files=f"{arg}.jsonl.bz2").rename_column('text','input_ids')
    train_test = raw_dataset['train'].train_test_split(100000,shuffle=False,seed=42)
    dataset = DatasetDict({
        'train': train_test['train'],
        'test': train_test['test']
    })
    print(arg,dataset)
    datasets.append(dataset)
dataset = DatasetDict({
    'train': concatenate_datasets([dataset['train'] for dataset in datasets]),
    'test': concatenate_datasets([dataset['test'] for dataset in datasets])
})
del datasets
print('MERGED',dataset)
num_embeddings = model.transformer.wte.num_embeddings
tokenized_dataset = dataset.map(lambda row: tokenizer(row['input_ids'])).filter(lambda row: len(row['input_ids']) < 1024 and all((x < num_embeddings for x in row['input_ids'])))
print(tokenized_dataset)
training_args = TrainingArguments(
    output_dir=model_name,
    overwrite_output_dir=True,
    per_device_train_batch_size=1,
    eval_steps=int(10000/steps),
    save_steps=int(10000/steps),
    logging_steps=int(10000/steps),
    num_train_epochs=epochs,
#    auto_find_batch_size=True,
    gradient_accumulation_steps=steps,
    no_cuda=False,
    fp16=True,
    save_total_limit = 50,
    save_strategy = "steps",
    evaluation_strategy = "steps",
    load_best_model_at_end=False
)
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=collator,
    train_dataset=tokenized_dataset['train'],
    eval_dataset=tokenized_dataset['test']
)
trainer.train(resume_from_checkpoint=resume)
trainer.save_model()
