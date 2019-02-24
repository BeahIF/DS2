require_relative("conexao.rb")
require_relative("reserva.rb")
class ReservaDAO
	def salvar(pes) 
		if(pes.salva ==  true)
	    	if pes.id.nil?
	    		#puts pes.salva
	    		query = 'INSERT INTO "reserva" ("cliente","quarto", "entrada", "saida","valor", "quant_pessoas",  "dthratualizacao") VALUES ($1,$2, $3, $4, $5, $6, $7)'
    		else
            	query = 'UPDATE "reserva" SET  "cliente"=$2,"quarto"=$3, "entrada"=$4, "saida"=$5,"valor"=$6, "quant_pessoas"=$7, "dthratualizacao"=$8 WHERE "id" = $1' 
       		end
       		res = conecta{|con|
			con.exec_params(query, pes.to_a)
			}
       	else
       		puts "Nao pode fazer reserva em quarto pequeno"
       		#break
       	end
		
	end
	def excluir(pes)
		if pes.id
			conecta{|con|
				con.exec_params('DELETE FROM "reserva" WHERE "id" = $1',[pes.id])
			}
		end
	end

	  def get(id)
        res = conecta{|con|
            con.exec_params('SELECT * FROM "reserva" WHERE id = $1', [id])
        }
        #p res[0]
    	Reserva.new res[0]
	end

	def listar
		v = []
	#	puts "oi"
		res = conecta{|con|
			con.exec_params('SELECT * FROM "reserva"')}
		res.each{|linha|
		#	puts linha
			v.push Reserva.new linha}
	#	puts "po"
		tam = v.length
		cont = 0

		while cont <= tam
			puts v[cont].to_s
			#puts v[cont].quarto

			cont = cont +1
		end 
		
	end




end