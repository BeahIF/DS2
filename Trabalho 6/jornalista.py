from flask import *
from modelo import * 
from persistencia import *
jornalista = Blueprint('jornalista', __name__,
                      template_folder='jornalista/templates', static_folder = 'jornalista/static')

@jornalista.route("/tela_inicial", methods=['GET','POST'])
def jornalista_tela_inicial():
	#print "jornalistaaaaaa"
	login = session['login']
	#print login
	senha = session['senha']
	#print senha
	perfil = "jornalista"
	jornalistaDAO = JornalistaDAO()
	
	retorno = jornalistaDAO.testa(login, senha)

	#print retorno
	if(retorno == True):
		noticiaDAO = NoticiaDAO()
		id = jornalistaDAO.obter_id(login)
	#	print id
		return render_template("gerencia.html", vetNoticia = noticiaDAO.listar(), mensagem = "", id=id)
	else:
		return render_template("login.html",mensagem="Login ou senha incorreta")
@jornalista.route("/inicio")
def jornalista_inicio():
	noticiaDAO = NoticiaDAO()
	jornalistaDAO = JornalistaDAO()
	id = jornalistaDAO.obter_id(login)
	return render_template("gerencia.html", vetNoticia = noticiaDAO.listar(), mensagem="", id=id)

@jornalista.route("/tela_adicionar_assunto")
def jornalista_tela_adicionar_assunto():
	return render_template("adiciona_assunto.html", mensagem="")

@jornalista.route("/adicionando_assunto", methods=['POST'])
def jornalista_adicionando_assunto():
	nome = request.form['nome']
	assuntoDAO = AssuntoDAO()
	assunto = Assunto(nome)
	noticiaDAO = NoticiaDAO()
	#print noticiaDAO.listar()
	jornalistaDAO = JornalistaDAO()
	try:
		assuntoDAO.adiciona(assunto)
		login = str(session['login'])
		id = jornalistaDAO.obter_id(login)
		return render_template("gerencia.html",vetNoticia=noticiaDAO.listar(), mensagem="Assunto adicionado!", id=id)
	except Exception as e:
		return "Erro ao adicionar assunto!"

@jornalista.route("/tela_adicionar_noticia")
def jornalista_tela_adicionar_noticia():
	assuntoDAO = AssuntoDAO()
	#print assuntoDAO.listar()
	return render_template("adiciona_noticia.html", url = "/jornalista/adicionando_noticia", titulo = "", texto = "", data = "", vetAssunto= assuntoDAO.listar(), mensagem="")

@jornalista.route("/adicionando_noticia", methods=['POST'])
def jornalista_adicionando_noticia():
	print "adiciona"
	jornalistaDAO = JornalistaDAO()
	login = str(session['login'])

	id = jornalistaDAO.obter_id(login)

	titulo = request.form['titulo']
	texto = request.form['texto']
	data = str(request.form['data'])
	#print data
	assunto = request.form['assunto'] 
	#print assunto
	noticiaDAO = NoticiaDAO()
	id_assunto = noticiaDAO.id_assunto(assunto)
	print id_assunto
	id_assunto = int(id_assunto)
	#id = int(id)
	print id
	noticia = Noticia(titulo, texto,data, id_assunto, id)
	try:
		noticiaDAO.adiciona(titulo, texto, data, id_assunto, id)
		return render_template("gerencia.html", vetNoticia = noticiaDAO.listar(), mensagem = "Nova noticia adicionada com sucesso!", id=id)
	except Exception as e:
#		# app.logger.error(str(e))
		return "deu erro no adicionar...."



@jornalista.route("/excluir_noticia/<int:noticia_id>")
def jornalista_excluir_noticia(noticia_id):
	noticiaDAO = NoticiaDAO()
	noticiaDAO.excluir(noticia_id)	
	jornalistaDAO = JornalistaDAO()
	login = str(session['login'])
	id = jornalistaDAO.obter_id(login)
	return render_template("gerencia.html", vetNoticia = noticiaDAO.listar(), mensagem = "Excluido", id=id)


@jornalista.route("/tela_editar_noticia/<int:noticia_id>", methods = ['GET'])
def jornalista_tela_editar_noticia(noticia_id):
	noticiaDAO = NoticiaDAO()
	noticia = Noticia()
	noticia = noticiaDAO.obter(noticia_id)
	assuntoDAO = AssuntoDAO()
	return render_template("adiciona_noticia.html" , url = "/jornalista/alterando_noticia/"+str(noticia.id), titulo = noticia.titulo, texto = noticia.texto, data=noticia.data,vetAssunto= assuntoDAO.listar() )

@jornalista.route("/alterando_noticia/<int:noticia_id>", methods=['POST'])
def jornalista_alterando_noticia(noticia_id):
	titulo = request.form['titulo']
	titulo = str(titulo)
	print titulo
	texto = request.form['texto']
	texto = str(texto)
#	print senha
	data = request.form['data']
	data = str(data)
	assunto = request.form['assunto']
	noticiaDAO = NoticiaDAO()
	id_assunto = noticiaDAO.id_assunto(assunto)
	print id_assunto
	noticia = Noticia()
	noticia.id = noticia_id
	noticia.titulo = titulo
	noticia.texto=texto
	noticia.data = data
	noticia.assunto = id_assunto
	print noticia
	noticiaDAO.alterar(noticia)
	jornalistaDAO = JornalistaDAO()
	login = str(session['login'])
	id = jornalistaDAO.obter_id(login)
	return render_template("gerencia.html", vetNoticia = noticiaDAO.listar(), mensagem = "Noticia alterada com sucesso!", id=id)

@jornalista.route("editar_perfil/<id>")
def jornalista_editar_perfil(id):
	login = str(session['login'])
	jornalistaDAO = JornalistaDAO()
	nome = jornalistaDAO.obter_nome(login)
	return render_template("tela_adicionar.html", url = "/jornalista/alterando_perfil/"+str(id), login = str(session['login']), senha = str(session['senha']), nome = nome)

@jornalista.route("alterando_perfil/<id>", methods=['POST'])
def jornalista_alterando_perfil(id):
	login = request.form['login']
	login = str(login)
#	print matricula
	senha = request.form['senha']
	senha = str(senha)
#	print senha
	nome = request.form['nome']
	nome = str(nome)
#	print nome

	jornalistaDAO = JornalistaDAO()
#	alunoDAO.apagafoto(app.config['UPLOAD_FOLDER'], "", matricula)
	jornalista = Jornalista()
	jornalista.id = str(id)
	jornalista.login = login
	jornalista.senha = senha
	jornalista.nome = nome
	
	id = str(id)
	jornalistaDAO.alterar(jornalista)
	jornalista = jornalistaDAO.obter(id)
	print jornalista
	return render_template("perfil.html", jornalista = jornalistaDAO.obter(id), perfil = "jornalista")

@jornalista.route("ver_perfil")
def jornalista_ver_perfil():
	jornalistaDAO = JornalistaDAO()
	login = str(session['login'])
	id = jornalistaDAO.obter_id(login)
	return render_template("perfil.html", jornalista = jornalistaDAO.obter(id), perfil ="jornalista")
	
@jornalista.route("/comentarios/<int:id>")
def jornalista_comentarios(id):
	id = str(id)
	comentarioDAO = ComentarioDAO()
	
	return render_template("comentarios.html", comentarios = comentarioDAO.listar_por_noticia(id), perfil = "jornalista")



@jornalista.route("/excluir_comentario/<int:id>")
def jornalista_excluir_comentario(id):
	id = str(id)
	comentarioDAO = ComentarioDAO()
	comentarioDAO.excluir(id)
	id_noticia = comentarioDAO.obter_id_noticia(id)	
	return render_template("comentarios.html", comentarios = comentarioDAO.listar_por_noticia(id_noticia), perfil = "jornalista", mensagem = "Excluido")
