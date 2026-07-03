from db.crud import get_categories, get_books
from db.db import SessionLocal


def main():
    with SessionLocal() as session:
        categories = get_categories(session)

        print("Категории и книги из PostgreSQL:")
        for category in categories:
            print(f"\nКатегория: {category.title}")
            for book in category.books:
                print(f"- {book.title}: {book.price} руб.")
                print(f"  {book.description}")

        print("\nВсе книги:")
        for book in get_books(session):
            print(f"{book.id}. {book.title} ({book.category.title})")


if __name__ == "__main__":
    main()
