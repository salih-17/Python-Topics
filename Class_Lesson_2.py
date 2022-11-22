# Class method  : When you want to change the clasee variable or handiling the clasee
# instance method : when you want to use instance variable 
# Static methon : For the realation ship between the class and function
# Inttance method is the function inside the clases

from datetime import datetime , date

class Customer:
    no_customer = 0
    discount_percent = 0.1
    
    def __init__ (self , name , dob , gender):
        self.name  = name 
        self.dob = dob
        self.gender = gender
        self.email = name + "@gmail.com"
        self.cart = []
        self.cart_total = 0
        Customer.no_customer +=1
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

#customer_1 = Customer( 'A', '1990-01-01', 'Male')
#customer_2 = Customer( 'B', '1992-01-01', 'Female')



#print (customer_1.__dict__)
#print (customer_2.age())
#print (Customer.age(customer_1))

customer_1_string = 'A,1990,Femal'
customer_2_string = 'B,1993,male'

"""
customer_1.add_cart({'product':'watch' , 'price': 200})
customer_1.add_cart({'product':'TV' , 'price': 1200})

customer_2.add_cart({'product':'phone' , 'price':1500})
customer_2.add_cart({'product':'bag' , 'price':700})

Customer.set_discount_percent (0.2)

#print ('The total of the customer_1 {} '.format (customer_1.calculate_total() ))
#print ('The dicount of customer 2 user is ', customer_1.discount())

print (Customer.discount_percent)
print (customer_1.discount_percent)
print (customer_2.discount_percent)

"""
customer_1 = Customer.from_str_info (customer_1_string)
customer_2 = Customer.from_str_info (customer_2_string)

print (customer_1.name)


print (Customer.is_discount_day (date.today()))





