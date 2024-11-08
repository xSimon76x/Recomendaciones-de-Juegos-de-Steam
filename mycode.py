import os
from flask import Flask
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
from external_api import list_single_player_games
from bot_ia import bot_chat
from langchain.memory import ChatMessageHistory

app = Flask(__name__)
history = ChatMessageHistory()

@app.route("/")
def recommend_game():

    data = list_single_player_games()

    bot = bot_chat(data, history)

    return bot

if __name__ == '__main__':
    app.run(debug=True)


# Ejecutar sv local:  flask --app mycode run --debug