import pytest
import requests


@pytest.fixture
def base_url():
    return 'http://localhost:5000'  # Замените на соответствующий URL вашего Flask-сервиса


def test_create_card(base_url):
    url = f'{base_url}/card'
    data = {
        'number': '1234-5678-9012-3456',
        'cvv': 123,
        'issue': '01/23',
        'expiration': '01/25',
        'status': 'new',
        'balance': 100
    }

    response = requests.post(url, json=data)
    assert response.status_code == 201
    assert response.json() == {'message': 'Card created successfully'}

    # Проверяем, что данные сохранены в базе данных
    card_number = data['number']
    card_url = f'{base_url}/card/{card_number}'
    response = requests.get(card_url)
    assert response.status_code == 200
    assert card_number in response.text


def test_get_card(base_url):
    # Предварительно вставляем тестовую запись в базу данных
    card_number = '1234-5678-9012-3456'
    card = {
        'number': card_number,
        'cvv': 123,
        'issue': '01/23',
        'expiration': '01/25',
        'status': 'new',
        'balance': 100
    }
    card_url = f'{base_url}/card/{card_number}'
    requests.post(f'{base_url}/card', json=card)

    # Получаем данные с использованием GET запроса
    response = requests.get(card_url)
    assert response.status_code == 200
    assert card_number in response.text
    assert card['cvv'] in response.text
    assert card['issue'] in response.text
    assert card['expiration'] in response.text
    assert card['status'] in response.text
    assert str(card['balance']) in response.text


if __name__ == '__main__':
    pytest.main()
