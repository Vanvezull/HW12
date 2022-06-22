import json
from json import JSONDecodeError
from exception import DataError


def load_posts():
    try:
        with open('posts.json', 'r', encoding='utf-8') as file:
            posts = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        raise DataError('Файл поврежден')
    return posts


def search_post_cont(user_content):
    posts = load_posts()
    search_result = []
    for post in posts:
        if user_content.lower() in post['content'].lower():
            search_result.append(post)
    return search_result


def add_post(picture, content):
    posts = load_posts()
    user_post = {'pic': picture, 'content': content}
    posts.append(user_post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        return json.dump(posts, file, ensure_ascii=False, indent=2)












