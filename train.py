training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    save_strategy="epoch",

    learning_rate=2e-5,

    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,

    num_train_epochs=2,

    weight_decay=0.01,

    logging_dir="./logs",

    load_best_model_at_end=True,

    fp16=False
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics
)