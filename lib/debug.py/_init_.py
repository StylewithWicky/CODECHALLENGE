from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

# Create sample data
author = Author(name="Alice Smith")
author.save()

magazine = Magazine(name="Science Weekly", category="Science")
magazine.save()

author.add_article(magazine, "The Future of AI")

# Retrieve and display
print("Articles by Alice Smith:", author.articles())
print("Magazines contributed to:", author.magazines())
print("Topic areas:", author.topic_areas())
print("Top publisher:", Magazine.top_publisher().name if Magazine.top_publisher() else "None")