from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db.sqlite'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(120))
    
    def __init__(self, title, content):
        self.title = title
        self.content = content
        
    def __repr__(self):
        return '{} {}'.format(self.title, self.content)
    
    
db.create_all()
db.session.commit()
