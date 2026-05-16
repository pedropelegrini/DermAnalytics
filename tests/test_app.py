from Backend.app import app


def test_app_carrega():
    assert app is not None


def test_rota_dados_responde():
    client = app.test_client()
    response = client.get("/dados")

    assert response.status_code == 200
    assert response.is_json