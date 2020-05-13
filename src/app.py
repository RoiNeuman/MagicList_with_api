import json

from sanic import Sanic, response
from sanic_jwt import Initialize, protected, exceptions

from src.user import User


async def authenticate(request, *args, **kwargs):
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    try:
        user = await User.get(username=username)
    except exceptions.AuthenticationFailed:
        raise exceptions.AuthenticationFailed("User not found.")

    if password != user.password:
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return user

app = Sanic("app")
Initialize(app, authenticate=authenticate)


@app.post("/")
@protected()
async def root(request):
    body = json.loads(request.body.decode("utf-8"))
    res = {item["name"]: item[next((key for key in item.keys() if "val" in key.lower()), None)] for item in body}

    return response.json(res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
