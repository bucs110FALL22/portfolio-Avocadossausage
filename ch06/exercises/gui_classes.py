class Enemy:
  def_init_(self):
    self.enemy_type = 3
    self.enemy_health = 100
    self.enemy_attack_damage = 50

class Ally:
  def_init_(self):
    self.ally_lives = 3
    self.ally_move = True
    self.ally_amount = 2

class PowerUp:
  def_init_(self):
    self.power_up_damage = 25
    self.power_up_speed = 25
    self.power_up_timeonscreen = 50