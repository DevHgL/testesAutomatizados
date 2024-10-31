import requests

BASE_URL = "https://suaapi.com/api"


def test_consulta_pontos_coleta_sucesso():
    # Parâmetros da rota
    params = {
        "rota": "rota_valida"
    }
    
    # Realiza a requisição
    response = requests.get(f"{BASE_URL}/pontos-coleta", params=params)
    
    # Valida o status code
    assert response.status_code == 200  # OK
    
    # Valida que existem pontos de coleta retornados
    data = response.json()
    assert len(data['pontos']) > 0
    assert "localizacao" in data['pontos'][0]  # Verifica a estrutura dos dados

def test_consulta_pontos_coleta_sem_resultados():
    # Parâmetros da rota sem pontos de coleta
    params = {
        "rota": "rota_sem_pontos"
    }
    
    # Realiza a requisição
    response = requests.get(f"{BASE_URL}/pontos-coleta", params=params)
    
    # Valida o status code
    assert response.status_code == 404  # Nenhum ponto encontrado
    
    # Valida a mensagem de retorno
    data = response.json()
    assert data['message'] == "Nenhum ponto de coleta disponível nesta rota"
