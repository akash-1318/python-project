from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

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