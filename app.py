from flask import Flask, render_template

from controllers.pet_controller import pets_blueprint
from controllers.vet_controller import vets_blueprint
from controllers.owner_controller import owners_blueprint

app = Flask(__name__)

app.register_blueprint(pets_blueprint)
app.register_blueprint(vets_blueprint)
app.register_blueprint(owners_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)