import sqlite3


class OfflineService:

    def __init__(self):

        self.conn = sqlite3.connect("travel.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS saved_places (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            location TEXT,
            description TEXT,
            image TEXT
        )
        """)

        self.conn.commit()

    def save_place(self, name, location, description, image):

        self.cursor.execute(
            """
            INSERT INTO saved_places
            (name, location, description, image)
            VALUES (?, ?, ?, ?)
            """,
            (name, location, description, image)
        )

        self.conn.commit()

    def get_places(self):

        self.cursor.execute(
            "SELECT * FROM saved_places"
        )

        return self.cursor.fetchall()

    def delete_place(self, place_id):

        self.cursor.execute(
            "DELETE FROM saved_places WHERE id=?",
            (place_id,)
        )

        self.conn.commit()

    def close(self):
        self.conn.close()