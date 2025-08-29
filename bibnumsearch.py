from flask import Flask, request, render_template, jsonify
import bible  # assuming my_script.py is the name of your Python script

app = Flask(__name__)

#app.config['APPLICATION_ROOT'] = '/app'

@app.route('/submit', methods=['POST'])
def submit():
        my_number = request.form['my_number']
        result = bible.scriptures(my_number)
        return jsonify(result)

@app.route('/bible')
def bible_route():
        return render_template('index.html')

@app.route('/')
def root_route():
    return render_template('index.html')


if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)
