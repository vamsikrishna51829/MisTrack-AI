import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
import os 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

def taking_description():
    df = pd.read_csv("../../data/processed/unified_dataset.csv",usecols=["title","description"])
    return df.values

def calling_gemini():
    load_dotenv()

    gemini_response = []
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key = GEMINI_API_KEY,
        temperature = 0.0
    )
    
    title_and_description = taking_description()

    template = """
            Title:{title}
            Description:{description}
            read the Title,Description and just give me factual claim in one sentence.
            no quotes
            no explanation 
            output just claim in one sentence
            """
    prompt = PromptTemplate.from_template(template=template)
    chain = prompt | llm
    for title,description in title_and_description:
        response = chain.invoke({
            "title" : {title},
            "description" : {description}
        })
        gemini_response.append(response.content)

    return gemini_response

def response_saving():

    claim = calling_gemini()

    df = pd.read_csv("../../data/processed/unified_dataset.csv")
    df = df.assign(gemini_response=claim)

    df.to_csv("../../data/processed/unified_dataset.csv",index=False)

response_saving()