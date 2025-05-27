import sqlite3
from lib.db.connection import get_connection


class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Title must be a non-empty string.")
        self._title = value.strip()

    def save(self):
        """Save article to database or update existing one."""
        conn = get_connection()
        cursor = conn.cursor()

        try:
            if self.id is None:
                cursor.execute(
                    "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                    (self.title, self.author_id, self.magazine_id)
                )
                self.id = cursor.lastrowid
            else:
                cursor.execute(
                    "UPDATE articles SET title = ?, author_id = ?, magazine_id = ? WHERE id = ?",
                    (self.title, self.author_id, self.magazine_id, self.id)
                )
            conn.commit()
        finally:
            conn.close()

    @classmethod
    def find_by_id(cls, id):
        """Find an article by ID."""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return cls(
                id=row['id'],
                title=row['title'],
                author_id=row['author_id'],
                magazine_id=row['magazine_id']
            )
        return None

    @classmethod
    def find_by_title(cls, title):
        """Find all articles with a given title."""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE title = ?", (title,))
        rows = cursor.fetchall()
        conn.close()

        return [
            cls(
                id=row['id'],
                title=row['title'],
                author_id=row['author_id'],
                magazine_id=row['magazine_id']
            ) for row in rows
        ]

    @classmethod
    def find_by_author(cls, author_id):
        """Find all articles written by a specific author."""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE author_id = ?", (author_id,))
        rows = cursor.fetchall()
        conn.close()

        return [
            cls(
                id=row['id'],
                title=row['title'],
                author_id=row['author_id'],
                magazine_id=row['magazine_id']
            ) for row in rows
        ]

    @classmethod
    def find_by_magazine(cls, magazine_id):
        """Find all articles published in a specific magazine."""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE magazine_id = ?", (magazine_id,))
        rows = cursor.fetchall()
        conn.close()

        return [
            cls(
                id=row['id'],
                title=row['title'],
                author_id=row['author_id'],
                magazine_id=row['magazine_id']
            ) for row in rows
        ]

    def author(self):
        """Get the Author who wrote this article."""
        from .author import Author
        return Author.find_by_id(self.author_id)

    def magazine(self):
        """Get the Magazine where this article was published."""
        from .magazine import Magazine
        return Magazine.find_by_id(self.magazine_id)

    def __repr__(self):
        return f"<Article(id={self.id}, title='{self.title}', author_id={self.author_id}, magazine_id={self.magazine_id})>"
