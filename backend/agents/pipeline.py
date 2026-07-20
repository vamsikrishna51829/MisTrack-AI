from langgraph.graph import StateGraph,START,END
from typing import TypedDict
import pandas as pd
from newsapi_fetcher import get_news_from_newsapi
from mastodon_fetcher import get_news_from_mastodon
from dataset_builder import news_combine
from claim_extractor import response_saving
from similarity_engine import similarity_engine

class state(TypedDict):
    keyword : str
    newsapi_df : pd.DataFrame
    mastodon_df : pd.DataFrame
    merged_df : pd.DataFrame
    claims_df : pd.DataFrame
    similar_df : pd.DataFrame

def pipeline():

    graph = StateGraph(state)

    graph.add_node("fetcher_newsapi_node",newsapi_node)
    graph.add_node("fetcher_mastodon_node",mastodon_node)
    graph.add_node("merge_data_node",merge_data_node)
    graph.add_node("claim_extraction_node",claim_extration_node)
    graph.add_node("similar_node",similar_node)
    graph.add_edge(START,"fetcher_newsapi_node")
    graph.add_edge(START,"fetcher_mastodon_node")
    graph.add_edge("fetcher_newsapi_node","merge_data_node")
    graph.add_edge("fetcher_mastodon_node","merge_data_node")
    graph.add_edge("merge_data_node","claim_extraction_node")
    graph.add_edge("claim_extraction_node","similar_node")
    graph.add_edge("similar_node",END)

    graph = graph.compile()

    result = graph.invoke({
        "keyword":"MLA rip",
        
    })

    return result

def newsapi_node(state):
    try:
        get_news_from_newsapi(state["keyword"])
        df = pd.read_csv("../../data/raw/newsapi_KEYWORD_TIMESTAMP.csv")
        state["newsapi_df"] = df

    except Exception as e:
        print(e)

    return state

def mastodon_node(state):
    try:
        get_news_from_mastodon(state["keyword"])
        df = pd.read_csv("../../data/raw/Mastodonapi_KEYWORD_TIMESTAMP.csv")
        state["mastodon_df"] = df
    
    except Exception as e:
        print(e)

    return state

def merge_data_node(state):
    
    news_combine()
    df = pd.read_csv("../../data/processed/unified_dataset.csv")
    state["merged_df"] = df

    return state

def claim_extration_node(state):
    
    response_saving()
    df = pd.read_csv("../../data/processed/unified_dataset.csv")
    state["claims_df"] = df

    return state

def similar_node(state):

    similarity_engine(0.8)
    df = pd.read_csv("../../data/processed/similarity_dataset.csv")
    state["similar_df"] = df

    return state

print(pipeline())