from flask import Flask, render_template, request, jsonify, send_file, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/templates/index.html')
def index():
    return render_template("index.html")


if __name__=="__main__":
    app.run(host='0.0.0.0', port=80)

   #test comment
