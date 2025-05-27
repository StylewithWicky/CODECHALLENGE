# CODECHALLENGE
# 📝 Articles Code Challenge – Author, Article, Magazine Relationship (Phase 3)

This project is a Python-based object-relational system modeling the relationship between **Authors**, **Articles**, and **Magazines**, with **SQL database integration** (using raw SQL, no ORM frameworks like SQLAlchemy).

## 📚 Domain Overview

- **Author** can write many **Articles**
- **Magazine** can publish many **Articles**
- **Article** belongs to **one Author** and **one Magazine**
- Thus, the relationship between **Author** and **Magazine** is **many-to-many**, via **Articles**

---

## 🗂️ Project Structure

