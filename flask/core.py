from flask import Flask
import subprocess

app = Flask(__name__)


@app.route("/")
def hello_world():
    return {"message": "hello world!"}


@app.route("/vrising")
def vrising():
    msg = subprocess.run(
        ["./scripts/start_v_rising.sh"], stdout=subprocess.PIPE
    ).stdout.decode("utf-8")
    return {"message": msg}
