# Para a criação do banco de dados

import sqlite3

banco = sqlite3.connect('database.db')
banco.execute("PRAGMA foreign_keys=on")

cursor = banco.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Missao(
                id INTEGER PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                launch_date DATE NOT NULL,
                destination VARCHAR(255) NOT NULL,
                status VARCHAR(50) NOT NULL,
                tripulation VARCHAR(255) NOT NULL,
                util_charge VARCHAR(255) NOT NULL,
                duration INTERVAL NOT NULL,
                cost REAL NOT NULL,
                status_descr VARCHAR(255) NOT NULL
                );''')

cursor.execute('''SELECT * FROM Missao''');

banco.commit();

cursor.close()
banco.close()
