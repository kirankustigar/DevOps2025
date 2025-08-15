from flask import Flask
  # Capital F

app = Flask(__name__)
    # Capital F here too
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
