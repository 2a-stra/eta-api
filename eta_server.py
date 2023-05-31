from flask import Flask, request

app = Flask(__name__)

@app.route('/calculate_eta', methods=['POST'])
def login():

    print(request.json)

    body = {"eta": "2023-05-31T17:00:00"}
    return body

if __name__ == "__main__":
    app.run(debug = False, host = "0.0.0.0", port = 8080)