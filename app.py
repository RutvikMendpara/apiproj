from flask import Flask, request

app = Flask(__name__)


@app.route('/reverse', methods=['POST'])
def reverse_string():
    input_string = request.args.get('string')
    return {'output_string': input_string[::-1]}


if __name__ == '__main__':
    app.run(debug=True)