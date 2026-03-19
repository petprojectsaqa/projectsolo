import httpx
import pytest


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

@pytest.mark.regression
def test_get_one_post(new_post_id):
    response = httpx.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    assert response['id'] == new_post_id

def test_get_all_posts(hello):
    response = httpx.get(f'https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100

def test_add_post():
    body = {
        "title": "title",
        "body": "body",
        "userId": 1,
    }
    headers = {'Content-Type': 'application/json'}
    response = httpx.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers,
    )

    assert response.status_code == 201
    assert response.json()['id'] == 101

@pytest.mark.parametrize('num', [1, 4, 2, 9])
def test_num(num):
    assert num == num
    print('yes')

