import json


with open('data.json') as f:
    data = json.load(f)


class ParentForUser:
    def about(self):
        print(f"Name {self.name}")


print(data)
User = type("User", (ParentForUser,), data)
NewUser = User()



