import unittest
from unittest.mock import Mock

class TestCartePizzeria(unittest.TestCase):
  def setUp(self):
    self.carte_pizzeria = CartePizzeria()