class Author:
    def __init__(self, n1, n2, coun, yearB, nick=None, yearD=None):
        self.name1, self.name2 = n1, n2
        self.yearB, self.yearD = yearB, yearD
        self.nick, self.country = nick, coun
        self.works = []

    def addWork(self, work):
        self.works.append(work)

class Work:
    def __init__(self, author, publisher, year):
        self.author, publisher, year = author, publisher, year
        self.otherAuthors = []

    def addAuthor(self, author):
        self.otherAuthors.append(author)

class Publisher:
    def __init__(self, n1, n2, country, yearB, yearD=None):
        self.name1, self.name2 = n1, n2
        self.yearB, self.yearD = yearB, yearD
        self.country = country
        self.publ_works = []

    def addPubl_work(self, work):
        self.publ_works.append(work)

class Book(Work):
    def __init__(self, author, publisher, year, binding_and_cover):
        super().__init__(author, publisher, year)
        self.binding_and_cover = binding_and_cover

class Journal(Work):
    def __init__(self, author, publisher, year, type_of_cover):
        super().__init__(author, publisher, year)
        self.type_of_cover = type_of_cover

class Publication(Work):
    def __init__(self, author, publisher, year, place):
        super().__init__(author, publisher, year)
        self.Place = place

Tolstoy = Author('Lev', 'Tolstoy', 'Russia', 1828, yearD=1910)
Katkov = Publisher('Michael', 'Katkov', 'Russia', 1818, yearD=1887)
War_and_peace = Work(Tolstoy, Katkov, 1863)
