from datetime import datetime
from LinkedList import LinkedList, ListNode


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


    def mutual_friends(self,user1, user2):
        if self.user_list.search_linear(ListNode(user1)) is not None:
            if self.user_list.search_linear(ListNode(user2)) is not None:
                

            else:
                return f"{user2} is not in SN"
        else:
            return f"{user1} is not in SN"





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

    User1 = User("Vinaa", "Federico", 19)
    User2 = User("LignanoSabbiador", "Emanuele", 20)
    User3 = User("LordLux", "Lorenzo", 20)

    SN = SocialNetwork()
    SN.add_users(User1)
    SN.add_users(User2)


    print(SN.get_user(ListNode(User3)))
    SN.add_friendship(User1, User2)
    print(SN)
