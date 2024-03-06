class CartePizzeriaException(Exception):
    def __init__(self, message="Erreur dans la carte pizzeria"):
        self.message = message
        super().__init__(self.message)
