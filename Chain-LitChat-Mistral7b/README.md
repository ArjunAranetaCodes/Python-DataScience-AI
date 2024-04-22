# Mixtral-8x7B LLM with LangChain and Chainlit Chat UI

## Prerequisites
* Python 3.1 or higher

# Steps to Run Chainlit App
Fork this repository. Download load it locally

Install the required Python packages by running the following command in your terminal:

```
pip install chainlit langchain dotenv
```
Create a .env file in the project directory. You can use the example.env file as a reference. Add your Hugging Face API token to the .env file in the following format:

HUGGINGFACEHUB_API_TOKEN = your_token_here

Run the following command:
```
chainlit run app.py -w
```
This will launch Chainlit UI and you will be able to chat with the Mixtral-8x7B LLM.

Enjoy using Mistalai LLM with LangChain and Chainlit!
