# server.py - AI Chatbot met Flask en Ollama
# ------------------------------------------
# Deze server beheert een webinterface waarmee gebruikers kunnen chatten met een lokaal LLM-model.

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests

# ------------------------------------------
# **Configuratie**
# ------------------------------------------
OLLAMA_API_URL = "http://localhost:11434/api/generate"  # Ollama draait lokaal
DEFAULT_MODEL = "llama3"  # Standaard model

app = Flask(__name__, static_folder='assets')
CORS(app)  # Sta frontend-toegang toe

conversation_history = []  # Houdt de chatgeschiedenis bij

# ------------------------------------------
# **Routes**
# ------------------------------------------

@app.route("/")
def serve_chat_interface():
    """Laadt de chatinterface."""
    return send_from_directory(".", "chat_interface.html")

@app.route("/assets/<path:filename>")
def serve_static_files(filename):
    """Laadt statische bestanden zoals afbeeldingen."""
    return send_from_directory("assets", filename)

@app.route("/chat", methods=["POST"])
def chat():
    """Verwerkt gebruikersvragen en stuurt ze naar de AI."""
    global conversation_history
    data = request.json
    user_message = data.get("message", "").strip()
    selected_model = data.get("model", DEFAULT_MODEL)

    if not user_message:
        return jsonify({"response": "Geen invoer ontvangen!"}), 400

    # Voeg het bericht toe aan de gesprekshistorie
    conversation_history.append({"role": "user", "content": user_message})

    # Maak een volledige prompt inclusief vorige berichten
    conversation_prompt = "\n".join(
        [f"{msg['role'].capitalize()}: {msg['content']}" for msg in conversation_history]
    )

    # Verstuur prompt naar Ollama
    payload = {"model": selected_model, "prompt": conversation_prompt, "stream": False}
    response = requests.post(OLLAMA_API_URL, json=payload)

    # Controleer of de AI een geldige reactie geeft
    if response.status_code != 200:
        return jsonify({"response": "Fout bij verwerking!"}), 500

    bot_response = response.json().get("response", "Geen reactie ontvangen!")

    # Voeg de AI-reactie toe aan de geschiedenis
    conversation_history.append({"role": "assistant", "content": bot_response})

    return jsonify({"response": bot_response})

# ------------------------------------------
# **Server starten**
# ------------------------------------------

if __name__ == "__main__":
    print("🚀 Server gestart op http://127.0.0.1:5004")
    app.run(debug=True, host="0.0.0.0", port=5004)
