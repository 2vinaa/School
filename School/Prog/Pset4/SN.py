from asyncio import current_task
from datetime import datetime
from LINKEDLISTADT import LinkedList, ListNode

class SocialNetwork:
    def __init__(self):
        self.user_list = LinkedList()

    def add_users(self, other):
            if self.user_list.search_linear(ListNode(other)) is None:
                self.user_list.append_constant(ListNode(other))
            else:
                print("This user is already in the SN")

    def __str__(self):
        if self.user_list.head is None:
            return "Empty"

        result = str(self.user_list.head.data)
        current = self.user_list.head.next

        # Traverse and append each element to the result string
        while current:
            result += "\n\n" + str(current.data)
            current = current.next

        return result

    def get_user(self, user: ListNode):
        if self.user_list.search_linear(user) is not None:
            return self.user_list.search_linear(user)
        else:
            return "The user isn't in the SN"

    def add_friendship(self, user1, user2):
        if self.user_list.search_linear(ListNode(user1)) is not None:
            if self.user_list.search_linear(ListNode(user2)) is not None:
                user1.add_friends(user2)

            else:
                return f"{user2} is not in SN"
        else:
            return f"{user1} is not in SN"


    def remove_friendship(self,user1, user2):
        if self.user_list.search_linear(ListNode(user1)) is not None:
            if self.user_list.search_linear(ListNode(user2)) is not None:
                user1.remove_users(user2)

            else:
                return f"{user2} is not in SN"
        else:
            return f"{user1} is not in SN"


    def mutual_friends(self, user1, user2):

        if self.user_list.search_linear(ListNode(user1)) is None:
            return f"{user1} is not in SN"
        if self.user_list.search_linear(ListNode(user2)) is None:
            return f"{user2} is not in SN"

        mutual = LinkedList()
        current1 = user1.friends.head
        while current1 is not None:
            if user2.friends.search_linear(current1) is not None:
                mutual.append_constant(current1)
            current1 = current1.next
        return f"The Common Friend(s) are {mutual}"


    def suggest_friends(self, user1, user2, user3):
        if self.user_list.search_linear(ListNode(user1)) is None:
            return f"{user1} is not in SN"
        if self.user_list.search_linear(ListNode(user2)) is None:
            return f"{user2} is not in SN"
        if self.user_list.search_linear(ListNode(user3)) is None:
            return f"{user3} is not in SN"


        suggested = LinkedList()
        mutual = LinkedList()
        current1 = user1.friends.head
        while current1 is not None:
            if user2.friends.search_linear(current1) is not None:
                mutual.append_constant(current1)
            current1 = current1.next

        currmut = mutual.head
        while currmut is not None:
            if user3.friends.search_linear(currmut) is None:
                if currmut.data != user3.username:
                    suggested.append_constant(ListNode(currmut))
            currmut = currmut.next
        return f"The suggested friend(s) are: {suggested}"

class User:
    def __init__(self,username, name, age):
        self.username = username
        self.name = name
        self.age = age
        self.registration_date = datetime.now()
        self.friends = LinkedList()

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def get_age(self):
        return self.age

    def date(self):
        return self.registration_date

    def __eq__(self, other):
        if self.username == other.username:
            return True
        else:
            return False


    def __str__(self):
        return  f"The name is {self.name}\nThe Age is {self.age}\nUsername is {self.username}\nThe Registration date is {self.registration_date}\nFriends = {self.friends}"


    def add_friends(self, friend_user):
        assert self != friend_user, "You cant add yourself"
        self.friends.append_constant(ListNode(friend_user.username))
        friend_user.friends.append_constant(ListNode(self.username))

    def get_friends(self):
        if self.friends.length == 1:
            return f"User: {self.friends} is in the friends list"
        elif self.friends.length == 0:
            return "There are no friends :c"
        else:
            return f"Users: {self.friends} are in the friends list"

    def remove_users(self, removed_user):
        try:
            self.friends.remove(removed_user.username)
            removed_user.friends.remove(self.username)
        except IndexError:
            print("This user isn't in your friends list")


if __name__ == "__main__":

        SN = SocialNetwork()


        User1 = User("Vinaa", "Federico", 19)
        User2 = User("LignanoSabbiador", "Emanuele", 20)
        User3 = User("LordLux", "Lorenzo", 20)
        User4 = User("AlfredoBonaventura", "Salvo", 23)
        User5 = User("Misma", "Luka", 23)


        SN.add_users(User1)
        SN.add_users(User2)
        SN.add_users(User4)
        SN.add_users(User5)
        SN.add_users(User3)



        print(SN.get_user(ListNode(User3)))
        SN.add_friendship(User1, User2)
        SN.add_friendship(User1, User5)
        SN.add_friendship(User2, User5)
        SN.add_friendship(User1, User4)
        SN.add_friendship(User4, User2)
        print(SN)
        print(SN.mutual_friends(User1, User2))
        print(SN.suggest_friends(User1,User2, User4))

