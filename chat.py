import json, os

from flask import Flask
import openai

app = Flask(__name__)

@app.route("/")
def chat():
    # Comment sample response to avoid costs
    response = json.loads(
        '''
        { "choices": [ { "finish_reason": "stop", "index": 0, "logprobs": null, "text": " Sure, I can help you with that. May I ask why you're cancelling your subscription?" } ], "created": 1675375164, "id": "cmpl-6fbu0rQSjW3QBq2m5gBiOU38u3QSn", "model": "text-davinci-003", "object": "text_completion", "usage": { "completion_tokens": 20, "prompt_tokens": 66, "total_tokens": 86 } }
        '''
    )

    # Uncomment here to hit API
    # openai.api_key = os.getenv("OPENAI_API_KEY")    
    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
    #     temperature=0.9,
    #     max_tokens=10,
    #     top_p=1,
    #     frequency_penalty=0.0,
    #     presence_penalty=0.6,
    #     stop=[" Human:", " AI:"]
    # )

    return f"<p>{response}</p>"


