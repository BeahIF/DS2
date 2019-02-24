from modelo import * 
from flask import *
estagio = Blueprint('estagio', __name__,
                        template_folder='estagio/templates', static_folder = 'estagio/static')


@estagio.route("/listar_estagiarios")
def estagiaio_listar_estagios():
   # selecionando todos
   #vetUsuario = Usuario.query.all()
   # usando filtro
   vetEstagiario = Estagiario.query.all()
   print vetEstagiario
 #  resultado = ""
  # for i in range(0, len(vetUsuario)):
   #   resultado += vetUsuario[i].nome + "<br>"
   return render_template("ver_estagiarios.html", vetEstagiario=vetEstagiario)
   
   #return UsuarioIapereira.username


# rota inicial => index
@estagio.route("/excluir_estagiario/<id>")
def estagio_excluir_estagiario(id):
   # criando o objeto que pretendo adicionar
   #Usuario = Usuario("iapereira","igor.pereira@riogrande.ifrs.edu.br")
   # propondo que vou adicionar
   #db.session.add(Usuario)

   usuario = Estagiario.query.get(id)
   db.session.delete(usuario)
   # fechando a transacao
   db.session.commit()
   # mensagem de sucesso...da adicao => retornando o Usuario.Usuarioname
   return redirect("estagio/listar_estagiarios")
@estagio.route("/tela_editar_estagiario/<id>")
def estagio_tela_editar_estagiario(id):
   print "entrei"
   print id
   return render_template("tela_editar_estagiario.html", id=id)

@estagio.route("/editar_estagiario/<id>", methods=['POST'])
def estagio_editar_estagiario(id):
   
   login = request.form['login']
   senha=request.form['senha']
   nome =request.form['nome']
   estagiario = Estagiario(login, senha, nome)
   db.session.update(estagiario).where(es.id==id).values()
   db.session.commit()  
   return redirect("estagio/listar_estagiarios") 
@estagio.route("/add", methods=['POST'])
def estagio_add():

   login = request.form['login']
   senha=request.form['senha']
   nome =request.form['nome']
   estagiario = Estagiario(login, senha, nome)
   db.session.add(estagiario)
   db.session.commit()
   return redirect("/estagio/listar_estagiarios")
#@estagio.route("/apagar")



app.register_blueprint(estagio, url_prefix='/estagio')   