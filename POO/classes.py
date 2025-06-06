from cgi import print_exception


class Drug:
  category = "Cocaine"
  price = 100
  weight = 10
  quantity = 1

  def __init__(self, category, price, weight, quantity):
    self.category = category
    self.price = price
    self.weight = weight
    self.quantity = quantity
print(Drug.category)