import json
import os

from constants import DATA_DIR


class TodoList(list):
    number_of_lists = 0
    def __init__(self, name, items=[]):
        self.items = items
        self.name = name
        TodoList.number_of_lists += 1
        print("todo list created")
        super().__init__()
    
    def __str__(self):
      return f"TodoList({self.name})"
    def add(self, item):
      if not isinstance(item, str):
        raise TypeError("Item must be a string")
      if  item not in self.items:
        self.items.append(item)
        return True
      else:
        raise ValueError("Item already exists")
        
    def remove(self, item):
      if not isinstance(item, str):
        raise TypeError("Item must be a string")
      if item in self.items:
        self.items.remove(item)
        return True
      else:
        raise ValueError("Item does not exist")
        
    def show(self):
      print(f"Here it is my todo list {self.name} content")      
      for item in self.items:
        print(f"- {item}")
      return True
    def clear(self):
      self.items.clear()
      return True
    
    def save(self):
      my_path = os.path.join(DATA_DIR, f"{self.name}.json")
      if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
      with open(my_path, "w") as f:
        json.dump(self.items, f, indent=4)
      return True
    
    @staticmethod
    def show_numerical():
      print(f"It have {TodoList.number_of_lists} lists created !")
      return True
    
    @classmethod
    def high(cls):
      cls.number_of_lists += 1
      return cls("Cannabis}")
    
    @classmethod
    def tasks(cls):
      cls.number_of_lists += 1
      return cls("Tasks")
    
if __name__ == "__main__":
  get_high = TodoList("Cannabis")
  get_high.add("420")
  get_high.show()
  get_high.save()
  TodoList.show_numerical()

