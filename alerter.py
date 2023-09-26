import subprocess
from flask import Flask

app = Flask(__name__)



@app.route('/webhook/<script>', methods=['GET'])
def webhook(script):
    script_path =  #path to your script goes here
    try:
        subprocess.check_call(script_path, shell=True)
        return '', 200  
    except subprocess.CalledProcessError as e:
        return str(e), 500  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
