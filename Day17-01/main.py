# class User:
#     pass
#
#
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Jazz"
#
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Sham"
#
# # Above is a ballache need to look at constructing an object and initialising it.
#
# print(user_1)
# print(user_1.username)
#
# user_1.username = "Sham"
# print(user_1.username)

class User():
    def __init__(self, userid, username):
        self.id = userid
        self.username = username
        self.followers = 0
        self.following = 0

    def output_user(self):
        print(f"The User id is {self.id}")
        print(f"The Username is {self.username}")
        print(f"The User followers number are {self.followers}")
        print(f"The User is themselves following {self.following}")

    def follow(self, user):
        # The user parameter above is another use that you are following they go up by one
        user.followers += 1
        # As the user itself (self)! is following that user the self account following value does up by 1
        self.following += 1


user1 = User("001", "Jazz")
user2 = User("002", "Shamim")
user1.output_user()
user2.output_user()
print("Sham is going to follow Jazz")
user2.follow(user1)
print(f"User 1 details {user1.output_user()}")
print(f"User 2 details {user2.output_user()}")