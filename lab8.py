from datetime import datetime
class ArchiveItem:
    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = int(year)

    def __str__(self):
        return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}"

    def __eq__(self, other):
        return self.uid == other.uid

    def is_recent(self, n):
        return self.year >= (2025 - n)

class Book(ArchiveItem):
    def __init__(self, uid, title, year, author, pages):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = int(pages)

    def __str__(self):
        return f"Book -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Author: {self.author}, Pages: {self.pages}"

class Article(ArchiveItem):
    def __init__(self, uid, title, year, journal, doi):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi

    def __str__(self):
        return f"Article -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Journal: {self.journal}, DOI: {self.doi}"

class Podcast(ArchiveItem):
    def __init__(self, uid, title, year, host, duration):
        super().__init__(uid, title, year)
        self.host = host
        self.duration = int(duration)

    def __str__(self):
        return f"Podcast -> UID: {self.uid}, Title: {self.title}, Year: {self.year}, Host: {self.host}, Duration: {self.duration} mins"

def save_to_file(items, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in items:
            if isinstance(item, Book):
                file.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n")
            elif isinstance(item, Article):
                file.write(f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n")
            elif isinstance(item, Podcast):
                file.write(f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n")


def load_from_file(filename):
    items = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            type_ = parts[0]
            if type_ == "Book":
                items.append(Book(*parts[1:]))
            elif type_ == "Article":
                items.append(Article(*parts[1:]))
            elif type_ == "Podcast":
                items.append(Podcast(*parts[1:]))
    return items

if __name__ == "__main__":
    items = [
        Book("B001", "Uğultulu Tepeler", 1847, "Emily Brönte", 775),
        Book("B002", "Kendine ait bir Oda", 1929, "Virginia Woolf", 464),
        Article("A101", "Quantum Computing", 2022, "Nature", "10.1234/qc567"),
        Article("A102", "Neural Interfaces", 2020, "Science", "10.5678/ni891"),
        Podcast("P301", "TechTalk AI", 2023, "Jane Doe", 45),
        Podcast("P302", "MindCast", 2017, "John Smith", 60)
    ]

    save_to_file(items, "archive.txt")

    loaded_items = load_from_file("archive.txt")

    print("All Items:")
    for item in loaded_items:
        print(item)

    print("\nRecent Items (last 5 years):")
    for item in loaded_items:
        if item.is_recent(5):
            print(item)

    print("\nArticles with DOI starting '10.1234':")
    for item in loaded_items:
        if isinstance(item, Article) and item.doi.startswith("10.1234"):
            print(item)
