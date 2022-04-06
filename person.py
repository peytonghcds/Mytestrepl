class Person:


  def eat(self,amount_to_eat):
    if self.current_food + amount_to_eat >= self.max_food:
      print("You're already stuffed!")
    else:
      self.current_food += amount_to_eat
      print("Yum, that's delicious!")
  
  def __init__(self,_name,_height,_hairColor,_eyeColor,_skinColor):
    self.name = _name
    self.height = _height
    self.hairColor = _hairColor
    self.eyeColor = _eyeColor
    self.skinColor = _skinColor
    self.num_eyes = 2
    self.num_fingers = 10
    self.num_toes = 10
    self.max_food = 25
    self.current_food = 8

  def run(self):
    if self.current_food == 0:
      print("You need to eat something before you run!")
    else:
      self.current_food -= 1
      print("run run run")