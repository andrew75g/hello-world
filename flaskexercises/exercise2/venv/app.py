from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/result', methods=['GET'])
def result():
    number = request.args.get('number', '')  # Get the number from query parameter
    if number:
        try:
            number = int(number)
            result = 'even' if number % 2 == 0 else 'odd'
        except ValueError:
            result = 'not an integer'
    else:
        result = 'no number provided'

    return render_template('result.html', number=number, result=result)

if __name__ == '__main__':
    app.run(debug=True)
