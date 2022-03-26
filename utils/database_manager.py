import mysql.connector as connection

class DatabaseManager:
    def __init__(self, host, database, user, passwd):
        self.connect = connection.connect(host=host,
                                database = database,
                                user=user,
                                passwd=passwd,
                                use_pure=True)
        self.cursor = self.connect.cursor()
    
    def insert(self, query: str, data: tuple):
        self.cursor(query, data)

    def read(self, query: str, data: tuple):
        result = {}
        if(len(data) == 0):
            result = self.cursor.execute(query, data)
        else:
            result = self.cursor.execute(query)
        
        print(f"Retornou {len(result)} resultados")

        return result