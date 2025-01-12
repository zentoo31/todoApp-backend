from flask import Flask
from blueprints.userBlueprint import user_blueprint

app = Flask(__name__)
app.register_blueprint(blueprint=user_blueprint, url_prefix = '/user')


if __name__ == '__main__':
    app.run(debug=True)