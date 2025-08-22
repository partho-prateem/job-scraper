import streamlit as sl
import pandas as pd

sl.title("AI/ML Job Market Insights")
df= pd.read_csv("Jobs_cleaned.csv")
sl.write("###Preview of job data", df.head())