from flask import Flask
from flask.json import jsonify
from redis import Redis
import arrow


app = Flask(__name__)
app.config.from_pyfile("settings.py")

r = Redis(unix_socket_path=app.config["REDIS_URL"])


@app.route("/health")
def home():
    health_status = dict(health=r.ping(), timestamp=arrow.utcnow().timestamp())

    return jsonify(health_status)


if __name__ == "__main__":
    app.run()
