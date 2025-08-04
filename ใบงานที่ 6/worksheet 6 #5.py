def discountcal(price, discount):
    return price*(discount/100)
x = int(input("price: "))
y = int(input("discount: "))
print(discountcal(x,y))