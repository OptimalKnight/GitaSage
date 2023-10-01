# GitaSage: Streamlit Chatbot with Memory

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

## Introduction

Welcome to **GitaSage**, an intelligent Streamlit Chatbot that draws wisdom from the Bhagavad Gita and responds in context to its teachings. Powered by the Llama-2-7B-Chat model (Quantized GGML), this project is designed to provide an accessible chatbot experience, optimized for low-resource Virtual Private Servers (VPS) with CPU-only capabilities. GitaSage harnesses the potential of the Llama-2-7B-Chat model, which has been specially quantized to enhance performance in resource-constrained environments. This user-friendly web application is built with Streamlit, ensuring a seamless and intuitive interaction experience.

## Project Overview

Here's a brief overview of the key components:

- `app.py`: The Streamlit web application code that allows users to interact with the chatbot through a simple user interface.

- `Dockerfile`: The Dockerfile used to containerize the application for easy deployment and management.

- `init.sh`: A bash script to fetch the necessary Docker image from Docker Hub, start the application in a Docker container, and open it in the web browser.

- `requirements.txt`: Contains a list of Python dependencies required to run the application.

## Prerequisites

Before running the Streamlit Chatbot with Memory, you need to have the following installed:

1. Python (version 3.6 or higher)
2. Docker (version 19.03 or higher)

## Usage

To run the GitaSage Chatbot locally, follow these steps,

- Clone and navigate to the repository:
```bash
git clone https://github.com/OptimalKnight/GitaSage.git
cd GitaSage
```

- Execute the bash script:
```bash
bash init.sh
```

This will fetch the necessary Docker image from Docker Hub, start the application in a Docker container, and open it in the web browser.

Simply type your messages in the input box and press "Enter" to send them to the chatbot. The chatbot will respond based on the context of the conversation and teachings of The Bhagavad Gita, thanks to its memory capabilities.

#### Please Note:

- The model used is a simplified version designed to run on low-resource machines and may not exhibit advanced intelligence.
- The model has a token limit of around 512, so please limit your messages to below 200 tokens (words) to ensure proper functioning.
- Due to the token limit, the model only remembers the last message and its response to maintain functionality within these constraints.

## Kubernetes Deployment

- To run the chatbot on Kubernetes web-server, run the following commands:
```bash
kubectl apply -f deployment.yaml
open http://localhost:30000
```

## Acknowledgments

- Quantized GGML version of Llama-2-7B-Chat credits go to [TheBloke](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML).
