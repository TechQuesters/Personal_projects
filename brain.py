import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Access environment variables
secret_key = os.getenv("API_KEY")
# AI model configuration
genai.configure(api_key=secret_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def getAnswer(prompt)->str:
    response = model.generate_content(prompt)
    output = response.text.replace('*','')
    return output

if __name__=="__main__":
    
    pro = input("Enter query : ")
    print('Loading.........')
    output = getAnswer(pro)
    output=output.replace('*','')
    print(output)
