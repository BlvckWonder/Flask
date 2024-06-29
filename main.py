from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = 'manasesija'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/par mani')
def par_mums():
    return render_template('par mani.html')

@app.route('/kontakti')
def kontakti():
    return render_template('kontakti.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')
    
@app.route('/pamati_sintakse')
def pamati_sintakse():
    return render_template('pamati_sintakse.html')
    
@app.route('/mainigie')
def mainigie():
    vards = "Anna"
    vecums = 33
    vecums2 = vecums + vecums
    return render_template('mainigie.html', vards=vards, vecums=vecums)

@app.route('/datu_tipi')
def datu_tipi():
    teksts = "Sveika pasaule!"
    skaitlis = 10
    decimals = 3.14
    saraksts = [1, 2, 3, 4, 5]
    mans_dict = {"vards":"Anna", "vecums": 33}
    mans_kopa = {1, 2, 3, 4, 5}
    return render_template('datu_tipi.html', teksts=teksts,                      skaitlis=skaitlis, decimals=decimals, saraksts=saraksts,                     mans_dict=mans_dict, mans_kopa=mans_kopa)

@app.route('/sveiciens')
def sveiciens():
    return render_template('sveiciens.html')

@app.route('/operatori')
def operatori():
    a = 10
    b = 3
    summa = a + b
    starpība = a - b
    reizinajum = a * b
    dalijums = a / b
    atlikums = a % b
    vienads = (a == b)
    return render_template('operatori.html', summa=summa, reizinajums=reizinajums, 
dalijums=dalijums, starpiba=starpība, atlikums=atlikums, vienads=vienads  )

@app.route('/kontroles_strukturas')
def kontroles_strukturas():
    x = 3
    if x > 5:
        rezultats = "x ir lielāks par 5"
    else:
        rezultats = "x ir mazāks par 5"
    for_cikla_rezultats = [i for i in range(6, 31)]
    while_cikla_rezultats = []
    y = 0
    while y < 10:
        while_cikla_rezultats.append(y)
        y += 1

    return render_template('kontroles_strukturas.html', rezultats=rezultats, 
                           for_cikla_rezultats=for_cikla_rezultats, 
                           while_cikla_rezultats=while_cikla_rezultats)


@app.route('/funkcijas')
def funkcijas():
    def sveiciens(vards="Jānis"):
        return f"Sveiki! {vards}!"
    sveiciens1 = sveiciens()
    sveiciens2 = sveiciens("Anna")

    return render_template('funkcijas.html', sveiciens1=sveiciens1, sveiciens2=sveiciens2)

@app.route('/failu_apstrade')
def failu_apstrade():
    saturs= ""
    with open("teksts.txt", "r") as fails:
        saturs = fails.read()
    return render_template('failu_apstrade.html', saturs=saturs)

@app.route('/moduli')
def moduli():
    import math
    sqrt_rezultats = math.sqrt(16)
    return render_template('moduli.html', sqrt_rezultats=sqrt_rezultats)

@app.route('/aptauja')
def aptauja():
    return render_template('aptauja.html')

@app.route('/pieteikties', methods=['GET', 'POST'])
def pieteikties():
    if request.method == 'POST':
    lietotajvards = request.form['lietotajvards']
    parole = request.form['parole']

    conn = sqlite3.connect('datubaze.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM lietotaji WHERE lietotajvards = 7", (lietotajvards,) 
    admin = cursor.fetchone()
    conn.close()

    if admin and check_password_hash(admin[2], parole):
        session['lietotajvards'] = lietotajvards
        return redirect(url_for('panelis'))
    else:
        flash('Nepareizs lietotājvārds vai parole!!!!!')
                   
    return render_template('pieteikties.html')

@app.route('/panelis')
def panelis():
    if 'lietotajvards' not in session:
        return redirect(url_for('pieteikties'))
    conn = sqlite3.connect('datubaze.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM lietotaji')
    lietotaji = cursor.fetchall()
    conn.close()
    return render_template('panelis.html', lietotaji=lietotaji)


@app.route('/iesniegt', methods=['POST'])
def iesniegt():
    vards = request.form['vards']
    dzimums = request.form['dzimums']
    hobiji = request.form.getlist('hobiji')
    hobiji_str = ', '.join(hobiji)
    conn = sqlite3.connect('datubaze.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO lietotaji (vards, dzimums, hobiji) VALUES (?, ?, ?)', 
                 (vards, dzimums, hobiji_str))
    conn.commit()
    conn.close()
    
    return render_template('paldies.html')

def init_db():
    conn = sqlite3.connect('datubaze.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lietotaji (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vards TEXT NOT NULL,
            dzimums TEXT NOT NULL,
            hobiji TEXT
            )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS administratori (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lietotajvards TEXT NOT NULL,
            parole TEXT NOT NULL
            )
    ''')

    cursor.execute('SELECT * FROM administratori WHERE lietotajvards = ?', ('admin',))
    if not cursor.fetchone():
        cursor.execute('INSERT INTO administratori (lietotajvards, parole) VALUES (?, ?)',( 'admin', generate_password_hash('admin')))
    conn.commit()
    conn.close()

init_db()


@app.route('/aiziet', methods=['POST'])
def aiziet():
    lietotajs = request.form['lietotajvards']
    return f"Paldies, {lietotajs}! Jūsu pieteikums ir saņemts"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
