from flask import Flask, request, render_template
import random
import os
import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Add the following lines to specify the location of your templates folder
app = Flask(__name__)
app.template_folder = 'templates'

# Create a route to serve the index.html page


@app.route('/')
def index():
    return render_template('index.html')

# Define a function to generate a response


def generate_response(input_text):
    # Define a dictionary of prompts and corresponding responses
    prompts = {
        'hello': ['Looking for internships? we provide internships in every domain check out our website https://app.internship.codeclause.com/intern/dashboard '],
        'how are you': ['I\'m doing well, thanks!', 'I\'m fine, how about you?', 'Not too bad.'],
        'goodbye': ['Goodbye!', 'See you later!', 'Bye!'],
        'name': ['My name is Code clause.', 'I am Chatbot. Nice to meet you!']

    }

    # Preprocess the input text
    input_text = input_text.lower()

    # Look for a prompt that matches the input text
    for prompt, responses in prompts.items():
        if prompt in input_text:
            return random.choice(responses)

    # If no matching prompt was found, generate a default response
    return 'I\'m sorry, I didn\'t understand your message.'

# Create a route to handle incoming messages


@app.route('/message', methods=['POST'])
def handle_message():
    message = request.form['message']
    response = generate_response(message)
    return response


if __name__ == '__main__':
    app.run(debug=True)
