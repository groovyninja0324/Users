from flask_app.config.mysqlconnection import connectToMySQL

class User: 
    DB ="users"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    def full_name(self):
            results = f"{self.first_name} {self.last_name}"
            return results
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
            print(users)
        return users
    
    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def update(cls, data):
        query = """UPDATE users 
                SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s 
                WHERE id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def delete(cls, data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results