def test_deletar_entrega():
    url = "https://healthcareapp.com/api/entregas"
    
    # Primeiro, cria uma nova entrega
    nova_entrega = {
        "paciente": "Carlos Pereira",
        "medicamento": "Paracetamol",
        "data_entrega": "2024-11-01",
        "endereco": "Rua Esperança, 321, Recife"
    }
    response = requests.post(url, json=nova_entrega)
    entrega_id = response.json()["id"]
    
    # Deletar a entrega criada
    response_delete = requests.delete(f"{url}/{entrega_id}")
    
    assert response_delete.status_code == 204  # Verifica se a remoção foi bem-sucedida
    
    # Verificar se a entrega realmente foi deletada
    response_check = requests.get(f"{url}/{entrega_id}")
    assert response_check.status_code == 404  # A entrega não deve mais existir
