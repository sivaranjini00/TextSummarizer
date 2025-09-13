from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
import torch
from datasets import load_from_disk
import os
from src.textSummarizer.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(
            tokenizer=tokenizer,
            model=model_pegasus
        )

        # loading the data
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # training arguments
        training_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=1, warmup_steps=500,
            per_device_train_batch_size=1, per_device_eval_batch_size=1,
            weight_decay=0.01, logging_steps=10,
            eval_strategy='steps', eval_steps=500, save_steps=1e6,
            gradient_accumulation_steps=16
        )

        # trainer
        trainer = Trainer(
            model=model_pegasus,
            args=training_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["test"],
            eval_dataset=dataset_samsum_pt["validation"]
        )

        trainer.train()
        # save the model and tokenizer
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.json(self.config.root_dir,"tokenizer"))


