def test_atualizar_entrega():
    url = "https://healthcareapp.com/api/entregas"
    
    # Primeiro, cria uma nova entrega
    nova_entrega = {
        "paciente": "Maria Souza",
        "medicamento": "Antibiótico",
        "data_entrega": "2024-10-31",
        "endereco": "Av. Saúde, 456, Rio de Janeiro"
    }
    response = requests.post(url, json=nova_entrega)
    entrega_id = response.json()["id"]
    
    # Atualiza o endereço da entrega criada
    update_data = {"endereco": "Rua Nova, 789, Rio de Janeiro"}
    response_update = requests.put(f"{url}/{entrega_id}", json=update_data)
    
    assert response_update.status_code == 200  # Verifica se a atualização foi bem-sucedida
    assert response_update.json()["endereco"] == "Rua Nova, 789"  # Verifica se o endereço foi atualizado
