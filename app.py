from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    response = requests.get(f"{GITHUB_API_URL}/users/{username}", headers=headers)
    return jsonify(response.json()), response.status_code

@app.route('/repos', methods=['POST'])
def create_repo():
    data = request.get_json()
    response = requests.post(f"{GITHUB_API_URL}/user/repos", headers=headers, json=data)
    return jsonify(response.json()), response.status_code

@app.route('/repos/<owner>/<repo>', methods=['PATCH'])
def update_repo(owner, repo):
    data = request.get_json()
    response = requests.patch(f"{GITHUB_API_URL}/repos/{owner}/{repo}", headers=headers, json=data)
    return jsonify(response.json()), response.status_code

@app.route('/repos/<owner>/<repo>', methods=['DELETE'])
def delete_repo(owner, repo):
    response = requests.delete(f"{GITHUB_API_URL}/repos/{owner}/{repo}", headers=headers)
    return jsonify(message="DELETE request sent to GitHub"), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
