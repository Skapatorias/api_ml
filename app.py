from flask import Flask, render_template, request
from logica  import isMutant

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('mutantes.html')


@app.route('/mutant/<adn>', methods=['POST'])
def post(adn):
    dna= eval(adn)
    if isMutant(dna['dna']):
        return  "Es mutante", 200
    else:  
        return  "No es mutante", 403
        

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == "POST":
        adn = request.form['adn']
        if isMutant(adn):
            return render_template('agregado_m.html')
        else:
            return render_template('agregado_h.html')


if __name__ == "__main__":
    app.run()