from flask import Flask


app = Flask(__name__)


@app.route('/', )
def index():
    return('Hello word!')


@app.route('/cat/', methods = ['POST', 'GET'])
def cat():
    
    return ('Hello word from catsq!')

@app.route('/cats/<int:id>')
def cats(id):
    return (f'Hello word from  {id}')



app.run(debug=True, host='0.0.0.0', port='6002')

