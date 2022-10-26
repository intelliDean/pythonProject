def sales():
    global total
    product1 = 5000
    product2 = 2300
    product3 = 840
    product4 = 2900
    product5 = 18500
    grand_total = 0
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    p5 = 0
    p_num = int(input("enter 1 - 5 for product number or -1 to quit\n"))
    quantity = int(input("enter quantity or -1 to quit\n"))
    while p_num != -1:
        if p_num == 1:
            price = product1
            total = price * quantity
            p1 += 1
        elif p_num == 2:
            price = product2
            total = price * quantity
            p2 += 1
        elif p_num == 3:
            price = product3
            total = price * quantity
            p3 += 1
        elif p_num == 4:
            price = product4
            total = price * quantity
            p4 += 1
        elif p_num == 5:
            price = product5
            total = price * quantity
            p5 += 1
        else:
            print("invalid product number")
        grand_total += total
        p_num = int(input("enter product number\n"))
        quantity = int(input("enter quantity\n"))
    print(f"\nThe total price is {grand_total:,}")


if __name__ == '__main__':
    sales()
