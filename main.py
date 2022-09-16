from views import *
from registration import *
import json

class Car(CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin, OrderMixin):
    def get_start(self):
        choice = input('Welcome!\nХотите начать? Да/Нет: ')
        while choice.lower() == 'да':
            print('Что бы вы хотели сделать?(1 - create, 2 - listing, 3 - retrieve, 4 - update, 5 - delete, 6 - order, 7 - exit)')
            choice = int(input('Выберите действие: (1,2,3,4,5,6,7): '))
            if choice == 1: print(super().create_auto())
            elif choice == 2: print(super().listing_auto())
            elif choice == 3: print(super().retrieve_auto())
            elif choice == 4: print(super().update_auto())
            elif choice == 5: print(super().delete_auto())
            elif choice == 6: print(super().order_auto())
            elif choice == 7: 
                print('Good luck!')
                break
            else: print('Такого действия нет')

car = Car()
car.get_start()
