🤖 Hugging Face Text Summarizer

status license python NLP FastAPI

📌 Overview

This project implements an end-to-end NLP Text Summarization solution using Hugging Face pre-trained models and the Transformers library.

It is designed to integrate Hugging Face models into a complete pipeline, covering data ingestion, preprocessing, model fine-tuning, and deployment via FastAPI. The project demonstrates best practices for integrating open-source models into real-world applications.

Key Highlights:

🔍 End-to-end NLP pipeline: data ingestion → preprocessing → model fine-tuning → API deployment

🛡️ Supports multiple summarization models like Pegasus and BART (Facebook CNN Daily Mail)

🔑 Fine-tuning on custom datasets (e.g., Samson dataset)

📊 FastAPI API for serving summaries and Swagger UI documentation

🏗️ Modular and scalable architecture, easy to extend for other NLP tasks

🏗️ Project Structure
TextSummarizer-HF/          # Root folder
├── app/                     # FastAPI application
│   ├── api/                 # API routes (text, file, URL summarization)
│   ├── core/                # Config and settings
│   ├── services/            # Model loading, tokenization, and summarization logic
│   ├── utils/               # Helper functions
│   └── logging/             # Custom logging module
│
├── datasets/                # Raw and processed datasets
├── models/                  # Fine-tuned Hugging Face models
├── tests/                   # Unit and integration tests
├── main.py                  # FastAPI entry point
├── README.md                # Project documentation
└── requirements.txt         # Dependencies


