import os

from dotenv import load_dotenv
from flask import Flask

from app.config.routes import routes_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.register_blueprint(routes_bp)
load_dotenv()


@app.route('/health')
def health_check():
    return "Status: Up!"


if __name__ == "__main__":
    app.run(debug=True)
