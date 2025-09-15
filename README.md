## 🤖 Hugging Face Text Summarizer

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![Domain](https://img.shields.io/badge/Domain-NLP-purple)
![Framework](https://img.shields.io/badge/Framework-FastAPI-orange)


## 📌 Overview

Hugging Face Text Summarizer is an end-to-end NLP Text Summarization solution built using Hugging Face pre-trained models and the Transformers library.

It integrates Hugging Face models into a complete pipeline covering data ingestion, preprocessing, model fine-tuning, and deployment via FastAPI.

This project demonstrates best practices for integrating open-source models into real-world applications.

## 🔑 Key Highlights

🔍 End-to-end NLP pipeline: data ingestion → preprocessing → model fine-tuning → API deployment

🛡️ Supports multiple summarization models: Pegasus, BART (Facebook CNN Daily Mail)

📈 Fine-tuning on custom datasets: e.g., Samson dataset

📊 FastAPI API for serving summaries with Swagger UI documentation

🏗️ Modular and scalable architecture, easy to extend for other NLP tasks

## 🏗️ Project Structure
```text
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
