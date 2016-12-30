from flask import Flask, render_template, request, make_response

from examples.xai_filter import generate_xai_filter

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Xai.filter', methods=['POST'])
def generate_filter():
    filter_string = str(generate_xai_filter(request.form))

    response = make_response(filter_string)
    response.headers['Content-Disposition'] = 'attachment; filename=Xai.filter'
    return response

if __name__ == '__main__':
    app.run()
