from flask import Flask, render_template

app = Flask(__name__) #instanciado
"""
# estamos usando la sintaxis decorador definiendo la ruta raiz de la app
@app.route('/')
def principal():
    return "Bienvenido a mi primer hola mundo usando Flask, y ahora estoy en debug mode" 

@app.route('/contacto')
def contacto():
    return "Esta es la pagina de contacto"
"""
# Cabe resaltar que Flask ya tiene un motor de plantillas llamado
#Jinja2, que es el mismo que ocupa dJango...
#creando una pantilla base que heredara a los demas archivos
@app.route('/')
def principal():
    #Tenemos que crear plantillas especificas para cada ruta y ver un formato en html
    return render_template('index.html')
#endpoints que se indican en la vista general
@app.route('/lenguajes')
def mostrarLenguajes():
    misLenguajes=("PHP", "JAVA", "C#", "Python", "Ruby",
                "JavaScript", "Perl", "Rust")
    return render_template('lenguajes.html', lenguajes=misLenguajes)


@app.route('/contacto')
def mostrarContacto():
    return render_template('contacto.html')#redir a la pagina que se desea

if __name__ == '__main__':
    #El parametro debug=True indica que estoy en desarrollo 
    # y hara que el servidor se reinicie automaticamente
    #guardando los nuevos cambios
    app.run(debug=True, port=5017)