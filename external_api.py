import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
import requests

def base_api_call_steam(extended_url):
    try:
        base_url = os.environ["STEAM_API_URL"]
        url = f"{base_url}{extended_url}"
        response = requests.get(url)


        if response.status_code == 200:
            data = response.json()  # Convierte la respuesta en JSON a un diccionario de Python
            return data
        
        print("Error en la solicitud:", response.status_code)
        return None
    except Exception as ex:
        print("API: call_api_steam")
        print(ex)
        return None

def list_single_player_games():
    """Lista de juegos que posee un jugador"""

    steam_api_key = os.environ["STEAM_API_KEY"]
    steam_user_id = os.environ["STEAM_USER_ID"]
    url = f"IPlayerService/GetOwnedGames/v0001/?key={steam_api_key}&steamid={steam_user_id}&format=json&include_played_free_games=true&include_appinfo=true"
    res = base_api_call_steam(url)
    if res['response']['game_count'] > 0:
        games = res['response']['games']
        return ", ".join(list(map(lambda x: x['name'], games)))
        
    return []
