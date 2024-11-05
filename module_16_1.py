from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome():
    return "Главная страница"


@app.get("/user/admin")
async def admin():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def paginator(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def news(username: str = 'admin', age: int = 99):
    return f'Информация о пользователе. Имя: {username}. Возраст: {age}'
