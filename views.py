import json

file_path = 'data1.json'

class GetMixin:
    '''Миксин для обмена данными с data.json'''
    def get_data(self):
        with open(file_path) as file:
            return json.load(file)

    def get_id(self):
        with open('id.txt','r') as file:
            id = int(file.read())
            id += 1
        with open('id.txt', 'w') as file_:
            file_.write(str(id))
        return id

class CreateMixin(GetMixin):
    '''Миксин для создания новых Авто'''
    def create_auto(self):
        data = super().get_data()
        try:
            new_product = {
                'id': super().get_id(),
                'brand': input('Введите марку Авто: '), 
                'model': input('Введите модель Авто: '), 
                'year': int(input('Введите год выпуска Авто: ')), 
                'engine': round(float(input('Введите объем двигателя Авто: ')),1), 
                'color': input('Введите цвет Авто: '),
                'body': input('Введите тип кузова Авто / варианты(седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап): '),
                'mileage': int(input('Введите пробег Авто: ')),
                'price': round(float(input('Введите цену Авто: ')),2)
            }
        except ValueError:
            print('Вы ввели некорректные данные')
            self.create_auto()
        else:
            data.append(new_product)
            with open(file_path,'w') as file:
                json.dump(data, file)
            return 'Successfully Created!'

class ListingMixin(GetMixin):
    '''Миксин для получения списка всех Авто'''
    def listing_auto(self):
        print('Список всех Авто')
        data = super().get_data()
        print(data)
        return 'End'

class RetrieveMixin(GetMixin):
    '''Миксин для получения одного Авто по индексу'''
    def retrieve_auto(self):
        data = super().get_data()
        try:
            id = int(input('Введите id продукта: '))
        except ValueError:
            print('Вы ввели некорректные данные')
            return self.retrieve_data()
        else:
            one_car = list(filter(lambda x: x['id'] == id, data))
            if not one_car: return 'Такого продукта нет'
            else: return one_car[0]

class UpdateMixin(GetMixin):
    '''Миксин для обновления данных об Авто'''
    def update_auto(self):
        data = super().get_data()
        flag = False
        try:
            id = int(input('Введите id продукта: '))

        except ValueError:
            print('Введите корректное id!')
            return self.update_auto()
        else: 
            one_product = list(filter(lambda x: x['id'] == id, data))
            if not one_product: return 'Такого продукта нет'
            product = data.index(one_product[0])
            choice = int(input('Что вы хотите изменить? (1 - brand, 2 - model, 3 - year, 4 - engine, 5 - color, 6 - body, 7 - mileage, 8 - price):'))
            if choice == '1': 
                data[product]['brand'] = input('Введите новую марку Авто: ')
                flag = True
            elif choice == '2':
                data[product]['model'] = input('Введите новую модель Авто: ')
                flag = True
            elif choice == '3':
                try:
                    data[product]['year'] = int(input('Введите новый год выпуска Авто: '))
                except ValueError: 
                    return 'Вы ввели некорректные данные'
                else:
                    flag = True
            elif choice == '4':
                try:
                    data[product]['engine'] = input('Введите новый объем двигателя Авто: ')
                except ValueError: 
                    return 'Вы ввели некорректные данные'
                else:
                    flag = True
            elif choice == '5':
                data[product]['color'] = input('Введите новый цвет Авто: ')
                flag = True
            elif choice == '6':
                data[product]['body'] = input('Введите новый тип кузова Авто (седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап): ')
                flag = True
            elif choice == '7':
                try:
                    data[product]['mileage'] = int(input('Введите новый пробег Авто: '))
                except ValueError: 
                    return 'Вы ввели некорректные данные'
                else:
                    flag = True
            elif choice == '8':
                try:
                    data[product]['price'] = round(float(input('Введите новую цену Авто: ')),2)
                except ValueError: 
                    return 'Вы ввели некорректные данные'
                else:
                    flag = True
            else:
                print('Такого поля нет')
            with open(file_path,'w') as file:
                json.dump(data, file)
        if flag: return 'Successfully updated!'
        else: return 'Такого продукта нет'

class DeleteMixin(GetMixin):
    '''Миксин для удаления Авто'''
    def delete_auto(self):
        data = super().get_data()
        try:
            id = int(input('Введите id продукта: '))
        except ValueError:
            print('Вы ввели некорректное id!')
            return self.delete_auto()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
        if not one_product: 
            return 'Такого продукта нет'
        product = data.index(one_product[0])
        data.pop(product)
        
        with open(file_path,'w') as file:
            json.dump(data, file)
        return 'Successfully deleted!'

class OrderMixin(GetMixin):
    '''Миксин для выполнения заказов'''
    def order_auto(self):
        data = super().get_data()
        list_of_orders = []
        try:
            id = int(input('Введите id продукта: '))
        except ValueError:
            print('Вы ввели некорректное id')
            self.order_auto()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))[0]
        if not one_product: 
            return 'Такого продукта нет'
        product = one_product
        print(f'Ваш заказ: {one_product["brand"]} {one_product["model"]}')

        with open(file_path,'w') as file:
            json.dump(data, file)
        return 'Ваш заказ принят'
