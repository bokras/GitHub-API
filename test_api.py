import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPOSITORY_NAME = os.getenv("REPOSITORY_NAME")

GITHUB_API_URL = "https://api.github.com"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def create_repository():
    url = f"{GITHUB_API_URL}/user/repos"
    data = {
        "name": REPOSITORY_NAME,
        "private": False,
        "description": "Test repository created by API",
    }
    response = requests.post(url, headers=HEADERS, json=data)
    response.raise_for_status()

    if response.status_code == 201:
        print(f"Репозиторий {REPOSITORY_NAME} успешно создан.")
    else:
        print(f"Ошибка создания репозитория: {response.text}")

def check_repository():
    url = f"{GITHUB_API_URL}/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()

    repos = response.json()
    for repo in repos:
        if repo["name"] == REPOSITORY_NAME:
            print(f"Репозиторий {REPOSITORY_NAME} найден.")
            return True
    print(f"Репозиторий {REPOSITORY_NAME} не найден.")
    return False

def delete_repository():
    url = f"{GITHUB_API_URL}/repos/{GITHUB_USERNAME}/{REPOSITORY_NAME}"
    response = requests.delete(url, headers=HEADERS)

    if response.status_code == 204:
        print(f"Репозиторий {REPOSITORY_NAME} успешно удален.")
    else:
        print(f"Ошибка удаления репозитория: {response.text}")

if __name__ == "__main__":
    create_repository()
    check_repository()
    delete_repository()
