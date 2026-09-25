class Weed:
  weed_created = 0
  def __init__(self, strain, effect):
    self.strain = strain
    self.effect = effect
    Weed.weed_created += 1

weed_1 = Weed("HulkBerry", "Relaxing and puwerful")
weed_2 = Weed("Fat Banana", "Uplifting and energizing")
weed_3 = Weed("Sour Diesel", "Intense and focused")

print(f"The weed strain is {weed_1.strain} and this effects {weed_1.effect}")
print(f"The weed strain is {weed_2.strain} and this effects {weed_2.effect}")
print(f"The weed strain is {weed_3.strain} and this effects {weed_3.effect}")
print(f"Total weeds created: {Weed.weed_created}")