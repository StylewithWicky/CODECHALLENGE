from models.author import Author
from models.magazine import Magazine
from models.article import Article

def seed_data():
    # Clear existing data (optional)
    print("🗑️  Clearing old data...")

    # You could add DELETE statements if needed
    # But for simplicity, we'll assume fresh inserts each time

    print("🌱 Seeding data...")

    # Create Authors
    author1 = Author(name="Alice Smith")
    author2 = Author(name="Bob Johnson")
    author3 = Author(name="Charlie Davis")

    author1.save()
    author2.save()
    author3.save()

    # Create Magazines
    mag1 = Magazine(name="Tech Weekly", category="Technology")
    mag2 = Magazine(name="Fashion Monthly", category="Fashion")
    mag3 = Magazine(name="Science Journal", category="Science")

    mag1.save()
    mag2.save()
    mag3.save()

    # Create Articles
    Article(title="The Future of AI", author_id=author1.id, magazine_id=mag1.id).save()
    Article(title="Sustainable Fashion Trends", author_id=author2.id, magazine_id=mag2.id).save()
    Article(title="Quantum Computing Breakthroughs", author_id=author1.id, magazine_id=mag3.id).save()
    Article(title="How to Stay Fit", author_id=author3.id, magazine_id=mag2.id).save()
    Article(title="Advances in Robotics", author_id=author2.id, magazine_id=mag1.id).save()
    Article(title="AI Ethics", author_id=author1.id, magazine_id=mag1.id).save()
    Article(title="Climate Change Research", author_id=author3.id, magazine_id=mag3.id).save()

    print("✅ Database seeded successfully.")

if __name__ == "__main__":
    seed_data()