print("Welcome To Python pizza Deliveries\n")
size=input("enter 'S' for small Pizza , 'M' for Medium pizza And 'L' for large pizza :")
pepperoni=input("do you want pepperoni Y or N :")
cheese=input("Do you want extra cheese Y or N :")

if size=='S':
    if pepperoni=='Y':
        if cheese=='Y':
            bill=15+2+1
        else:
            bill=15+2
    elif pepperoni=='N':
        if cheese=='Y':
            bill=15+1
        else:
            bill=15
elif size=='M':
    if pepperoni=='Y':
        if cheese=='Y':
            bill=20+3+1
        else:
            bill=20+3
    elif pepperoni=='N':
        if cheese=='Y':
            bill=20+1
        else:
            bill=20
elif size=='L':
    if pepperoni=='Y':
        if cheese=='Y':
            bill=25+3+1
        else:
            bill=25+3
    elif pepperoni=='N':
        if cheese=='Y':
            bill=25+1
        else:
            bill=25


print(f"Total Bill is {bill}")

