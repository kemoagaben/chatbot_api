from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = (
        f"FindBuyer yanıtı: '{user_input}' mesajınız alındı. "
        "En kısa sürede tarafınıza dönüş yapılacaktır."
    )
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
