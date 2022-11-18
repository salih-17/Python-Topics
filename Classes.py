
from datetime import datetime

class Customer:
    
    dicount_price = 0.1
    
    def __init__ (self , name , dob , gender):
        self.name  = name 
        self.dob = dob
        self.gender = gender
        self.email = name + "@gmail.com"
        self.cart = []
        self.cart_total = 0
        
    def age (self):
        yob = datetime.strptime(self.dob, '%Y-%m-%d').year
        return (datetime.today().year - yob)
        
    
    def add_cart (self , product : dict):
        self.cart.append(product)
        
        
    def calculate_total (self):
        for product in self.cart:
            self.cart_total = self.cart_total + product['price']
        return self.cart_total

    def discount (self):
        total_after_discount = self.cart_total * self.dicount_price 
        return total_after_discount


customer_1 = Customer( 'A', '1990-01-01', 'Male')
customer_2 = Customer( 'B', '1992-01-01', 'Female')

#print ( customer_1.__dict__)
#print (customer_2.age())
#print (Customer.age(customer_1))

customer_1.add_cart({'product':'watch' , 'price': 200})
customer_1.add_cart({'product':'TV' , 'price': 1200})

customer_2.add_cart({'product':'phone' , 'price':1500})
customer_2.add_cart({'product':'bag' , 'price':700})


print ('The total of the customer_1 {} '.format (customer_1.calculate_total() ))
print ('The dicount of customer 2 user is ', customer_1.discount())

print ('The total of the customer_2 {} '.format (customer_2.calculate_total() ))
print ('The dicount of customer 2 user is ', customer_2.discount())







