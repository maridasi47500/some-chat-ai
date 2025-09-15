from flask import Flask, render_template, request
from stacks import frontends, backends, databases
from itertools import product

app = Flask(__name__)

@app.route('/transport', methods=['POST'])
def transport():
    selected = request.form.get('transport')
    return render_template('form.html', transport=selected)


@app.route('/', methods=['GET', 'POST'])
def index():
    selected_combinations = []
    if request.method == 'POST':
        selected_frontend = request.form.get('frontend')
        selected_backend = request.form.get('backend')
        selected_database = request.form.get('database')
        selected_combinations.append({
            'frontend': selected_frontend,
            'backend': selected_backend,
            'database': selected_database
        })
    return render_template('form.html',
                           frontends=frontends,
                           backends=backends,
                           databases=databases,
                           combinations=selected_combinations)

if __name__ == '__main__':
    app.run(debug=True)

