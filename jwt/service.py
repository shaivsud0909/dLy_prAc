from fastapi import FastAPI
from schema import user
import uuid
import json
from jwt_handler import create_access_token
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi import Response, Request

def home():
    return {"message":"welcome to the flask runimg"}


def creating_user(user: user):
    # Read existing data
    try:
        with open("res.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    # Add new user
    data.append(user.dict())

    # Save updated data
    with open("res.json", "w") as f:
        json.dump(data, f, indent=2)

    return {"message": "success"}

def login(user: user):
    try:
        with open("res.json","r") as f:
            data = json.load(f)
    except:
        return {"error": "No users registered"}

    for stored_user in data:

        if stored_user["username"] == user.username and stored_user["password"] == user.password:

            token = create_access_token(user.username)

            response = RedirectResponse(url="/dashboard", status_code=302) # redirecting to dashbord
            response.set_cookie(key="access_token", value=token, httponly=True) #set seesion cookie
            return response

    return {"error": "Invalid credentials"}




def dashboard(request: Request):
    token = request.cookies.get("access_token")

    if not token:
        return RedirectResponse(url="/")

    return {
        "message": "Welcome to Dashboard",
        "status": "Logged in"
    }



def logout():
    response = RedirectResponse(url="/")
    response.delete_cookie("access_token")

    return response
