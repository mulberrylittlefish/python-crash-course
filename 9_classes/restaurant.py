class Restaurant():

    def __init__(self, name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
        self.numbers_served = 0
    
    def describe_restaurant(self):
        print('The name of the restaurant is: ' + self.restaurant_name.title())
        print('This place serves: ' + self.cuisine_type)
    
    def open_restaurant(self):
        print('The restaurant is now open!')
    
    def set_numbers_served(self, numbers):
        self.numbers_served = numbers
    
    def increment_number_served(self, number):
        self.numbers_served += number