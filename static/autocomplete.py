from flask import Flask, render_template, jsonify
from flask_autoComplete import AutoComplete

app = Flask(__name__)
autoComplete = AutoComplete(app)

films = films

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autocomplete', methods=['GET'])
@autoComplete('src')
def autocomplete():
    query = request.args.get('q', '')  # Get the search query from the request
    results = filter(lambda film: film.startswith(query), films)
    return jsonify(results)

if __name__ == '__main__':
    app.run()
