from flask import *
from modelo import * 
from persistencia import *
# declarando meu modulo
admin = Blueprint('admin', __name__,
                        template_folder='admin/templates', static_folder = 'admin/static')
#@admin.before_request
#def antes():	
	#admin.logger.debug(request.path)
#	if ( request.path == "/admin/" or request.path == "/admin/login"):
#		app.logger.debug("entrou aqui")			
#	elif ('login' not in session and 'senha' not in session):
#		app.logger.warning("entrou no segundo...")
#		return "erro...faca login corretamente"		

@admin.route("/tela_adicionar_estagiario")
def admin_tela_adicionar_estagiario():
	return render_template("tela_adicionar_estagiario.html")
@admin.route("/tela_inicial")
def admin_tela_inicial():
	print "rela"
	jornalistaDAO = JornalistaDAO()
	return render_template("admin.html", vetJornalista = jornalistaDAO.listar(), mensagem="")

@admin.route("/tela_adicionar")
def admin_tela_adicionar():
	return render_template("tela_adicionar.html", url = "/admin/adicionando", login = "", senha = "", nome = "")

@admin.route("/adicionando", methods=['POST'])
def admin_adicionando():
	login = request.form['login']
	senha = request.form['senha']
	nome = request.form['nome'] 
	jornalistaDAO = JornalistaDAO()
	jornalista = Jornalista(login, senha, nome)
	try:
		jornalistaDAO.adiciona(jornalista)
		return render_template("admin.html", vetJornalista = jornalistaDAO.listar(), mensagem = "Adicionado")
	except Exception as e:
		# app.logger.error(str(e))
		return "deu erro no adicionar...."

@admin.route("/excluir/<int:jornalista_id>")
def admin_excluir(jornalista_id):
	jornalistaDAO = JornalistaDAO()
	
	jornalistaDAO.excluir(jornalista_id)	
	return render_template("admin.html", mensagem = "Excluido")

@admin.route("/tela_editar/<int:jornalista_id>", methods = ['GET'])
def admin_tela_editar(jornalista_id):
	
	jornalistaDAO = JornalistaDAO()
	
	#jornalista = Jornalista()
	jornalista = jornalistaDAO.obter(jornalista_id)

	return render_template("tela_adicionar.html" , url = "/admin/alterando/"+str(jornalista.id), login = jornalista.login, senha = jornalista.senha, nome = jornalista.nome)

@admin.route("/alterando/<int:jornalista_id>", methods=['POST'])
def admin_alterando(jornalista_id):
	
	login = request.form['login']
	login = str(login)
#	print matricula
	senha = request.form['senha']
	senha = str(senha)
	print senha
	nome = request.form['nome']
	nome = str(nome)
	print nome

	jornalistaDAO = JornalistaDAO()
#	alunoDAO.apagafoto(app.config['UPLOAD_FOLDER'], "", matricula)
	jornalista = Jornalista()
	jornalista.login = login
	jornalista.senha = senha
	jornalista.nome = nome
	jornalista.id = jornalista_id

	jornalistaDAO.alterar(jornalista)

	return redirect("/admin/tela_inicial")
