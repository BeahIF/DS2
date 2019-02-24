require 'pg'

def conecta 
	conf = {dbname: "banco", user: "bea", password: "123", host: "localhost", port: "5432" }


	begin
		c = PG.connect conf
		yield c

	rescue PG::Error => e
		puts "treta"
		puts e.message
		raise e
	ensure
		c.close if c
	end
end


