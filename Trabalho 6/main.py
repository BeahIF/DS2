# -*- coding: utf-8 -*-


from flask import *
import sys
import os
from persistencia import *
from jinja2 import TemplateNotFound
from admin import *
from jornalista import *
from leitor import *
import json
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
#from flask_static_compress import FlaskStaticCompress


app = Flask(__name__)
#compress = FlaskStaticCompress(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/trabalho5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
db = SQLAlchemy(app)

mail = Mail()
app.config.update(
	DEBUG=True,
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT = 465,
	MAIL_USE_SSL = True,
	MAIL_USERNAME= 'tadsfds2',
	MAIL_PASSWORD= 'mifael12345'
)
mail.init_app(app)

app.config['UPLOAD_FOLDER'] = 'C:/Users/usuario/Downloads/IFRS 2018/DS2/Trabalho 4/static/arquivos/'
app.secret_key = "chave_secreta"
app.register_blueprint(admin, url_prefix='/admin')


app.register_blueprint(jornalista, url_prefix='/jornalista')

app.register_blueprint(leitor, url_prefix='/leitor')

@app.route("/tela_email")
def tela_email():
	return render_template("email.html")

@app.route("/email", methods=['POST'])
def email():
	print "here entrei no email"
	texto =	request.form['email']
  	#print texto
  	
  	msg = Message("Hello", sender = 'tadsfds2@gmail.com', recipients = [texto])
	msg.html = "<br>alalalal<br>"
	mail.send(msg)
 	
   	return "Sent"

@app.before_request
def antes_da_rota():
	if request.path != '/' :
		if request.path != '/logar' :
			if request.path != '/login':
				if request.path != '/ajax':
					if request.path != '/leitor/tela_adicionar':
						if request.path != '/leitor/cria_leitor':
							if 'login' not in session:
								session['login'] = 0
							testa = str(session['login'])
							if testa == 'None':
								return render_template("erro.html", mensagem = "operacao proibida")
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r        

@app.route("/dados")
def dados_ajax():
	return render_template("dados.html")

@app.route("/info")
def info():
	# note that we set the 404 status explicitly
    return render_template('404.html'), 404
@app.route("/pesquisa")
def pesquisa():
	return render_template("ajax.html", mensagem="")

@app.route('/ajax', methods = ['POST'])
def ajax_request():
    username = request.form['username']
    return jsonify(username=username)

@app.route('/pesquisando', methods = ['POST'])
def pesquisando():
    campo = request.form['campo']
    print campo
    # busca somente uma unica noticia
    # noticia = NoticiaDAO().busca(campo)
    
    vetNoticia = []

    # se o campo nao veio em branco
    if (len(campo) > 0):
        vetNoticia = NoticiaDAO().busca2(campo)
    
    resultado = ""
    for n in vetNoticia:
        resultado = resultado  +n.titulo+   "<br>"
    return resultado

    # SERIA O CORRETO
    # return json.dumps(vetNoticia)
    # return jsonify(titulo=noticia.titulo, texto=noticia.texto)


@app.route("/")
def index():
	if 'perfil' not in session:
		session['perfil'] = 0
	perfil = session['perfil']
	noticiaDAO = NoticiaDAO()
	return render_template("index.html",vetNoticia = noticiaDAO.listar(), perfil = perfil, mensagem="")
@app.route("/logar")
def logar():
	return render_template("login.html", mensagem="")

@app.route("/login", methods=['POST'])
def login():
	print "here"
	login = request.form['login']
	login = str(login)
#	print login
	senha = request.form['senha']
	senha = str(senha)
	perfil = str(request.form['perfil'])	
#	print perfil
	session['login'] = login
	session['senha'] = senha
	session['perfil'] = perfil
#	print session['login']
	#PERGUNTAR COMO ENVIAR SENHA PARA AS OUTRAS ROTAS
	
	if(perfil == "admin"):
		print "entrei"
		if(senha == "admin" and login == "admin"):
			flash('You were successfully logged as Admin')
			return redirect("/admin/tela_inicial")
	else:
		if(perfil == "leitor"):
			return redirect("/leitor/tela_inicial")
		else:
			if(perfil == "jornalista"):
				print "jjjj"
				return redirect("/jornalista/tela_inicial")
	return redirect("/")			

@app.route("/perfil/<id>")
def perfil(id):
	id = str(id)
	if(session['perfil'] == jornalista):
		return render_template("perfil.html", url="/jornalista/edita_perfil/"+id)

@app.route("/comentarios/<id>")
def comentarios(id):
	id = str(id)
	print session['login']
	login = session['login']
	leitorDAO = LeitorDAO()
	nome_leitor = leitorDAO.obter_nome(login)

	comentarioDAO = ComentarioDAO()

	return render_template("comentarios.html", comentarios = comentarioDAO.listar_por_noticia(id), nome_leitor = nome_leitor)

@app.route("/adicionar_comentario/<id>")
def adicionar_comentario(id):
	print session['perfil']
	if(session['perfil'] == "leitor"):
		leitorDAO = LeitorDAO()
		return render_template("novo_comentario.html", id_leitor = leitorDAO.obter_id(session['login']), id_noticia= id)
	else:
		return redirect("/logar")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
@app.errorhandler(405)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('405.html'), 404

@app.route("/logout")
def logout():
    session['login'] = None
    session['senha'] = None
    print session
    return redirect("/")
@app.route("/qual_perfil")
def qual_perfil():
	print "qual_perfil"
	print session['perfil']
	perfil = str(session['perfil'])
	if perfil == "leitor":
		return redirect("/leitor/meu_perfil")

@app.route("/noticia_por_jornalista")
def noticia_por_jornalista():
	noticiaDAO = NoticiaDAO()
	vet = noticiaDAO.noticia_por_jornalista()
	resultado = ""
	for n in vet:
		resultado = resultado + str(n.jornalista) +"->" +str(n.titulo)+"<br>"
	return resultado
if __name__ == '__main__':
	# para arrumar os acentos (principalmente no windows)
	reload(sys)
	#compress.init_app(app)
	sys.setdefaultencoding('UTF-8')
	app.run()


