import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
import os 
from dotenv import load_dotenv

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
    
    tittle_and_description = taking_description()

    for tittle,description in tittle_and_description:
        response = llm.invoke(
            input=f"""
            tittle:{tittle}
            description:{description}
            read the tittle,description and just give me factual claim in one sentence.
            """
        )
        gemini_response.append(response.content)

    return gemini_response

def response_saving():

    claim = calling_gemini()

    df = pd.read_csv("../../data/processed/unified_dataset.csv")
    df = df.assign(gemini_response=claim)

    df.to_csv("../../data/processed/unified_dataset.csv",index=False)

response_saving()