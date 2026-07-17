from langgraph.graph import StateGraph,START,END
from typing import TypedDict
from pandas import DataFrame

class process(TypedDict):
    keyword : str
    newsapi_df : DataFrame
    mastodon_df : DataFrame
    merged_df : DataFrame
    claims_df : DataFrame
