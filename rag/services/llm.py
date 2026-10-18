# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model =ChatGoogleGenerativeAI(model="gemini-3.5-flash")

result=model.invoke("tell me about imrankhan and all his contribution in pakistan")
print(result.text)