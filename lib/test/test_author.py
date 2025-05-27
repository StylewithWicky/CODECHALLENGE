import os
import pytest
from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

# Run before each test
@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Recreate DB schema before each test
    conn = get_connection()
    conn.executescript(open("lib/db/schema.sql").read())
    conn.commit()
    conn.close()
    yield
    # Teardown logic (optional)


def test_author_can_be_created_and_saved():
    author = Author(name="Jane Austen")
    author.save()
    assert author.id is not None

def test_author_can_find_by_id():
    author = Author(name="George Orwell")
    author.save()

    found = Author.find_by_id(author.id)
    assert found.name == "George Orwell"
    assert found.id == author.id

def test_author_can_add_article_and_get_magazines():
    author = Author("Mark Twain")
    author.save()

    magazine = Magazine("Literary Weekly", "Fiction")
    magazine.save()

    article = author.add_article(magazine, "The Adventures of Huck")
    assert article.title == "The Adventures of Huck"
    assert article.author.id == author.id
    assert article.magazine.id == magazine.id

    magazines = author.magazines()
    assert len(magazines) == 1
    assert magazines[0]["name"] == "Literary Weekly"
