import pyxel
from langchain_upstage import ChatUpstage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
os.environ["UPSTAGE_API_KEY"] = os.getenv("UPSTAGE_API_KEY")

def text(x, y, text_str, col=7, shadow=1):
    pyxel.text(x, y + 1, text_str, shadow)
    pyxel.text(x, y, text_str, col)


def text_width(text_str):
    return len(text_str) * pyxel.FONT_WIDTH

def gen_choices(prompt, num_answers=3):
    llm = ChatUpstage()
    prompt = f"{prompt} Please provide {num_answers} possible answers."
    prompt_template = PromptTemplate.from_template(prompt)
    chain = prompt_template | llm | StrOutputParser()
    result = chain.invoke({})
    answers = result.strip().split("\n")
    return answers

def gen_text(prompt):
    llm = ChatUpstage()
    prompt_template = PromptTemplate.from_template(prompt)
    chain = prompt_template | llm | StrOutputParser()
    return chain.invoke({})