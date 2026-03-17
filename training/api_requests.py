import httpx


httpx = httpx.Client()

def all_posts():
    response = httpx.get('https://jsonplaceholder.typicode.com/posts')
    print(response.json())
    assert len(response.json()) == 100, 'Вернулись не все посты'

all_posts()

def one_post(post_id):
    response = httpx.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    print(response.json())
    assert response.json()['id'] == post_id, 'Не тот id'

one_post(2)

def post_something():
    response = httpx.post(
        'https://jsonplaceholder.typicode.com/posts',
        json={'title': 'My first post', "body": 'My "second" post', "user'Id": 1},
        headers={'Content-Type': 'application/json'}
    )
    print(response.json())

post_something()

def put_something():
    response = httpx.put(
        'https://jsonplaceholder.typicode.com/posts/21',
        json={'title': 'My first post', "body": 'My "seconnd" post', "user'Id": 1},
        headers={'Content-Type': 'application/json'}
    )
    print(response.json())

put_something()

def patch_something():
    response = httpx.patch(
        'https://jsonplaceholder.typicode.com/posts/21',
        json={'title': 'My first post', "user'Id": 7},
        headers={'Content-Type': 'application/json'}
    )
    print(response.json())

patch_something()

def delete_something():
    response = httpx.delete('https://jsonplaceholder.typicode.com/posts/21')
    print(response.json())
    print(response.status_code)

delete_something()