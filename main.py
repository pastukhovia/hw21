from store import Store
from shop import Shop
from request import Request

if __name__ == '__main__':
    store = Store({'печеньки': 25, 'собачки': 3, 'елки': 2, 'коробки': 2, 'кружки': 1})
    shop = Shop({'банки': 1})

    while True:
        user_input = input('Введите команду (0 - выход из программы): ')
        if user_input == '0':
            exit()

        print()
        input_list = user_input.split(' ')

        starting_index = 0
        for word in input_list:
            if word.isdigit():
                starting_index = input_list.index(word)
                break

        args = []
        adds = [3, 5, 0, 1]
        for add in adds:
            try:
                args.append(input_list[starting_index + add])
            except:
                args.append('')

        request = Request(args[0],
                          args[1],
                          int(args[2]),
                          args[3])

        available_items = store.get_items()
        if available_items[request.product] < request.amount:
            print(f'Не хватает на {request.from_where}, попробуйте заказать меньше')
        else:
            print(f'Нужное количество есть в {request.from_where}')
            print()
            if shop.add(request.product, request.amount) is False:
                print(f'В {request.to} недостаточно места, попобуйте что-то другое')
            else:
                print(f'Курьер забрал {request.amount} {request.product} с {request.from_where}')
                print(f'Курьер везет {request.amount} {request.product} с {request.from_where} в {request.to}')
                print(f'Курьер доставил {request.amount} {request.product} в {request.to}')
                store.remove(request.product, request.amount)

            print()
            print(f'В {request.from_where} хранится:')
            for k, v in store.get_items().items():
                if v > 0:
                    print(f'{v} {k}')

            print()
            print(f'В {request.to} хранится:')
            for k, v in shop.get_items().items():
                if v > 0:
                    print(f'{v} {k}')

            print()

