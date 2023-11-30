from flask import Flask, jsonify, send_from_directory
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')

@app.route('/run_playbook/<router>')
def run_playbook(router):
    try:
        limit = router if router != 'all' else ''
        result = subprocess.run(
            ['ansible-playbook', '-i', 'inventory.yml', 'playbook_verify_ospf_status.yml', '--limit', limit],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return jsonify({'stdout': result.stdout, 
                        'stder': result.stderr, 
                        'returncode': result.returncode
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')