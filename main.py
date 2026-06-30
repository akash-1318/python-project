from fastapi import FastAPI, status, HTTPException, Request, Depends, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import sqlite3

app = FastAPI()

@app.get('/')
def home_page():
    return {'message': 'Welcome to fastapi'}

# Path parameters
# @app.get("/users/{user_id}")
# def get_users(user_id:int):
#     return {"id": user_id}

# Query parameters
# @app.get("/users")
# def get_users(user_id:int = None, name:str = None):
#     return {"id": user_id, "name": name}

# @app.post('/create_user')
# def create_user(name:str, age:int):
#     return {
#         "name": name,
#         "age": age
#     }

# Pydantic validation
# class Address(BaseModel):
#     pincode: int
#     city: str

# class User(BaseModel):
#     name: str
#     age: int
#     address: Address

# @app.post('/create_user')
# def create_user(user:User):
#     return {
#         "message": "User created",
#         "user": user
#     }


# CRUD - 

# users = []

# class User(BaseModel):
#     name: str
#     age: int
    
# @app.post("/users")
# def create_user(user: User):
#     users.append(user)
#     return {"message": "User created", "user": user}

# @app.get("/users")
# def get_all_users():
#     return users

# @app.get("/users/{user_id}")
# def get_single_user(user_id: int):
#     if user_id < len(users):
#         return users[user_id]
#     return {"message": "User not found"}

# @app.put("/users/{user_id}")
# def update_user(user_id: int, updated_user: User):
#     if user_id < len(users):
#         users[user_id] = updated_user
#         return {"message": "User updated", "user": updated_user}
#     return {"message": "User not found"}

# @app.delete("/users/{user_id}")
# def delete_user(user_id: int):
#     if user_id < len(users):
#         deleted_user = users.pop(user_id)
#         return {"message": "User deleted", "user": deleted_user}
#     return {"message": "User not found"}



# Response model - 


# users = []

# class User(BaseModel):
#     name: str
#     age: int
#     password:str

# class UserResponse(BaseModel):
#     name: str
#     age: int

# @app.get('/create-user', response_model=UserResponse)
# def create_user(user: User):
#     users.append(user)
#     return {'message': 'User created', 'user': user}



# Error Handling

# @app.post("/user", status_code=status.HTTP_201_CREATED)
# def create_user():
#     return {
#         "message": "user created"
#     }

# @app.get("/user")
# def get_user():
#     return {
#         "status":"Success",
#         "message":"User Fetched",
#         "data":{
#             "name":"Akash",
#             "age":22
#         }
#     }

# @app.get("/user/{user_id}")
# def get_user(user_id:int):
#     if user_id != 1:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail={"message": "User not found"}
#         )
#     return {
#         "status":"Success",
#         "message":"User Fetched",
#         "data":{
#             "name":"Akash",
#             "age":22
#         }
#     }
    

# Advanced exception - 

# If UserNotFoundException occurs run this handler
# class UserNotFoundException(Exception):
#     def __init__(self, name):
#         self.name = name
        
# @app.exception_handler(UserNotFoundException)
# def user_not_found_handler(request: Request, exc: UserNotFoundException):
#     return JSONResponse(
#         status_code=status.HTTP_404_NOT_FOUND,
#         content={"message": f"User {exc.name} not found"}
#     )


# @app.get("/user/{user_id}")
# def get_user(user_id: int):
#     if user_id != 1:
#         raise UserNotFoundException(user_id)
#     return {
#         "message": "User found",
#         "data": {
#             "id": user_id,
#             "name": "Akash",
#             "age": 22
#         }
#     }


# Depency Injection

# def get_current_user():
#     return {
#         "user": "Akash"
#     }


# @app.get('/home')
# def home_page(user = Depends(get_current_user)):
#     return {
#         "message": "Welcome to fastapi",
#         "user": user
#     }

# @app.get("/dashboard")
# def dashboard(user = Depends(get_current_user)):
#     return {
#         "message": "Welcome to dashboard",
#         "user": user
#     } 

# Depency Injection

# def varify_token(token: str = Header(None)):
#     if token != "akashtoken":
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail={"message": "Invalid token"}
#         )
#     return {
#         "message": "Welcome to fastapi",
#         "token": token
#     }

# @app.get('/home')
# def home_page(token = Depends(varify_token)):
#     return {
#         "message": "Welcome to fastapi",
#         "token": token
#     }
    

# Middleware - 
# It will run for every http request - for performance tracking,api monitoring you can use middleware.

@app.middleware('http')
async def my_middleware(request: Request, call_next):
    print("Middleware started")
    response = await call_next(request)
    print("Middleware ended")
    response.headers["X-Custom-Header"] = "My Custom Value"
    return response
