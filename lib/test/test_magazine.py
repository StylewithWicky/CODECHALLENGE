import pytest
from models.magazine import Magazine
from models.author import Author
from models.article import Article

# Setup database before each test
@pytest.fixture(autouse=True)
def setup_database():
    from lib.db.connection import get_connection
    with open("lib/db/schema.sql", "r") as f:
        schema_sql = f.read()
    conn = get_connection()
    conn.executescript(schema_sql)
    conn.close()

# Test 1: Magazine can be created and saved
def test_magazine_can_be_created_and_saved():
    mag = Magazine(name="Tech Weekly", category="Technology")
    mag.save()
    assert mag.id is not None

# Test 2: Find magazine by ID
def test_find_by_id_returns_correct_magazine():
    mag = Magazine(name="Fashion Monthly", category="Fashion")
    mag.save()
    found = Magazine.find_by_id(mag.id)
    assert found is not None
    assert found.name == "Fashion Monthly"
    assert found.category == "Fashion"

# Test 3: Update magazine name and category
def test_update_magazine_details():
    mag = Magazine(name="Old Name", category="Old Category")
    mag.save()
    mag.name = "New Name"
    mag.category = "New Category"
    mag.save()

    updated = Magazine.find_by_id(mag.id)
    assert updated.name == "New Name"
    assert updated.category == "New Category"

# Test 4: Find magazines by name
def test_find_by_name_returns_matching_magazines():
    Magazine(name="Science Today", category="Science").save()
    Magazine(name="Science Today", category="Research").save()

    results = Magazine.find_by_name("Science Today")
    assert len(results) == 2

# Test 5: Find magazines by category
def test_find_by_category_returns_matching_magazines():
    Magazine(name="Sports Weekly", category="Sports").save()
    Magazine(name="Fitness Guide", category="Sports").save()
    Magazine(name="Tech Review", category="Technology").save()

    results = Magazine.find_by_category("Sports")
    assert len(results) == 2

# Test 6: Get all articles published in this magazine
def test_articles_method_returns_all_articles_in_magazine():
    mag = Magazine(name="Traveler's Journal", category="Travel")
    mag.save()

    author = Author(name="Samantha Lee")
    author.save()

    Article(title="Top Destinations", author_id=author.id, magazine_id=mag.id).save()
    Article(title="Budget Travel Tips", author_id=author.id, magazine_id=mag.id).save()

    articles = mag.articles()
    assert len(articles) == 2

# Test 7: Get all unique authors who contributed to the magazine
def test_contributors_method_returns_unique_authors():
    mag = Magazine(name="Health & Wellness", category="Health")
    mag.save()

    author1 = Author(name="Dr. Alice Chen")
    author1.save()

    author2 = Author(name="John Doe")
    author2.save()

    Article(title="Healthy Living", author_id=author1.id, magazine_id=mag.id).save()
    Article(title="Mental Health", author_id=author2.id, magazine_id=mag.id).save()
    Article(title="Nutrition Basics", author_id=author1.id, magazine_id=mag.id).save()

    contributors = mag.contributors()
    assert len(contributors) == 2

# Test 8: Get titles of all articles in the magazine
def test_article_titles_method_returns_list_of_titles():
    mag = Magazine(name="Foodie Digest", category="Food")
    mag.save()

    author = Author(name="Chef Maria")
    author.save()

    Article(title="Pasta Recipes", author_id=author.id, magazine_id=mag.id).save()
    Article(title="Healthy Smoothies", author_id=author.id, magazine_id=mag.id).save()

    titles = mag.article_titles()
    assert "Pasta Recipes" in titles
    assert "Healthy Smoothies" in titles

# Test 9: Get authors who have written more than one article for this magazine
def test_contributing_authors_method_returns_authors_with_more_than_one_article():
    mag = Magazine(name="Tech Innovations", category="Technology")
    mag.save()

    author1 = Author(name="Tom Smith")
    author1.save()

    author2 = Author(name="Emma Davis")
    author2.save()

    Article(title="AI Trends", author_id=author1.id, magazine_id=mag.id).save()
    Article(title="Machine Learning", author_id=author1.id, magazine_id=mag.id).save()
    Article(title="Data Science Tools", author_id=author2.id, magazine_id=mag.id).save()

    contributing_authors = mag.contributing_authors()
    assert len(contributing_authors) == 1
    assert contributing_authors[0]['name'] == "Tom Smith"

# Test 10: Top publisher returns magazine with most articles
def test_top_publisher_returns_magazine_with_most_articles():
    # Create multiple magazines
    mag1 = Magazine(name="Gaming Central", category="Gaming")
    mag1.save()

    mag2 = Magazine(name="Movie Reviews", category="Entertainment")
    mag2.save()

    # Create an author
    author = Author(name="David Kim")
    author.save()

    # Add several articles
    Article(title="Game Design Tips", author_id=author.id, magazine_id=mag1.id).save()
    Article(title="Best Games of 2024", author_id=author.id, magazine_id=mag1.id).save()
    Article(title="Streaming Platforms", author_id=author.id, magazine_id=mag2.id).save()

    top_mag = Magazine.top_publisher()
    assert top_mag.id == mag1.id
    assert top_mag.name == "Gaming Central"