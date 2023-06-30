from flask import Flask, render_template, request
import requests

# Flask instance
app = Flask(__name__)

# First route


@app.route('/', methods=['GET','POST'])
def home():
    if request.method=='GET':
        return render_template('index.html')
    if request.form['search']:
        url = "https://api.giphy.com/v1/gifs/search?api_key=ql66snaJwZsfCk7b1WmRhUcuIdwvEVBc&limit=12&q=" + request.form['search']
        giphy = requests.get(url)
        dataGiphy = giphy.json()
        return render_template('index.html',data = dataGiphy['data'])
    else:
        return render_template('index.html')

def pagina_no_encontrada(error):
    return render_template('404.html'), 404

app.register_error_handler(404, pagina_no_encontrada)

if __name__ == '__main__':
    app.run(debug=True)
