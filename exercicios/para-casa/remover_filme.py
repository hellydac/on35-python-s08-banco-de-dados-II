import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Remove o o filme com id 3
cursor.execute("DELETE FROM filmes WHERE id = ?", (3,))

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()