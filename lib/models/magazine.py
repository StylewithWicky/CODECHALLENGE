import sqlite3
from lib.db.connection import get_connection


class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = value.strip()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value.strip()

    def save(self):
        """Save magazine to database or update existing one."""
        conn = get_connection()
        cursor = conn.cursor()

        try:
            if self.id is None:
                cursor.execute(
                    "INSERT INTO magazines (name, category) VALUES (?, ?)",
                    (self.name, self.category)
                )
                self.id = cursor.lastrowid
            else:
                cursor.execute(
                    "UPDATE magazines SET name = ?, category = ? WHERE id = ?",
                    (self.name, self.category, self.id)
                )
            conn.commit()
        finally:
            conn.close()

    @classmethod
    def find_by_id(cls, id):
        """Find a magazine by its ID."""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category FROM magazines WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return cls(name=row[1], category=row[2], id=row[0])
        return None

    @classmethod
    def find_by_name(cls, name):
        """Find all magazines by name."""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category FROM magazines WHERE name = ?", (name,))
        rows = cursor.fetchall()
        conn.close()

        return [cls(id=row[0], name=row[1], category=row[2]) for row in rows]

    @classmethod
    def find_by_category(cls, category):
        """Find all magazines by category."""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category FROM magazines WHERE category = ?", (category,))
        rows = cursor.fetchall()
        conn.close()

        return [cls(id=row[0], name=row[1], category=row[2]) for row in rows]

    @classmethod
    def create_table(cls):
        """Create the magazines table if it doesn't exist."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS magazines (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    @classmethod
    def drop_table(cls):
        """Drop the magazines table if it exists."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS magazines")
        conn.commit()
        conn.close()

    def __repr__(self):
        return f"<Magazine(id={self.id}, name='{self.name}', category='{self.category}')>"
      
    
