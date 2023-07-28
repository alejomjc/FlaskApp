from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'J1$7qMf0@9z2'

@app.route('/')
def main():
    try:
        session['mascotas'] = session['mascotas'] if session['mascotas'] else []
    except:
        session['mascotas'] = []
    print('session', session['mascotas'])
    return render_template('index.html', mascotas=session['mascotas'])


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre_mascota = request.form['nombreMascota']
        nombre_dueno = request.form['nombreDueno']
        edad_mascota = request.form['edadMascota']
        tipo_mascota = request.form['tipoMascota']
        adicional = request.form['adicional']

        mascota = {'nombre': nombre_mascota,
                   'dueno': nombre_dueno,
                   'edad': edad_mascota,
                   'tipo': tipo_mascota,
                   'adicional': adicional}
        session['mascotas'] = session['mascotas'] + [mascota]
        return render_template('index.html', mascotas=session['mascotas'], mensaje='Registro exitoso')

    return render_template('registro.html')
