products={
    'salt':{'stock':20,'price':60,'discount':20},
    'sugar':{'stock':10,'price':50,'discount':12},
    'coco':{'stock':0,'price':70,'discount':10},
    'honey':{'stock':20,'price':160,'discount':4},
    'butter':{'stock':0,'price':90,'discount':0},
    }

for i in products:
    price=products[i]['price']
    print(i,price-(price*products[i]['discount']/100))
    
        
    
