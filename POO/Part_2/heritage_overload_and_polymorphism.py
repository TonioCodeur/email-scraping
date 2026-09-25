projects = ["pr_delete", "pr_admin", "view_projects"]
class User:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def __str__(self):
    return f"User: {self.first_name} {self.last_name}"

  def show_projets(self):
    for project in projects:
      print(project)

class Junior(User):
  def __init__(self, first_name, last_name):
    # User.__init__(self, first_name, last_name) ou
    super().__init__(first_name, last_name)

  def show_projets(self):
    for project in projects:
      if not project.startswith("pr_"):
        print(project)
  
ali = Junior("Ali", "Mentation")
ali.show_projets()

class Vehicule:
  def run(self):
    print("The engine is starting")

class Car(Vehicule):
  def run(self):
    super().run()
    print("The car is running")

class Plane(Vehicule):
  def run(self):
    super().run()
    print("The plane is flying")

car = Car()
plane = Plane()

car.run()
plane.run()