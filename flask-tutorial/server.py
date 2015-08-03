from flask import Flask
from flask import request
import models
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/stats/<id>/<date1>/<date2>', strict_slashes=False)
def render_date_range(id, date1, date2):
    dt_format = "%Y-%m-%d"
    try:
        date1 = dt.strptime(date1, dt_format)
        date2 = dt.strptime(date2, dt_format).replace(hour=23, minute=59, second=59)
    except:
        return render_template("date_error.html")

## Get and Post a Todo
@app.route('/todos', strict_slashes=False, methods=('get', 'post'))
def todo():
    title = request.args.get('title')
    content = request.args.get('content')
    
    ## Create a new todo
    todo = models.Todo(title, content)
    
    ## Connect to the database here
    ##models.db.create_all()
    models.db.session.add(todo)
    models.db.session.commit()
    
    ## Return a JSON response
    return json.dumps({'results':'success'})
    

if __name__ == '__main__':
    app.run(debug=True)