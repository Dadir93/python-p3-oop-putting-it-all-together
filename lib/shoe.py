#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = 'Used'

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'

class TestShoe:
    def has_brand_and_size(self):
        stan_smith = Shoe("Adidas", 9)
        assert stan_smith.brand == "Adidas"
        assert stan_smith.size == 9

    def requires_int_size(self):
        stan_smith = Shoe("Adidas", 9)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.size = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue().strip() == "size must be an integer"

    def can_cobble(self):
        stan_smith = Shoe("Adidas", 9)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.cobble()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue().strip() == "Your shoe is as good as new!"

    def cobble_makes_new(self):
        stan_smith = Shoe("Adidas", 9)
        stan_smith.cobble()
        assert stan_smith.condition == "New"