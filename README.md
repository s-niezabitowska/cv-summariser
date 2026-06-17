# Automated CV Parser & Ingestion Engine

A lightweight, modular Python component designed to programmatically isolate, clean, and extract highly structured analytical parameters from unstructured resume formats using deep semantic analysis. 

## 🎯 Business Context & Problem Space
Manual resume screening during high-volume recruitment drives creates severe process bottlenecks for talent acquisition teams. This proof-of-concept showcases how raw, unstructured text files can be programmatically audited and normalised using low-latency LLM completions pipelines to feed structured data models into downstream applicant tracking systems (ATS).

## 🛠️ Architecture & Features

* **Defensive Error Gateways:** Implements structured runtime diagnostics and specific API error interception (`RateLimitError`, `APIConnectionError`) to maintain pipeline uptime.
* **Deterministic Completions Output:** Pinpoints data extraction parameters utilising a constrained temperature threshold (`0.2`) to suppress creative generation errors and maximise parsing consistency.
* **Environment Separation:** Complete integration with secure `.env` architectures to keep API credentials securely segregated from version control logs.
* **Production Logging Framework:** Fully decoupled from generic system `print` commands in favor of standard runtime system stream logs.

## 🚀 Installation & Testing Setup

1. Clone this repository:
```bash
git clone https://github.com/s-niezabitowska/cv-summariser.git
cd cv-summariser
```

2. Establish dependencies:

```bash
pip install -r requirements.txt
```

3. Setup your environment variable:

Create a .env file in the root directory and append your secure client key:

```bash
echo "OPENAI_API_KEY=your_key_here" > .env
```

4. Execute script:

```bash
python main.py
```
