from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # Run stress_cpu.py in a separate process
        subprocess.Popen(['python3', 'stress_cpu.py'])
        return 'Stress CPU process initiated\n', 200
    elif request.method == 'GET':
        # Get private IP address of EC2 instance
        private_ip = socket.gethostbyname(socket.gethostname())
        return f'Private IP address: {private_ip}\n', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


