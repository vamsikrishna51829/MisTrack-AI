import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
import os 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

def taking_description():
    df = pd.read_csv("../../data/processed/unified_dataset.csv",usecols=["title","description"])
    return df.values

def extract_claim(GEMINI_API_KEY,title,description=None):

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key = GEMINI_API_KEY,
        temperature = 0.0
    )
    
    template = """
            Title:{title}
            Description:{description}
            read the Title,Description and just give me factual claim using the title and description if description not give me factual claim based on title in one sentence.
            no quotes
            no explanation 
            output just claim in one sentence
            """
    prompt = PromptTemplate.from_template(template=template)
    chain = prompt | llm
    try:
        response = chain.invoke({
            "title" : title,
            "description" : description
        })
        return response.content
    except Exception:
        return title
def response_saving():
    claim = []
    load_dotenv()

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    for title,description in taking_description():
        claim.append(extract_claim(GEMINI_API_KEY,title,description))

    df = pd.read_csv("../../data/processed/unified_dataset.csv")
    df = df.assign(extracted_claim=claim)

    df.to_csv("../../data/processed/unified_dataset.csv",index=False)

response_saving()