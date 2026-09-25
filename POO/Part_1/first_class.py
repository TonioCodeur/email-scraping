class Weed:
  strain = "HulkBerry"
  percentage_of_thc = 28.5
  percentage_of_cbd = 0.3
  effect = "Relaxing and puwerful"

print(f"The weed strain is {Weed.strain} and this effects {Weed.effect}")

# instancier une classe
my_weed = Weed()
print(f"The weed strain is {my_weed.strain} and this effects {my_weed.effect}")

weed_1 = Weed()
Weed.strain = "Fat Banana"
Weed.effect = "Uplifting and energizing"
weed_2 = Weed()
print(f"The weed strain is {weed_2.strain} and this effects {weed_2.effect}")
weed_2.strain = "Sour Diesel"
weed_2.effect = "Intense and focused"
print(f"The weed strain is {weed_2.strain} and this effects {weed_2.effect}")