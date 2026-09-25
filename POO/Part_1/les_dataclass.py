from dataclasses import dataclass
from typing import ClassVar


@dataclass
class User:
  pseudo: str
  email: str
  password: str
  # ici age est aussi une classe variable car il est défini dans la classe User et non dans l'instance user_1 ou user_2
  age: ClassVar[int]

  def __post_init__(self):
    self.id = f"{self.email} {self.password}"

user_1 = User("John Doe", "john.doe@example.com", "password123")
print(repr(user_1))
user_2 = User("Mark Zuckerberg", "mark.zuckerberg@example.com", "password456")
print(repr(user_2))
print(user_1.__dict__)
print(user_2.id)