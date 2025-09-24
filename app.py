from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title="Halaman Index")

@app.route('/about')
def about():
    return "Ini adalah halaman about"

@app.route('/halo/<name>')
def halo(name):
    return f"Halo <strong> {name}</strong> !! Apa Kabar???"

if __name__ == '__main__':
    app.run(debug=True) 