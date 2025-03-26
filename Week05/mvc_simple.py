from pydantic import BaseModel
from typing import Optional

# 🧠 Model
class UserModel(BaseModel):
    name: Optional[str] = None

    def greeting(self) -> str:
        return f"Hello, {self.name}!" if self.name else "Hello!"

# 👁️ View
class UserView:
    def get_input(self) -> str:
        return input("Enter your name: ")

    def show_output(self, message: str):
        print(message)

# 🧩 Controller
class UserController:
    def __init__(self):
        self.model = UserModel()
        self.view = UserView()

    def run(self):
        name = self.view.get_input()
        self.model.name = name
        self.view.show_output(self.model.greeting())

# 🚀 Entry point
if __name__ == "__main__":
    controller = UserController()
    controller.run()
