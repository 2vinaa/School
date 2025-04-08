class EmailSet:
    def __init__(self):
        self.set = []

    def add_emails(self, email):
        if self.contain(email) is False:
            self.set.append(email)
        else:
            return "This email cannot be added, as it is already inside the set"

    def contain(self, email):
        for i in range(len(self.set)):
            if self.set[i] == email:
                return True

        return False

    def remove(self, email):
        if self.contain(email)==True:
            self.set.remove(email)
            return "You have successfully removed the email"
        else:
            return "You cant remove something that isn't there"

    def intersect(self, other):
        email1 = []
        email2 = []
        intersectemail = []
        for i in range(len(self.set)):
            email1.append(self.set[i])


        for j in range(len(other.set)):
            email2.append(other.set[j])


        for i in email1:
            for j in email2:
                if i == j:
                    intersectemail.append(i)
                else:
                    pass


        return f"The emails which can be found in both are {intersectemail}"

    def __str__(self):
        return str(self.set)


if __name__ == "__main__":

    Newspaper = EmailSet()
    Newspaper.add_emails("f@gmail.com")
    Newspaper.add_emails("g@gmail.com")
    Newspaper.add_emails("h@gmail.com")
    Newspaper.add_emails("3@gmail.com")
    Newspaper.add_emails("1@gmail.com")

    FashionBook = EmailSet()
    FashionBook.add_emails("f@gmail.com")
    FashionBook.add_emails("1@gmail.com")
    FashionBook.add_emails("a@gmail.com")
    FashionBook.add_emails("b@gmail.com")
    FashionBook.add_emails("c@gmail.com")

    print(FashionBook.contain("1@gmail.com"))
    print(Newspaper.remove("3@gmail.com"))

    print(Newspaper.intersect(FashionBook))


