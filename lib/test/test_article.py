from models.magazine import Magazine

# Create table
Magazine.create_table()

# Create and save a new magazine
mag = Magazine(name="Tech Weekly", category="Technology")
mag.save()

# Find by ID
found = Magazine.find_by_id(mag.id)
print(found)

# Update and save again
mag.category = "Science & Tech"
mag.save()

# Search by name
results = Magazine.find_by_name("Tech Weekly")
print(results)