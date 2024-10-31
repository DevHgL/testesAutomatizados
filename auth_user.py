import requests
import pytest
from jsonschema import validate

# URL base da API
BASE_URL = "https://example.com/api"

# Esquema JSON para validação de contrato da API de login
login_schema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "token": {"type": "string"}
    },
    "required": ["message", "token"]
}

def test_login_sucesso():
    # Dados de login válidos
    payload = {
        "email": "usuario@example.com",
        "senha": "senha123"
    }
    
    # Realiza a requisição
    response = requests.post(f"{BASE_URL}/login", json=payload)
    
    # Valida o status code
    assert response.status_code == 200

    # Valida o corpo da resposta
    data = response.json()
    assert data['message'] == "Login efetuado com sucesso"
    assert "token" in data  # Verifica se o token está presente

    # Valida o esquema JSON (contrato)
    validate(instance=data, schema=login_schema)

def test_login_falha_senha_incorreta():
    # Dados de login inválidos
    payload = {
        "email": "usuario@example.com",
        "senha": "senha_incorreta"
    }
    
    # Realiza a requisição
    response = requests.post(f"{BASE_URL}/login", json=payload)
    
    # Valida o status code
    assert response.status_code == 401  # Acesso negado
    
    # Valida a mensagem de erro
    data = response.json()
    assert data['message'] == "Credenciais inválidas"
