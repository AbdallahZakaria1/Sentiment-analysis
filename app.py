from flask import Flask, request, jsonify, render_template
from analyzer import analyzer
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<nom>')
def page(nom):
       return render_template(f'{nom}.html')





@app.route('/submit', methods=['POST'])
def submit():
    input = request.get_json()['input']
    input = analyzer(input)
    return jsonify(response=f'Votre phrase est {input}')

if __name__ == '__main__':
    app.run(debug=True)