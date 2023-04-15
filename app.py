from flask import Flask, request , render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>String Reverser API</title>
        </head>
        <body>
            <h1>String Reverser API</h1>
            <p>This API has one endpoint: <code>/reverse</code></p>
            <p>To use the endpoint, send a <code>POST</code> request with a form field named <code>string</code> containing the string you want to reverse.</p>
            <p>The endpoint will return the reverse of the input string.</p>
        </body>
    </html>
    """
    return render_template_string(html)

@app.route('/reverse', methods=['POST'])
def reverse_string():
    input_string = request.args.get('string')
    return {'output_string': input_string[::-1]}


if __name__ == '__main__':
    app.run(debug=True)