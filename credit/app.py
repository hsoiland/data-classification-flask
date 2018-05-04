from flask import Flask
from models import db

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/creditdb' 
db.init_app(app)

@app.route("/")
def main():
    return 'Hello World !'

if __name__ == '__main__':
    app.run()
