from langchain_deepseek import ChatDeepSeek
import os
from dotenv import load_dotenv

load_dotenv() # load environment variables from .env file

llm = ChatDeepSeek(
    model="deepseek-chat",
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
)

messages = [
    ("system", "You are a helpful translator. Translate the user sentence to Spanish."),
    ("human", "I love programming."),
]


response = llm.invoke(messages)
print(response)