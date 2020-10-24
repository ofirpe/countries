from flask import Flask, render_template, url_for
import requests

# restcountries API
# Mozilla Public License MPL 2.0

app = Flask(__name__)


# enum injection - credit to sean-vieira
# profile: https://stackoverflow.com/users/135978/sean-vieira
# https://stackoverflow.com/questions/27035728/flask-cannot-import-enumerate-undefinederror-enumerate-is-undefined
@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/countries_by_flag')
def countries_by_flag():
    api_result = requests.get('https://restcountries.eu/rest/v2/all')
    api_json = api_result.json()
    images = [(c['flag'], c['name']) for c in api_json]
    return render_template('countries_by_flag.html', flags=images)


@app.route('/result/<i>')
def result(i):
    api_result = requests.get('https://restcountries.eu/rest/v2/all')
    result_id = int(i)
    api_json = api_result.json()[result_id]

    return render_template(
         'result.html',
         name=api_json['name'],
         capital=api_json['capital'],
         region=api_json['region'],
         population=api_json['population'],
         flag=api_json['flag'],
         timezones=api_json['timezones']
     )


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
