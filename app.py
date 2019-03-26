from flask import Flask
from flask import render_template, jsonify, request
import requests
app = Flask(__name__)


@app.route('/webhook')
def hello_world():
    """
    Sample hello world
    """

    return render_template('home.html')


@app.route('/chat', methods=["POST"])
def chat():
    """
    chat end point that performs NLU using rasa.ai
    and constructs response from response.py
    """
    # try:
    user_message = request.form["text"]
    response = requests.get("http://localhost:5055/parse", params={"q": user_message})
    response = response.json()
    entities = response.get("entities")
    topresponse = response["intent"]
    intent = topresponse.get("name")
    print("Intent {}, Entities {}".format(intent, entities))
    if intent == "gst-info":
        response_text = gst_info(
            entities)
    elif intent == "gst-query":
        response_text = gst_query(entities)
    else:
        response_text = get_random_response(intent)
    return jsonify({"status": "success", "response": response_text})


if __name__ == "__main__":
    app.run(debug=True)
