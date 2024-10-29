def test_buscar_entregas():
    url = "https://healthcareapp.com/api/entregas"
    
    # Buscar todas as entregas
    response = requests.get(url)
    assert response.status_code == 200  # Verifica se a resposta é OK
    assert len(response.json()) > 0  # Verifica se há entregas registradas
    
    # Buscar uma entrega específica pelo ID
    entrega_id = response.json()[0]['id']  # Pega o primeiro ID de entrega
    response_entrega = requests.get(f"{url}/{entrega_id}")
    assert response_entrega.status_code == 200  # Verifica se a entrega foi encontrada
    assert response_entrega.json()["id"] == entrega_id  # Confirma o ID da entrega
