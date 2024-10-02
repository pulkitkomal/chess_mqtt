import requests
import json
import time
import os
from dotenv import load_dotenv

# Load .env from the parent directory
load_dotenv('.env')

# Now you can access your environment variables
openai_api_key = os.getenv('openai_api_key')

class OPENAI:
    def __init__(self) -> None:
        # defining as a global variable
        self.api_key = openai_api_key # Replace this with your actual API key

    def create_prompt(self, data):
        prompt = """
    given this data, give next best move for the black side, stick to given output format, donot add any other data. The output should be in standard json RFC 8259 format but it should be plain text.
    example output = {"piece":'', "position":''}"""
        return data+prompt

    def call_openai(self, prompt):
        url = 'https://api.openai.com/v1/chat/completions'  # Use this endpoint for ChatGPT or the completion endpoint for language models

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }

        # Define the payload for your request
        data = {
            'model': 'gpt-4o-mini',  # Change to 'gpt-4' if you are using that model
            'messages': [
                {'role': 'user', 'content':self.create_prompt(data=prompt)}
            ],
            'max_tokens': 100,  # Specify the maximum number of tokens to generate
        }

        # Make the request to the OpenAI API
        for i, attempt in enumerate(range(3)):  # Retry up to 3 times
            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                response_data = response.json()
                assistant_reply = response_data.get('choices')[0].get('message').get('content')

                # Convert assistant_reply to JSON
                try:
                    assistant_reply_json = json.loads(assistant_reply)
                except json.JSONDecodeError:
                    print(f"OPENAI: Response was not valid JSON, retrying... {assistant_reply}")
                    time.sleep(1)  # Wait before retrying
                    continue
                
                print(f'OPENAI: got response on {i} try ... {assistant_reply_json}')
                return assistant_reply_json
            else:
                print(f"OPENAI: Request failed with status code {response.status_code}")
                print(response.json())
                return json.dumps(response.json())