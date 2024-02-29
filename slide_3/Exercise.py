def switch_case(argument):
    switcher = {
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday",
    }
    return switcher.get(argument,'Không xác định')

print(switch_case(6));

fruits = ['apple', 'orange', 'lemon']

for fruit in fruits:
    print('Trái cây :', fruit)

length = input('Enter the length of the rectangle: ')
width = input('Enter the width of the rectangle: ')

for i in range(int(length)):
    for j in range(int(width)):
        print('*',end=' ')
    print()