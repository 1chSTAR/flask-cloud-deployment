from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route('/webhook-endpoint', methods=['POST'])
def handle_webhook():
    data = request.json

    # You can add more verification to ensure it's a legitimate request from DockerHub
    if 'callback_url' in data:
        try:
            # Stop the current container
            stop_command = "docker stop YOUR_CONTAINER_NAME_OR_ID"
            subprocess.call(stop_command, shell=True)

            # Pull the latest image
            pull_command = "docker pull YOUR_DOCKER_IMAGE_NAME:TAG"
            subprocess.call(pull_command, shell=True)

            # Start a new container
            run_command = "docker run YOUR_RUN_OPTIONS YOUR_DOCKER_IMAGE_NAME:TAG"
            subprocess.call(run_command, shell=True)

            return jsonify({'status': 'success'}), 200
        except Exception as e:
            return jsonify({'status': 'failed', 'error': str(e)}), 500
    else:
        return jsonify({'status': 'bad request'}), 400

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
