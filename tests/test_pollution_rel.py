import requests

BASE_URL = "https://suaapi.com/api"

def test_submissao_relatorio_sucesso():
    # Dados do relatório de poluição
    payload = {
        "localizacao": "Praia do Forte",
        "descricao": "Água contaminada com resíduos plásticos",
        "foto": "imagem_base64"
    }
    
    # Realiza a requisição
    response = requests.post(f"{BASE_URL}/report", json=payload)
    
    # Valida o status code
    assert response.status_code == 201  # Criado
    
    # Valida a mensagem de sucesso
    data = response.json()
    assert data['message'] == "Relatório enviado com sucesso"

def test_submissao_relatorio_falha():
    # Dados do relatório incompleto (falta a descrição)
    payload = {
        "localizacao": "Praia do Forte",
        "foto": "imagem_base64"
    }
    
    # Realiza a requisição
    response = requests.post(f"{BASE_URL}/report", json=payload)
    
    # Valida o status code
    assert response.status_code == 400  # Requisição mal-formada
    
    # Valida a mensagem de erro
    data = response.json()
    assert data['message'] == "Preencha todos os campos obrigatórios"
