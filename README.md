# openai-chat-flask
## OpenAI chat with a Flask API.

```
git clone git@github.com:seanhelvey/openai-chat-flask.git
cd openai-chat-flask
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
flask --app chat run
```

In your browser now you can visit http://127.0.0.1:5000.  

In the code you can comment the sample response and uncomment the API request to hit the API.