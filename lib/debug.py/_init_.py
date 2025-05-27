from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article


author = Author(name="JOHN KAMAU")
author.save()

magazine = Magazine(name="ONYI TULIA !", category="JOHNTE")
magazine.save()

author.add_article(magazine, "UNAANGALIA!")


print("ARTICLE:", author.articles())
print("MAGAZINE:", author.magazines())
print("TOPIC:", author.topic_areas())
print("PUBLISH ULE MNONA:", Magazine.top_publisher().name if Magazine.top_publisher() else "None")
