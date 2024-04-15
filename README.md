# End-to-End Dialogue Summarizer

### Introduction
Dialogue Summarization is a very important aspect of Natural Language Processing (NLP) applications, particularly in use cases where we need fast response or vast amounts of text needs to condensed. 

This repository documents the development and deployment of a Dialogue Summarization model focused on fine-tuning a HuggingFace PEGASUS model on Samsum data and deployment using AWS.

### Key Aspects of the Project
* Fine-tuning the HuggingFace PEGASUS (Transformer) model on custom (Samsum) data.
* Modular coding practices for better code orgnization and maintainability.
* Integration with FastAPI for easy user interface.
* Deployment of the optimized model using Docker and AWS services such as EC2, and ECR
* Continuous Integration and Continuous Deployment (CI/CD) workflows using GitHub Actions.

### Local Run of the Application

With the following steps, you can run the user interface on your local machine.
Please clone the repo for run on your local machine.

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

#### Step 1: Login into your AWS Console

#### Step 2: Create an IAM user for deployment

AWS EC2 is a virtual machine, and AWS ECR (Elastic Container Registry) to save your Docker image in AWS.

Process involved-
* Build a Docker image of your source code
* Push the Docker image to the ECR
* Launch you EC2
* Pull your image from ECR to EC2
* Launch your Docker image in EC2

Policies used-
* AmazonEC2ContainerRegistryFullAccess
* AmazonEC2FullAccess

#### Step 3: Create ECR Repo to store/save Docker Image
Make sure to save your ECR repo URI.
<!-- ECR repo URI: 654654169409.dkr.ecr.us-west-1.amazonaws.com/text-s -->

#### Step 4: Create EC2 machine with Ubuntu configuration

#### Step 5: Open EC2 and Install Docker in EC2 Machine

Run each of the code lines for the installation:
```
sudo apt-get update -y
sudo apt-get upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

#### Step 6: Configure EC2 as a self-hosted runner

```
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```

#### Step 7: Setup GitHub Secrets for the following tags

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
AWS_ECR_LOGIN_URI
ECR_REPOSITORY_NAME
```

### Built With

* [PEGASUS](https://huggingface.co/google/pegasus-cnn_dailymail) - The HuggingFace model used

### Acknowledgements

This project was possible due the theoretical insructional videos by:
* Krish Naik
* Bappy Ahmed
