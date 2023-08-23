from flask import render_template, request, jsonify
from lib.freshservice_client import FreshServiceClient
from lib.openai import ChatAssistant
from lib.text_processor import TextProcessor

chat_assistant = ChatAssistant()
freshservice_client = FreshServiceClient()
text_processor = TextProcessor()

def index():
    return render_template('index.html')

def chat():
    message = request.form['message']

    # Retrieve Freshservice results based on the incoming message
    freshservice_results = freshservice_client.get_solution_articles(message, params={"per_page": 3}, max_page=1)

    # Add user message to ChatAssistant
    chat_assistant.add_message("user", message)

    for result in freshservice_results[0:]:
        chat_assistant.add_message("system", text_processor.preprocess(result[1]))

    # Generate a response using the ChatAssistant instance
    response = chat_assistant.generate_response()

    # Check if the response is a string
    if isinstance(response, str):
        # Add response message to ChatAssistant
        chat_assistant.add_message("assistant", response)
    else:
        # Handle the error when the response is not a string
        # You can log the error or display an error message to the user
        print("Error: Invalid response format")

    return jsonify({'message': response})

def clear_messages():
    chat_assistant.clear_messages()
    chat_assistant.save_messages()
    return jsonify({'message': 'Messages cleared'})