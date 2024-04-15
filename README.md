# End-to-End Dialogue Summarizer

### Introduction
Dialogue Summarization is a very important aspect of Natural Language Processing (NLP) applications, particularly in use cases where we need fast response or vast amounts of text needs to condensed. 

This repository documents the development and deployment of a Dialogue Summarization model focused on fine-tuning a HuggingFace PEGASUS model on Samsum data and deployment using AWS.

### Key Aspects of the Project
* Fine-tuning the HuggingFace PEGASUS (Transformer) model on custom (Samsum) data.
* Modular coding practices for better code orgnization and maintainability.
* Integration with FastAPI for easy user interface.
* Deployment of the optimized model using AWS services such as EC2, and ECR.
* Continuous Integration and Continuous Deployment (CI/CD) workflows using GitHub Actions.

### Local Run of the Application

With the following steps, you can run the user interface on your local machine.

#### Creating Conda (VM) Environment

To create the virtual environment to run the code:
```
conda create -n dialogue python=3.8 -y
conda activate dialogue
```

#### Installation

Run the following line of code to install dependencies.
```
pip install -r requirements
```

#### Local Run

To run the application, enter the following command:
```
python app.py
```

Now, open your local host and port on your web browser to view the application.

### Project CI/CD Deployment using AWS and GitHub Actions


ECR repo URI: 654654169409.dkr.ecr.us-west-1.amazonaws.com/text-s
