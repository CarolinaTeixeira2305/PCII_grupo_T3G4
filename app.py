from flask import Flask, render_template, request, session
from datafile import filename

import os

from classes.bilhete import Bilhete
from classes.cliente import Cliente
from classes.filme import Filme
from classes.filmefun import FilmeFun
from classes.funcionario import Funcionario
from classes.menu import Menu
from classes.reviews import Reviews
from classes.sessao import Sessão
from classes.userlogin import Userlogin

app = Flask(__name__)

Bilhete.read(filename + 'Filmedata.db')
Cliente.read(filename + 'Filmedata.db')
Filme.read(filename + 'Filmedata.db')
FilmeFun.read(filename + 'Filmedata.db')
Funcionario.read(filename + "Filmedata.db")
Menu.read(filename + 'Filmedata.db')
Reviews.read(filename + 'Filmedata.db')
Sessão.read(filename + 'Filmedata.db')
Userlogin.read(filename + "Filmedata.db")

prev_option = ""
submenu = ""
app.secret_key = 'FILME_SECRET_KEY'

upload_folder = os.path.join('static', 'FilmeFotos')
app.config['UPLOAD'] = upload_folder


import subs_login as lsub
import subs_gform as gfsub
import subs_gformT as gfTsub
import subs_subform as gfsubsub
import subs_filmeFoto as filmeFotosub
import subs_gform1 as gfsub1
import subs_gformCliente as gfsubCliente

 

@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"), usergroup=session.get("usergroup"))
    
@app.route("/login")
def login():
    return lsub.login()


@app.route("/logoff")
def logoff():
    return lsub.logoff()

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    return lsub.chklogin()

@app.route("/submenu", methods=["post","get"])
def getsubm():
    global submenu
    submenu = request.args.get("subm")
    return render_template("index.html", ulogin=session.get("user"),usergroup=session.get("usergroup"),submenu=submenu)

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname=''):
    submenu = request.args.get("subm")
    return gfsub.gform(cname,submenu)

@app.route("/gform1/<cname>", methods=["post","get"])
def gform1(cname=''):
    submenu = request.args.get("subm")
    return gfsub1.gform1(cname,submenu)

@app.route("/gformCliente/<cname>", methods=["post","get"])
def gformCliente(cname=''):
    submenu = request.args.get("subm")
    return gfsubCliente.gformCliente(cname,submenu)

@app.route("/gformT/<cname>", methods=["post","get"])
def gformT(cname=''):
    submenu = request.args.get("subm")
    return gfTsub.gformT(cname,submenu)

     
@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname=""):
    submenu = request.args.get("subm")
    return gfsubsub.subform(cname,submenu)


@app.route("/filmeform", methods=["post","get"])
def filmeFoto():
    submenu = request.args.get("subm")
    cname = 'Filme'
    return filmeFotosub.filmeFoto(app,cname,submenu)

@app.route("/order/mapa", methods=["post","get"])
def ordermapa():

    return render_template("uc.html", ulogin=session.get("user"),usergroup=session.get("usergroup"),submenu=submenu)

@app.route('/reviews')
def show_reviews():
    return render_template('reviews.html')

@app.route('/catalogo')
def catalogo():
    filmes = Filme.get_all_filmes()  
    return render_template("catalogo.html", filmes=filmes, ulogin=session.get("user"), usergroup=session.get("usergroup"))

@app.route('/menucliente')
def menu():
    return render_template("menucliente.html", ulogin=session.get("user"), usergroup=session.get("usergroup"))


if __name__ == '__main__':
    app.run(debug=True)
    #app.run()
