import psycopg2
import json
from chatbot.utils import ChatbotError, handle_error

class PostgresDatabase:
    def __init__(self, db_credentials):
        self.db_credentials = db_credentials
        self.init_database()

    def init_database(self):
        try:
            self.conn = psycopg2.connect(**self.db_credentials)
        except psycopg2.Error as e:
            handle_error(e)
            raise ChatbotError("Failed to connect to the PostgreSQL database.")

        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                context TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_client(self, client_data):
        self.cur.execute("INSERT INTO clients (name, context) VALUES (%s, %s)", (client_data["name"], json.dumps(client_data["context"])))
        self.conn.commit()

    def load_clients(self):
        self.cur.execute("SELECT id, name, context FROM clients")
        clients = self.cur.fetchall()
        return {client[0]: {"name": client[1], "context": json.loads(client[2])} for client in clients}

    def load_client_context(self, client_id):
        clients = self.load_clients()
        return clients[client_id]["context"]

    def save_client_context(self, client_id, context):
        self.cur.execute("UPDATE clients SET context = %s WHERE id = %s", (json.dumps(context), client_id))
        self.conn.commit()

    def close(self):
        self.conn.close()