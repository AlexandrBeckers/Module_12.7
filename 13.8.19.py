tickets = int(input('Сколько нужно билетов? :'))
visitor = tickets
price = 0
while visitor != 0:
    age = int(input(f'Сколько лет участнику {visitor} ? :'))
    if age < 18:
        print ('Проходи бесплатно')
    elif 18 <= age < 25:
        price += 990
        print ('С тебя 990р')
    else:
        price += 1390
        print ('С тебя 1390р')
    visitor -= 1

if tickets > 3:
    discount = price - (price * 0.1)
    print (f'Со всех с учетом скидки: {discount}р')
else:
    print(f'Итого к оплате: {price}р')