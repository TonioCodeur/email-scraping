class Weed:
  weeds_created = 0
  def __init__(self, strain, percent_thc, effects):
    self.strain = strain
    self.percent_thc = percent_thc
    self.effects = effects
    Weed.weeds_created += 1
  
  def __str__(self):
    return f"Strain: {self.strain}, Percent THC: {self.percent_thc}, Effects: {self.effects}"
  
  @classmethod
  def HulkBerry(cls):
    return cls("HulkBerry", "28% THC", ["Energizing", "Relaxing", "Happy"])

  @classmethod
  def LemonSkunk(cls):
    return cls("LemonSkunk", "20% THC", ["Relaxing", "Happy", "Creative"])

  @classmethod
  def PurpleHaze(cls):
    return cls("PurpleHaze", "22% THC", ["Relaxing", "Creative", "Energizing"])

  @classmethod
  def WhiteRuntz(cls):
    return cls("WhiteRuntz", "23% THC", ["Relaxing", "Happy", "Creative"])

  @staticmethod
  def get_weed_count():
    return print(f"Total weeds created: {Weed.weeds_created}")
  
hulkberry = Weed.HulkBerry()
print(hulkberry.strain)
print(hulkberry.percent_thc)
print(hulkberry.effects)

lemon_skunk = Weed.LemonSkunk()
print(lemon_skunk.strain)
print(lemon_skunk.percent_thc)
print(lemon_skunk.effects)

purple_haze = Weed.PurpleHaze()
print(purple_haze.strain)
print(purple_haze.percent_thc)
print(purple_haze.effects)

white_runtz = Weed.WhiteRuntz()
print(white_runtz.strain)
print(white_runtz.percent_thc)
print(white_runtz.effects)

print(hulkberry)
print(lemon_skunk)
print(purple_haze)
print(white_runtz)

Weed.get_weed_count()