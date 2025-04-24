from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print("Telegram Message Received:", data)
    return 'OK', 200

if __name__ == '__main__':
    app.run()
