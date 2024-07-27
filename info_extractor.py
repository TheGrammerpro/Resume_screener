from dotenv import load_dotenv
from openai import OpenAI
import ast
import os

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


class InfoExtractor:
    def __init__(self, text):
        self.base_prompt = """You extract specific information from text for candidate classification in a csv file.
        extract the name, the email, the state, the phone number, title of companies worked at and how long they worked 
        there, college degrees and where the degrees were obtained, all the skills. Your output should come in the form 
        of a Python dictionary in the following format: {'name': 'candidate name', 'email': 'candidate@email.com', 
        'phone number': '5646876543', 'county & city': 'USA, New York', 'companies worked at':['Apple Inc.: tech field (2015-2018)', 
        'Disney: entertainment (2018-current)'], 'experience (years)': 9 (This is calculated based on the difference between 
        first year in experience and last or current year, should be integer), 'degrees': ['Computer science bachelor at Oxford', 
        'English bachelor at community college'], 'skills': ['SQL', 'CSS', 'Python', 'Project Management', 'Data Analysis']}
        \n*rules:\n
        \n-When you use lists, don't add multiple elements at once like this ['languages: SQL, java, Python'], 
        it should be like this ['SQL', 'Java', 'Python']
        \n-Your output should only include the dictionary
        \n-No need for any introductions such as 'here is what you requested'
        \n-No need to explain what you did
        \n-Don't add "```python" or such text before or after your output"""
        self.info_dict = {}
        self.extract_openai(text)

    def extract_openai(self, text):
        creation_prompt = f"""
            Answer the query below based only on the following context:

            {text}

            ---

            Answer the question above based on the following guidelines:
            {self.base_prompt}"""
        client = OpenAI(api_key=OPENAI_API_KEY)

        messages = [{"role": "user", "content": creation_prompt}]

        # Calls gpt-4o-mini:
        response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)

        # Calls agent's answer and stores it in a variable:
        self.info_dict = ast.literal_eval(response.choices[0].message.content)
