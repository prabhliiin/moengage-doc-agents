import os
from dotenv import load_dotenv
import google.generativeai as genai

# 👇 Load the .env file
load_dotenv()

# ✅ Now the env var is available to os.getenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text
