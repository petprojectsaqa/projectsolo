import pytest
import httpx


@pytest.fixture()
def new_post_id():
    body = {"title": "title_name", "body": "body_name", "userId": 1}
    headers = {'Content-Type': 'application/json'}
    response = httpx.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
    post_id = response.json()['id']
    post_id = 99  # песочница не создает реальную сущность, поэтому подменяем её
    yield post_id
    print(f'Deleting the post, id: {post_id}')
    httpx.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')

@pytest.fixture(scope='session')
def hello():
    print('hello')
    yield
    print('end')
