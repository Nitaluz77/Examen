# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

USUARIOS ={"juan":"admin","pepe":"user"}

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def total():
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        edad1 = int(request.form['edad1'])
        numero1 = int(request.form['numero1'])

        precio_tarro: int = 9000

        total_sin_descuento = precio_tarro * numero1

        if 18 <= edad1 <= 30:
            descuento = 0.15
        elif edad1 > 30:
            descuento = 0.25
        else:
            descuento = 0.0

        total_descuento = total_sin_descuento * descuento
        total_a_pagar = total_sin_descuento - total_descuento

        return render_template('ejercicio1.html', nombre1=nombre1, total_sin_descuento=total_sin_descuento, total_descuento=total_descuento, total_a_pagar=total_a_pagar)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        contrasena1 = request.form['contraseña1']

        if nombre1 in USUARIOS and USUARIOS[nombre1] == contrasena1:
            if nombre1 == "juan":
                mensaje = f"Bienvenido administrador {nombre1}"
            elif nombre1 == "pepe":
                mensaje = f"Bienvenido usuario {nombre1}"
            return render_template('ejercicio2.html', mensaje=mensaje)
        else:
            error = "Usuario o contraseña incorrectos"
        return render_template('ejercicio2.html', error=error)
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)