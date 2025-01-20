from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! CI/CD with Git, AWS, Docker, Terraform, and Pytest!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
