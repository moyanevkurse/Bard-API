import github_api

api_key = install_api()

github = github_api.GitHubAPI(api_key)

# Получить список репозиториев пользователя
repos = github.get_repos()

# Получить информацию о репозитории
repo = github.get_repo("bard-api")

# Создать новый репозиторий
github.create_repo("my-new-repo")

# Добавить файл в репозиторий
github.add_file("my-file.txt", "Hello, world!")

# Коммитить изменения
github.commit("Add my-file.txt")

# Запушить изменения в репозиторий
github.push()
