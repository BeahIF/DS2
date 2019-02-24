require_relative("conexao.rb")
require_relative("quarto.rb")
class QuartoDAO
	def salvar(pes) 
	    p pes.id
	    if pes.id.nil?
	   
            query = 'INSERT INTO "quarto" ("quant_pessoas","dthratualizacao") VALUES ($1,$2)'
        else
            query = 'UPDATE "quarto" SET "quant_pessoas"=$2,"dthratualizacao"=$3 WHERE "id" = $1'
        end
		res = conecta{|con|
			con.exec_params(query, pes.to_a)
		}
	end
	def excluir(pes)
		if pes.id
			conecta{|con|
				con.exec_params('DELETE FROM "quarto" WHERE "id" = $1',[pes.id])
			}
		end
	end

	  def get(id)
        res = conecta{|con|
            con.exec_params('SELECT * FROM "quarto" WHERE id = $1', [id])
        }
        #p res[0]
    	Quarto.new res[0]
	end

	def listar
		v = []
	#	puts "oi"
		res = conecta{|con|
			con.exec_params('SELECT * FROM "quarto"')}
		res.each{|linha|
			v.push Quarto.new linha}
		#puts "po"
		tam = v.length
		
		cont = 0

		while cont <= tam
			puts v[cont].to_s
			cont = cont +1
		end 
		
	end

end