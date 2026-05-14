# Medical-Chatbot

# How to run?
### STEPS:

Clone the respository

```bash
project repo: https://github.com/OlaoyeData/Medical-Chatbot.git/
```
### STEP 01- Create a conda environment after opening the respository
 ```bash
 conda create -n medibot python -y
 ```

 ```bash
 conda activate medibot
 ```

 ### STEP 02- install the requirements
 ```bash
 pip install -r requirements.txt
 ```

 ### Create a .env file in the root directory and add your Pinecone and Gemini credentials as follows:

 ```bash
 PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
 GEMINI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
 ```

 ```bash
 #run the following command to store embeddings to pinecone
 python store_index.py
 ```

 ```bash
 #Finally run the following command
 python app.py
 ```

 Now,
 ```bash
 Open up localhost:
 ```

 ### Techstack used:

 - Python
 - Langchain
 - Flask
 - GPT
 - Pinecone

 # AWS-CICD-Deployment-with-Github-Actions

 ## 1. Login to AWS console.

 ## 2. Create IAN user for deployment

        #with specific access

        1. EC2 access : It is virtual machine

        2. ECR: Elastic Container registry to save your docker image in aws

        #Description: About the deployment

        1. Build docker iamge of the source code

        2. Push your docker image to ECR

        3. Launch Your EC2

        4. Pull Your image from ECR in EC2

        5. Launch your docker image in EC2

        #Policy:

        1. AmazonEC2ContainerRegistryFullAccess

        2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image
        - Save the URI: 315865595366.dkr.ecr.us-east-1.amazonaws.com/medibot

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and install docker in EC2 machine:

        #optional

        sudo apt-get update-y

        sudo apt-get upgrade

        #required

        curl -fsSL https://get.docker.com -o get-docker.sh

        sudo sh get-docker.sh

        sudo usermod -aG docker ubuntu

        newgrp docker

# 6. Configure EC2 as self-hosted runner:
        setting>actions>runner>new self hosted runner>choose os>then run command one by one

# 7. Setup github secrets:

        - AWS_ACCESS_KEY_ID
        - AWS_SECRET_ACCESS_KEY
        - AWS_DEFAULT_REGION
        - ECR_REPO
        - PINECONE_API_KEY
        - GEMINI_API_KEY
