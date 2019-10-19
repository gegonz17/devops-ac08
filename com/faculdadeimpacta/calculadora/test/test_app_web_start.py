from com.faculdadeimpacta.calculadora import app_web_start

def test_root_status():

app_web_start = app_web_start.app.test_client()

response = app_web_start.get('/')

assert response.status_code == 200, 'Deveria existir essa rota'

def test_root_url():

app_web_start = app_web_start.app.test_client()

response = app_web_start.get('/')

assert response.data.decode('utf-8') == 'Index Page', 'Deveria ser Index Page'