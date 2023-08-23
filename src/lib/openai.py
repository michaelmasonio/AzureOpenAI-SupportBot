import json
import random
import openai

from lib.freshservice_client import FreshServiceClient

openai.api_version = '2023-05-15'
openai.api_base = ''
openai.api_type = "azure"
openai.api_key = ''

class ChatAssistant:
    def __init__(self):
        # Load messages from JSON file
        self.load_messages()

    def generate_response(self):
        # # Add solution articles to messages as system for context
        # self.add_solution_articles_to_messages()
    
        # Convert messages to correct format
        formatted_messages = []
        for message in self.messages:
            formatted_message = {
                "role": message["role"],
                "content": str(message["content"])
            }
            formatted_messages.append(formatted_message)
    
        # Generate openai response
        response = openai.ChatCompletion.create(
            engine="gpt-35-turbo",
            messages=formatted_messages[-5:],
            temperature=random.uniform(0.5, 1.0),
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
        )
    
        # Save messages to JSON file
        self.save_messages()
    
        # Extract the content from the response
        content = response['choices'][0]['message']['content']
    
        return content

    def load_messages(self):
        try:
            with open('messages.json', 'r') as file:
                self.messages = json.load(file)
        except FileNotFoundError:
            self.messages = []

    def save_messages(self):
        with open('messages.json', 'w') as file:
            json.dump(self.messages, file)

    def add_message(self, role, content):
        message = {"role": role, "content": content}
        self.messages.append(message)
        # Save updated messages to JSON file
        self.save_messages()

    def clear_messages(self):
        self.messages = self.messages[:2]
