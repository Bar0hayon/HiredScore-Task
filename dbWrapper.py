import psycopg2

class DBWrapper:
    def __init__(self, dbname, user):
        self.db_connection = psycopg2.connect(dbname=dbname, user=user)
        self.db = self.db_connection.cursor()
    
    def get_candidates(self):
        query = f"SELECT title FROM candidates;"
        self.db.execute(query)
        query_res = self.db.fetchall()
        candidates_list = list(map(lambda candidate_tuple: candidate_tuple[0], query_res))
        return candidates_list