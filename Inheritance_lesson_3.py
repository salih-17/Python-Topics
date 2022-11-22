#Inheritance let you ingerited method and attribute from onther object and used

"""
class MysubClass:
    pass
print (dir (MysubClass)) # to see all method that inheritaned form object class
"""

from datetime import datetime , date
class Customer:
    no_customer = []
    discount_percent = 0.1
    shpping_percent = 0.05
    def __init__ (self , name , dob , gender):
        self.name  = name 
        self.dob = dob
        self.gender = gender
        self.email = name + "@gmail.com"
        self.cart = []
        self.cart_total = 0
        Customer.no_customer.append (self)
     # instance method  
    def age (self):
        yob = datetime.strptime(self.dob, '%Y-%m-%d').year
        return (datetime.today().year - yob)
        
    # instance method
    def add_cart (self , product : dict):
        self.cart.append(product)
        
    # instance method        
    def calculate_total (self):
        for product in self.cart:
            self.cart_total = self.cart_total + product['price']
        return self.cart_total
    # instance method
    def discount (self):
        total_after_discount = self.cart_total * self.discount_percent 
        return total_after_discount


    def calculate_shipping (self):
        shipping = self.cart_total * self.shpping_percent
        return shipping

    def calculate_final_total (self):
        cart = self.calculate_total()
        print (f'Subtotal = {cart}')
        total_after_discount = cart - self.discount ()
        print (f'Total After discount = {total_after_discount}')
        shipping = self.calculate_shipping()
        print (f'shipping = {shipping}')
        total = total_after_discount  + shipping
        print (f'The total is {total}')

    # Class method
    @classmethod
    def set_discount_percent (cls , percent):
        cls.discount_percent = percent

    # Class method
    @classmethod
    def from_str_info (cls , str_info):
        name , dob , gender  = str_info.split (',')
        return cls (name , dob , gender)

    # Static method
    @staticmethod
    def is_discount_day (today):
        if today == date (2022 , 11 , 22):
            return True
        return False


class PrimeCustomer (Customer) : # This is inheritend of the actual class bu we change just one class method
    shpping_percent = 0


customer_1_string = 'A,1990,Femal'
customer_2_string = 'B,1993,male'



customer_1 = Customer.from_str_info (customer_1_string)
customer_2 = PrimeCustomer.from_str_info (customer_2_string)

customer_1.add_cart({'product':'watch' , 'price': 200})
customer_1.add_cart({'product':'TV' , 'price': 1200})

customer_2.add_cart({'product':'phone' , 'price':1500})
customer_2.add_cart({'product':'bag' , 'price':700})


print (customer_1.calculate_final_total())

print ('========='*10)
print (customer_2.calculate_final_total())
print ('========='*10)
help (PrimeCustomer) # To print beautiful things


# 10:37
