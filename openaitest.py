import openai

# Set your OpenAI API key here
openai.api_key = "sk-proj-zKWz5teV7Mzasug4HE45T3BlbkFJAB0oRU92Ba3Qrbgn8Hgt"

# Your prompt details
profile_summary = """
Ashok Singh — Lead Engineer with 12 years of experience in full-stack development, AI, and cloud solutions.
Expert in Python, Flask, FastAPI, Django, AWS, Docker, Kubernetes, Celery, Kafka, and Airflow.
Specialized in ETL pipelines, data engineering, LLM integrations (LangChain, RAG), and microservice architectures.
Strong leadership background in managing teams, architecting scalable systems, and delivering high-performance backend solutions.
"""

job_posting = """
Python Lead
Hyderabad
8 - 13 years
Not Disclosed
In office
Python, kafka, Node js, React.Js

Job description
Job Description: Python Lead Developer Location: Hyderabad, India Experience: 8+ Years Employment Type: Full-time
...
(Your full job description text)
...
"""

# The system prompt to guide the model
system_prompt = """
You are a helpful assistant that extracts structured JSON information from a given user profile and job description.
Extract the information into the following JSON format:
{
 "company_name":"",
 "about_company":"",
 "job_profile":"",
 "location":"",
 "experience":"",
 "skills":"",
 "job_description":"",
 "notice_period":"",
 "profile_match_percent":""
}
Return only valid JSON output without any extra text.
"""

# Combine the user prompt
user_prompt = f"""
My Profile summary is:
{profile_summary}

and job posting from the recruiter is:
{job_posting}

Generate the JSON as per the given format.
"""

# Call the OpenAI ChatCompletion API
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.0  # Lower temperature for more deterministic output
)

# Extract and print the response
output_json = response['choices'][0]['message']['content']
print(output_json)

