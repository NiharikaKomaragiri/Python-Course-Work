#oops concept
class Flipkart:        
    products = {'laptop':98768,
                'phone':72345,
                'earphones':789,
                'bags':780}

    #classmethod
    @classmethod
    def showproducts(cls):
        print(cls.products)

    #instance method
    def register(self,name,phno): #Here self knows who is calling 
        self.username=name
        self.phoneno=phno
        print(f'Welcome to the Flipkart {self.username}, shop now!!!')

    #staticmethod
    @staticmethod
    def discount():
        print("hey all,10% discount is goin on")

niharika=Flipkart()
niharika.register('niharika','987654321')
niharika.discount()
niharika.showproducts()
print()
vijay=Flipkart()
vijay.register('vijay','3456789876')
vijay.discount()
vijay.showproducts()
print()
lohi=Flipkart()
lohi.register('lohisree','2345678987')
print()
nivitha=Flipkart()
nivitha.register('nivitha','23456789')


OUTPUT

= RESTART: C:/Users/nihar/OneDrive/Documents/Desktop/python course work/oops.py

Welcome to the Flipkart niharika, shop now!!!
hey all,10% discount is goin on
{'laptop': 98768, 'phone': 72345, 'earphones': 789, 'bags': 780}

Welcome to the Flipkart vijay, shop now!!!
hey all,10% discount is goin on
{'laptop': 98768, 'phone': 72345, 'earphones': 789, 'bags': 780}

Welcome to the Flipkart lohisree, shop now!!!

Welcome to the Flipkart nivitha, shop now!!!




#Constructor is a special method used to initialize object values automatically
class Flipkart:
    def __init__(self,name,phno):
            self.username=name
            self.phoneno=phno
            print(f'Welcome to the Flipkart {self.username}, shop now!!!')

niharika=Flipkart('niharika','3456789987')

OUPUT
= RESTART: C:/Users/nihar/OneDrive/Documents/Desktop/python course work/oops.py

Welcome to the Flipkart niharika, shop now!!!



class insta:
    def __init__(self,username):
        self.username = username
        self.bio = ' '
        self.fullname = ''
        self.followers = set()
        self.following = set()
        print(f"Welcome to the instagram {self.username}")
        print(f"Welcome to the instagram {self.bio}")
        print(f"Welcome to the instagram {self.fullname}")
        print(f'followers: {len(self.followers)} Following:{len(self.following)}')

insta=insta('niharika')

OUTPUT
= RESTART: C:/Users/nihar/OneDrive/Documents/Desktop/python course work/oops.py
Welcome to the instagram niharika
Welcome to the instagram  
Welcome to the instagram 
followers: 0 Following:0
























