from flask import *
from modelo import * 
from persistencia import *
leitor = Blueprint('leitor', __name__,
                      template_folder='leitor/templates', static_folder = 'leitor/static')

@leitor.route("/tela_inicial", methods=['GET','POST'])
def leitor_tela_inicial():
	print "leitor"
	login = session['login']
	print login
	senha = session['senha']
	print senha
	leitorDAO = LeitorDAO()
	session['perfil'] = "leitor"
	retorno = leitorDAO.testa(login, senha)
	print retorno
	if(retorno == True):
		noticiaDAO = NoticiaDAO()
		return render_template("index.html", vetNoticia = noticiaDAO.listar(), mensagem = "")
	else:
		return render_template("login.html",mensagem="Login ou senha incorreta")

#@leitor.route("/adicionar_novo")
#def leitor_adicionar_novo():
#	print "entra aqui please"
#	return render_template("adicionar_novo.html")
@leitor.route("/tela_adicionar")
def leitor_tela_adicionar():


	print "adicionar leitor"
	return render_template("tela_adicionar.html", url = "/leitor/cria_leitor", login = "", senha = "", nome = "")

@leitor.route("/cria_leitor", methods=['POST'])
def leitor_cria_leitor():
	print "here"
	login = request.form['login']
	login = str(login)
#	print login
	senha = request.form['senha']
	senha = str(senha)
	nome = request.form['nome']
	nome = str(nome)
	perfil = "leitor"	
#	print perfil
	session['login'] = login
	session['senha'] = senha
	session['perfil'] = perfil
	leitorDAO = LeitorDAO()
	leitor = Leitor(login, senha, nome)
	leitorDAO.adiciona(leitor)
	noticiaDAO = NoticiaDAO()
	return render_template("perfil.html", leitor = leitorDAO.obter_p(login), mensagem = "", perfil = perfil)

@leitor.route("/meu_perfil")
def leitor_meu_perfil():
	leitorDAO = LeitorDAO()
	perfil = "leitor"
	login = str(session['login'])
	return render_template("perfil.html", leitor = leitorDAO.obter_p(login), mensagem="", perfil=perfil)

@leitor.route("/adicionando_comentario/<id_leitor>/<id_noticia>", methods=['POST'])
def jornalista_adicionando_noticia(id_leitor, id_noticia):
	id_leitor = str(id_leitor)
	id_noticia = str(id_noticia)
	print "to no adicionando_comentario"
	print id_leitor
	print id_noticia
	texto = request.form['texto']
	data = str(request.form['data'])
	print texto
	print data
	#print assunto
	comentarioDAO = ComentarioDAO()
	comentario = Comentario(texto,data,id_leitor, id_noticia)
	#print comentario
	try:
		comentarioDAO.adiciona(comentario)
		print comentarioDAO.listar_por_noticia(id_noticia)
		print "to aqui"
		comentarios = comentarioDAO.listar_por_noticia(id_noticia)
		print comentarios
		return render_template("comentarios.html", comentarios = comentarios)
	except Exception as e:
#		# app.logger.error(str(e))
		return "deu erro no adicionar...."



@leitor.route("/excluir_comentario/<int:id>")
def leitor_excluir_comentario(id):
	id = str(id)
	comentarioDAO = ComentarioDAO()
	comentarioDAO.excluir(id)	
	return render_template("index.html",  mensagem = "Excluido")


@leitor.route("/tela_editar_comentario/<int:id>", methods = ['GET'])
def leitor_tela_editar_comentario(id):
	id = str(id)
	comentarioDAO = ComentarioDAO()
	comentario = Comentario()
	comentario = comentarioDAO.obter(id)
	return render_template("edita_comentario.html" , texto = comentario.texto, data=comentario.data)


@leitor.route("/editar_perfil/<id>")
def leitor_editar_perfil(id):
	login = str(session['login'])
	leitorDAO = LeitorDAO()

	nome = leitorDAO.obter_nome(login)
	return render_template("adicionar_novo.html", url = "/leitor/alterando_perfil/"+str(id), login = str(session['login']), senha = str(session['senha']), nome = nome)

@leitor.route("alterando_perfil/<id>", methods=['POST'])
def leitor_alterando_perfil(id):
	login = request.form['login']
	login = str(login)
#	print matricula
	senha = request.form['senha']
	senha = str(senha)
#	print senha
	nome = request.form['nome']
	nome = str(nome)
#	print nome

	leitorDAO = LeitorDAO()
#	alunoDAO.apagafoto(app.config['UPLOAD_FOLDER'], "", matricula)
	leitor = Leitor()
	leitor.id = str(id)
	leitor.login = login
	leitor.senha = senha
	leitor.nome = nome
	
	id = str(id)
	leitorDAO.alterar(leitor)
	leitor = leitorDAO.obter(id)
	
	return render_template("perfil.html", leitor = leitorDAO.obter(id), perfil = "leitor")



