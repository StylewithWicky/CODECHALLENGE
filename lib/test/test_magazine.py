import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import os
import pytest
from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Recreate DB schema before each test
    conn = get_connection()
    conn.executescript(open("lib/db/schema.sql").read())
    conn.commit()
    conn.close()
    yield

def test_magazine_can_be_created_and_saved():
    mag = Magazine("Science World", "Science")
    mag.save()
    assert mag.id is not None

def test_magazine_can_get_articles():
    author = Author("Carl Sagan")
    author.save()

    mag = Magazine("Cosmos", "Space")
    mag.save()

    author.add_article(mag, "The Pale Blue Dot")
    articles = mag.articles()

    assert len(articles) == 1
    assert articles[0]["title"] == "The Pale Blue Dot"

def test_magazine_can_get_contributors():
    a1 = Author("Author One")
    a1.save()
    a2 = Author("Author Two")
    a2.save()

    mag = Magazine("Writers Monthly", "Writing")
    mag.save()

    a1.add_article(mag, "Writing Tips")
    a2.add_article(mag, "More Writing Tips")

    contributors = mag.contributors()
    contributor_names = [row["name"] for row in contributors]

    assert len(contributors) == 2
    assert "Author One" in contributor_names
    assert "Author Two" in contributor_names
