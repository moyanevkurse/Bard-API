import requests

class GitHubAPI:

    def __init__(self, api_key):
        self.api_key = api_key

    def request(self, method, path, params=None):
        """
        Отправляет запрос API GitHub.

        Args:
            method: Метод API.
            path: Путь к ресурсу.
            params: Параметры запроса.

        Returns:
            Ответ API.
        """

        response = requests.request(method, "https://api.github.com/" + path, params=params, headers={"Authorization": f"Bearer {self.api_key}"})
        if response.status_code != 200:
            raise Exception(f"Ошибка API: {response.status_code}")

        return json.loads(response.content.decode())

    def get_repos(self):
        """
        Получает список репозиториев пользователя.

        Returns:
            Список репозиториев.
        """

        return self.request("GET", "/user/repos")

    def get_repo(self, repo_name):
        """
        Получает информацию о репозитории.

        Args:
            repo_name: Имя репозитория.

        Returns:
            Информация о репозитории.
        """

        return self.request("GET", "/repos/<username>/<repo_name>")
