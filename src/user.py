import json

from sanic_jwt import exceptions


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    async def get(username=""):
        with open("users.json") as json_file:
            users: [] = json.load(json_file)
        user = next((u for u in users if u["username"] == username), None)
        if user is None:
            raise exceptions.AuthenticationFailed("User not found.")
        return User(user["username"], user["password"])

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password
        }
