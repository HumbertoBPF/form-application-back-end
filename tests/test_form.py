from faker.generator import random

from common.states import STATES

url = "/submitFormulario"


def test_form_empty_payload(client):
    response = client.post(url, json={})
    assert response.status_code == 400


def test_form(client, faker):
    payload = {
        "page_1": {
            "full_name": faker.name(),
            "national_id": "0123456789",
            "position": "Desenvolvedor",
            "city": "Minha Cidade",
            "state": random.choice(STATES),
            "is_correct": True,
            "titularity": "titular",
            "phone": faker.phone_number(),
            "email": faker.email(),
            "birth_date": "2000-01-01",
            "gender": "male",
            "weight": random.randint(60, 100),
            "height": random.randint(150, 200),
            "min_pressure": "",
            "max_pressure": "",
            "know_pressure": False
        },
        "page_2": {
            "diseases": [
                {"id": 1, "name": "Diabetes", "choices": ["2"]},
                {"id": 2, "name": "Problemas Cardíacos", "choices": ["2"]},
                {"id": 3, "name": "Pressão Alta", "choices": ["2"]}, {"id": 4, "name": "Asma", "choices": ["2"]},
                {"id": 5, "name": "Depressão", "choices": ["2"]}, {"id": 6, "name": "Ansiedade", "choices": ["2"]},
                {"id": 7, "name": "Colesterol Alto", "choices": ["2"]},
                {"id": 8, "name": "Dores nas Costas", "choices": ["2"]},
                {"id": 9, "name": "Dores nas Articulações", "choices": ["2"]},
                {"id": 10, "name": "Dores de Cabeça", "choices": ["2"]}, {"id": 11, "name": "Câncer", "choices": ["2"]},
                {"id": 12, "name": "Infecções Sexualmente Transmissíveis", "choices": ["2"]}],
            "remarks": faker.text()
        },
        "page_3": {
            "type": "Sem Restrição",
            "options": [
                "Doces (doces de qualquer tipo, bolos recheados com cobertura, biscoitos doces, refrigerantes e sucos industrializados)",
                "Grãos (arroz, milho e outros grãos)",
                "Massas"
            ]
        }
    }
    response = client.post(url, json=payload)
    assert response.status_code == 200
