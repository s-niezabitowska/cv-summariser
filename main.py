import os
from dotenv import load_dotenv
import openai

# Load the API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Sample CV text
sample_cv = """
Name: Sophia Niezabitowska
Email: s.niezabitowska@outlook.com
Education:
- BSc Computing and IT (Software Development), The Open University, 2028
Experience:
- Data and Process Analyst at STARK, 2025-present
- HR Systems Assistant at Builders Co, 2022-2025
Skills:
- Python, Power Automate, Excel, SQL
"""

# AI prompt to analyse CV
prompt = f"""
You are an HR assistant AI. Extract the following information from this CV:
- Full Name
- Contact Email
- Education
- Work Experience
- Skills

Format the output as a simple list.

CV Text:
{sample_cv}
"""

# Call OpenAI Chat Completions API
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Print the AI's response
print(response.choices[0].message.content.strip())
