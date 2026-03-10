import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Ideia(db.Model):
    __tablename__ = "ideias"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    ideia = db.Column(db.String(255), nullable=False)
    data_criacao = db.Column(db.DateTime, server_default=func.now())
    tempo_dias = db.Column(db.Integer)
    categoria = db.Column(db.String(255))

@app.route('/')
def index():
    ideias = Ideia.query.order_by(Ideia.data_criacao).all()
    return render_template('index.html', ideias=ideias)

@app.route("/insert", methods=["GET", "POST"])
def insert():
    if request.method == "POST":
        nome = request.form["nome"]
        tempo = request.form["tempo"]
        categoria = ','.join(request.form.getlist("categoria"))
        descricao = request.form["descricao"]

        nova_ideia = Ideia(
            nome=nome,
            ideia=descricao,
            tempo_dias=int(tempo),
            categoria=categoria
        )

        db.session.add(nova_ideia)
        db.session.commit()

        return redirect("/")

        
    return render_template('insert.html')

@app.route("/view/<int:id>")
def view(id):
    ideia = Ideia.query.get_or_404(id)
    return render_template("view.html", ideia=ideia)

@app.route("/delete/<int:id>")
def delete(id):
    id = Ideia.query.get_or_404(id)

    try:
        db.session.delete(id)
        db.session.commit()

        return redirect("/")
    except Exception as e:
        return f"Houve um problema para deletar esta tarefa: {str(e)}"
    
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    ideia = Ideia.query.get_or_404(id)

    if request.method == "POST":
        ideia.nome = request.form["nome"]
        ideia.ideia = request.form["descricao"]
        ideia.tempo_dias = int(request.form["tempo"])
        ideia.categoria = ",".join(request.form.getlist("categoria"))

        db.session.commit()

        return redirect("/")

    return render_template("edit.html", ideia=ideia)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=4949, debug=True)
