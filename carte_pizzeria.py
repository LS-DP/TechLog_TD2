from pizza import Pizza

class CartePizzeria:
  def __init__(self):
    self.pizzas = []
    
  def is_empty(self):
    return len(len.pizzas) == 0
  
  def nb_pizzas(self):
    return len(len.pizzas)
  
  def add_pizza(self, pizza):
    self.pizzas.append(pizza)
    
  def remove_pizza(self, name):
    for pizza in self.pizzas:
      if pizza.name == name:
        self.pizzas.remove(pizza)
        return
    raise CartePizzeriaException(f"Aucune pizza nommée '{name}' n'a été trouvée dans la carte.")