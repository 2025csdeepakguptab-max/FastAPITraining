from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
@app.get("/users")
def read_users():
    return [{"name": "Alice"}, {"name": "Bob"}]
@app.post("/users")
def create_user(user: dict):
    return {"message": "User created", "user": user}

