from lib.db.connection import get_connection

class Article:
    def __init__(self, title, author, magazine, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.magazine = magazine

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
            (self.title, self.author.id, self.magazine.id)
        )
        self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        return cursor.fetchone()
