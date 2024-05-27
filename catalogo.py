# -*- coding: utf-8 -*-
"""

#objective: catalogo.py

"""""
from flask import Flask, render_template, request, session

from classes.bilhete import Bilhete
from classes.cliente import Cliente
from classes.filme import Filme
from classes.filmefun import FilmeFun
from classes.funcionario import Funcionario
from classes.menu import Menu
from classes.reviews import Reviews
from classes.sessao import Sessao
from classes.userlogin import Userlogin

prev_option = ""

def catalogo(cname='',submenu=""):
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        return render_template("catalogo.html",
                        ulogin=session.get("user"),
                        usergroup=session.get("usergroup"),
                        submenu=submenu)
    else:
        return render_template("index.html", ulogin=ulogin)