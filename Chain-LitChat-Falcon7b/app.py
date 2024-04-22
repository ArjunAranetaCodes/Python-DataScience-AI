# pip install chainlit langchain dotenv

import os
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import chainlit as cl
from dotenv import load_dotenv

load_dotenv()

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system",
            """
            You are an AI assistant that provides helpful answers to user queries.
            """),
        ("user", "{question}\n"),
    ]
)


@cl.on_chat_start
def main():
    model_id = 'tiiuae/falcon-7b-instruct'

    llm = HuggingFaceEndpoint(
        repo_id=model_id, max_length=2000, temperature=0.5, token=os.environ['HUGGINGFACEHUB_API_TOKEN']
    )

    llm_chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True)

    cl.user_session.set("llm_chain", llm_chain)


@cl.on_message
async def main(message: cl.Message):
    llm = cl.user_session.get("llm_chain")
    res = await llm.acall(message.content, callbacks=[cl.AsyncLangchainCallbackHandler()])
    await cl.Message(content=res["text"]).send()

# chainlit run app.py -w