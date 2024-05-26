from flask import Flask, render_template, request, session
from werkzeug.utils import secure_filename
import os

from classes.filme import Filme

prev_option = ""
img = ""
error_message = ""

def filmeFoto(app, cname='', submenu=""):
    global img
    global prev_option
    global error_message  # Declare error_message as global
    ulogin = session.get("user")
    if ulogin is not None:
        cl = eval(cname)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        
        error_message = ""  # Reset error message
        
        if prev_option == 'insert' and option == 'save':
            if cl.auto_number == 1:
                strobj = "None"
            else:
                strobj = request.form[cl.att[0]]
            
            file = request.files['img']
            if file:
                filename = secure_filename(file.filename)
                file_ext = filename.rsplit('.', 1)[1].lower()
                if file_ext != 'jpeg':
                    error_message = "Apenas imagens com extensão .jpeg são aceites"
                else:
                    film_code = request.form[cl.att[0]] 
                    file.save(os.path.join("static/images", f"{film_code}.jpeg"))
                    foto = f"{film_code}.jpeg"
                    
                    for i in range(1, len(cl.att)):
                        att = cl.att[i]
                        if att != '_foto':
                            strobj += ";" + request.form[cl.att[i]]
                        else:
                            strobj += ";" + foto

                    obj = cl.from_string(strobj)
                    cl.insert(getattr(obj, cl.att[0]))
                    cl.last()

        elif prev_option == 'edit' and option == 'save':
            obj = cl.current()
            
            file = request.files['img']
            if file:
                filename = secure_filename(file.filename)
                file_ext = filename.rsplit('.', 1)[1].lower()
                if file_ext != 'jpeg':
                    error_message = "Apenas imagens com extensão .jpeg são aceites"
                else:
                    film_code = getattr(obj, cl.att[0])  
                    file.save(os.path.join("static/images", f"{film_code}.jpeg"))
                    foto = f"{film_code}.jpeg"
                    
                    for i in range(cl.auto_number, len(cl.att)):
                        att = cl.att[i]
                        if att != '_foto':
                            setattr(obj, att, request.form[att])
                        else:
                            setattr(obj, att, foto)

                    cl.update(getattr(obj, cl.att[0]))

        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            elif option == "delete":
                obj = cl.current()
                cl.remove(obj.code)
                if not cl.previous():
                    cl.first()
            elif option == "insert":
                butshow = "disabled"
                butedit = "enabled"
            elif option == 'cancel':
                pass
            elif option == "first":
                cl.first()
            elif option == "previous":
                cl.previous()
            elif option == "next":
                cl.nextrec()
            elif option == "last":
                cl.last()
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"))

        prev_option = option
        obj = cl.current()
        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            for att in cl.att:
                obj[att] = ""
            img = os.path.join("static/images", "None.jpeg")
        else:
            if obj._foto == "" or obj._foto == "None":
                img = os.path.join("static/images", "None.jpeg")
            else:
                img = os.path.join("static/images", obj._foto)

        return render_template("filmeform.html", butshow=butshow, butedit=butedit,
                               cname=cname, obj=obj, att=cl.att, header=cl.header, des=cl.des,
                               ulogin=session.get("user"), usergroup=session.get("usergroup"), auto_number=cl.auto_number,
                               img=img, submenu=submenu, error_message=error_message)
    else:
        return render_template("index.html", ulogin=ulogin, usergroup=session.get("usergroup"))
