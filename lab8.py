class ArchiveItem:

    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = year

    def __str__(self):
        return "( UID: " + str(self.uid) + ", Title: " + str(self.title) + ", Year: " + str(self.year) + ")"

    def __eq__(self, other):
        return self.uid == other.uid

    def is_recent(self,n):
        if (2025 - int(self.year)) <= int(n):
            return True

class Book(ArchiveItem):

    def __init__(self, uid, title, year, author, pages):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = pages

    def __str__(self):
        return "( UID: " + str(self.uid) + ", Title: " + str(self.title) + ", Year: " + str(
            self.year) + ", Author: " + str(self.author) + ", Pages: " + str(self.pages) + ")"

class Article(ArchiveItem):

    def __init__(self, uid, title, year, journal, doi):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi

    def __str__(self):
        return "( UID: " + str(self.uid) + ", Title: " + str(self.title) + ", Year: " + str(
            self.year) + ", Journal: " + str(self.journal) + ", DOI: " + str(self.doi) + ")"

class Podcast(ArchiveItem):

    def __init__(self, uid, title, year, host, duration):
        super().__init__(uid, title, year)
        self.host = host
        self.duration = duration

    def __str__(self):
        return "( UID: " + str(self.uid) + ", Title: " + str(self.title) + ", Year: " + str(
            self.year) + ", Host: " + str(self.host) + ", Duration: " + str(self.duration) + ")"


def save_to_file(items, filename):
    with open(filename, "w") as f:
        for item in items:
            item_type = item.__class__.__name__
            if item_type == "Book":
                f.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n")
            elif item_type == "Article":
                f.write(f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n")
            elif item_type == "Podcast":
                f.write(f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n")

def load_from_file(filename):
    items = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == "Book":
                items.append(Book(*parts[1:]))
            elif parts[0] == "Article":
                items.append(Article(*parts[1:]))
            elif parts[0] == "Podcast":
                items.append(Podcast(*parts[1:]))
    return items

book1 = Book(12345678, "Book 1", 2024, "John Glenn", 85)
book2 = Book(87654321, "My Book", 2018, "Jerry Thomas", 125)
article1 = Article(1223334444, "Best Study Ever", 2022, "Some Journal", 35232534252)
article2 = Article(97865432, "A Study On Computers", 2007, "PC Insider", 32732152444)
podcast1 = Podcast(215323253, "Podcast1", 2021, "Me", 12)
podcast2 = Podcast(2421421422, "FavouritePodcast",2014,"Brooke Jubal", 18)
archiveItems = [book1, book2, article1, article2, podcast1,podcast2]

save_to_file(archiveItems, "archive.txt")

archive = load_from_file("archive.txt")

for item in archive:
    print(item)

for item in archive:
    if item.is_recent(5):
        print(item)

for item in archive:
    if item.__class__.__name__ == "Article" and item.doi[0:8] == "10.1234":
        print(item)
