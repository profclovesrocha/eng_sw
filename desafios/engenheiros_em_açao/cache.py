import pytest
from app.main import app

@pytest.fixture
def client():
    return app.test_client()

def test_status_endpoint(client):
    """Valida se o healthcheck está online [cite: 58, 113]"""
    response = client.get('/status')
    assert response.status_code == 200
    assert response.json['status'] == "online"

def test_integrity_report_presence(client):
    """Garante que o relatório de integridade está presente no resumo [cite: 60, 115]"""
    response = client.get('/data/summary')
    assert response.status_code == 200
    assert "integrity_report" in response.json['meta']
    # Valida sanidade: preço negativo deve gerar erro no relatório [cite: 62, 119]
    assert response.json['meta']['integrity_report']['invalid_rows'] > 0