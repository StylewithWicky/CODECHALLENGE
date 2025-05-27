from models.author import Author
from models.magazine import Magazine
from models.article import Article

def seed_data():
    
 

 
    author1 = Author(name="Alice Wangui")
    author2 = Author(name="Bob Mwangi")
    author3 = Author(name="Charlis Wangui")

    author1.save()
    author2.save()
    author3.save()

    
    mag1 = Magazine(name="Daily Nation", category="General")
    mag2 = Magazine(name="Fashion ", category="Fashion")
    mag3 = Magazine(name="Science ", category="Science")

    mag1.save()
    mag2.save()
    mag3.save()

    # Create Articles
    Article(title="WHY IS WICKY SO COOL", author_id=author1.id, magazine_id=mag1.id).save()
    Article(title="NIKUNAME!", author_id=author2.id, magazine_id=mag2.id).save()
    Article(title="NIKUBAYA MANZE", author_id=author1.id, magazine_id=mag3.id).save()
    Article(title="JOHNE NOMA", author_id=author3.id, magazine_id=mag2.id).save()
    Article(title="CHEKI HII KATHE", author_id=author2.id, magazine_id=mag1.id).save()
    Article(title="GENGE LA BUNDOOKS", author_id=author1.id, magazine_id=mag1.id).save()
    Article(title="ACHANA NA MIMMI", author_id=author3.id, magazine_id=mag3.id).save()

    print("Database seeded successfully.")

if __name__ == "__main__":
    seed_data()