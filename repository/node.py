from sqlalchemy.orm import Session
from .userService import UserService

result = UserService.register("Diego", "Pineda", "zentoo31", "zentoo31@gmail.com", "gamemode31")
print(result)
login = UserService.login("zentoo31@gmail.com", "gamemode31")
print(login)
