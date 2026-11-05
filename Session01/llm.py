from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(model="gpt-4o-mini", input="write most in-demand skills for freshers to get hired in the AI era in India 2026 and on  Wards")

print(response.output_text)