from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "There is nothing here"


@app.route('/test', methods=['POST'])
def test():
    return {"type": "section", "text": {"type": "mrkdwn", "text": "A message *with some bold text* and _some italicized text_."}}


if __name__ == "__main__":
    app.run(host='0.0.0.0')
