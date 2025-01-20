from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello, World! CI/CD with Git, AWS, Docker, Terraform, and Pytest!"
