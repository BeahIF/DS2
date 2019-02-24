require_relative("conexao.rb")
require_relative("cliente.rb")
class ClienteDAO
	def salvar(pes) 
	    if pes.id.nil?
	   
            query = 'INSERT INTO "cliente" ("nome","cpf", "dthratualizacao") VALUES ($1,$2, $3)'
        else
            query = 'UPDATE "cliente" SET "nome"=$2, "cpf"=$3, "dthratualizacao"=$4 WHERE "id" = $1'
        end
		res = conecta{|con|
			con.exec_params(query, pes.to_a)
		}
	end
	def excluir(pes)
		if pes.id
			conecta{|con|
				con.exec_params('DELETE FROM "cliente" WHERE "id" = $1', [pes.id])
			}
		end
	end

	  def get(id)
        res = conecta{|con|
            con.exec_params('SELECT * FROM "cliente" WHERE id = $1', [id])
        }
        #p res[0]
    	Cliente.new res[0]
	end

	def listar
		v = []
	#	puts "oi"
		res = conecta{|con|
			con.exec_params('SELECT * FROM "cliente"')}
		res.each{|linha|
			v.push Cliente.new linha}
	#	puts "po"
		tam = v.length -1
		cont = 0

		while cont < tam
			puts v[cont].to_s
			cont = cont +1
		end 
		
	end

end