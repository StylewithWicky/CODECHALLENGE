import sqlite3
from lib.db.connection import get_connection


class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = value.strip()

    def save(self):
        """Save author to database or update existing one."""
        conn = get_connection()
        cursor = conn.cursor()

        try:
            if self.id is None:
                cursor.execute(
                    "INSERT INTO authors (name) VALUES (?)",
                    (self.name,)
                )
                self.id = cursor.lastrowid
            else:
                cursor.execute(
                    "UPDATE authors SET name = ? WHERE id = ?",
                    (self.name, self.id)
                )
            conn.commit()
        finally:
            conn.close()

    @classmethod
    def find_by_id(cls, id):
        """Find an author by their ID."""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, name FROM authors WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return cls(name=row['name'], id=row['id'])
        return None

    def articles(self):
        """Get all articles written by this author."""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    def magazines(self):
        """Get all unique magazines this author has contributed to."""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    def add_article(self, magazine, title):
        """Create a new article for this author in a specific magazine."""
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                (title, self.id, magazine.id)
            )
            conn.commit()
        finally:
            conn.close()

    def topic_areas(self):
        """Get unique categories of magazines this author has written for."""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT DISTINCT m.category FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()

        return [row['category'] for row in rows]

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"