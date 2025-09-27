from flask import Flask,render_template

app=Flask(__name__)

data={
    "nama":"Muhammad Rizky",
    "alamat":"Cilacap",
    "jenis_kelamin":"Laki-laki",
    "pekerjaan":"Mahasiswa",
    "tempat_lahir":"Cilacap",
    "tanggal_lahir":"2003-01-01",
    "foto":"senyum.png"
}

@app.route('/')
def index():
    return render_template('index.html',title="Halaman Index",isi="Selamat Datang di Website Flask")

@app.route('/about')
def about():
   return render_template('about.html',title="Halaman About",isi="Ini Halaman About")

@app.route('/biodata')
def biodata():
    return render_template('biodata.html',title="Biodata",isi=data)

if __name__ == '__main__':
    app.run(debug=True) 