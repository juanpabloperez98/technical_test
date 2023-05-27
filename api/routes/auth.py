from fastapi import APIRouter, Response, status
from pydantic import BaseModel
from jwt_functions import validate_token, write_token
from schemas.user import User, Login
from fastapi.responses import JSONResponse
from config.db import engine
from models.users import users
from werkzeug.security import generate_password_hash, check_password_hash

auth_routes = APIRouter()

@auth_routes.post("/register", status_code=status.HTTP_201_CREATED)
def create_user(data_user: User):
    with engine.connect() as conn:
        user = conn.execute(users.select().where(users.c.email == data_user.email)).first()
        if user:
            return Response(content="Email Already Exists", status_code=400)
        new_user = data_user.dict()
        new_user["password"] = generate_password_hash(data_user.password, "pbkdf2:sha256:30", 30)
        conn.execute(users.insert().values(new_user))
        return JSONResponse(content={
            "msg": "User Created Sucessfully"
        })

@auth_routes.post("/login", status_code=status.HTTP_200_OK)
def login(login: Login):
    with engine.connect() as conn:
        user = conn.execute(users.select().where(users.c.email == login.email)).first()
        if not user:
            return JSONResponse(content={
                "msg": "Email doesnt exits"
            }, status_code = 404)
        _check = check_password_hash(user.password, login.password)
        if not _check:
            return JSONResponse(content={
                "msg": "Invalid password"
            }, status_code = status.HTTP_400_BAD_REQUEST)
        token = write_token(login.dict())
        return JSONResponse(content={
            "token": token,
            "exp_days": 2
        })
        


