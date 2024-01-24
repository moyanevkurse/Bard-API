import requests

def install_api():
    """
    Устанавливает API GitHub на локальную машину.
    """

    response = requests.get("https://api.github.com/install")
    if response.status_code != 200:
        raise Exception(f"Ошибка установки API: {response.status_code}")

    json_data = json.loads(response.content.decode())
    api_key = json_data["api_key"]

    print(f"API-ключ: {api_key}")

    return api_key
