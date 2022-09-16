#**************************************************************************************************************(06.09.22)
from search import search_object

class CRUDMixin:
    def _get_or_set_objects_and_id(self):
        try:
            if (self.objects or not self.objects) and (self.id or not self.id):
                pass
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0

    def create(self, **kwargs):
        self._get_or_set_objects_and_id()
        self.id += 1
        object_ = dict(id=self.id, **kwargs)
        self.objects.append(object_)
        return {'status': 201, 'msg': object_}

    def list(self):
        result = []
        for obj in self.objects:
            result.append({'id': obj['id'], 
            'title': obj['title'], 
            'price': obj['price']})
        return {'status': 200, 'msg': result}

    @search_object
    def detail(self, id, **kwargs):
        obj = kwargs['object_']
        if obj:
            return {'status': 200, 'msg': obj}
        return {'status': 404, 'msg': 'Not found!'}

    @search_object
    def update(self, id, **kwargs):
        obj = kwargs.pop('object_')
        if obj:
            obj.update(**kwargs)
            return {'status': 206, 'msg': obj}
        return {'status': 404, 'msg': 'Not found!'}

    @search_object
    def delete(self, id, **kwargs):
        obj = kwargs['object_']
        if obj:
            self.objects.remove(obj)
            return {'status': 204, 'msg': 'Successfully deleted!'}
        return {'status': 404, 'msg': 'Not found!'}

    def save(self):
        import json
        with open('data.json', 'w') as file:
            json.dump(self.objects, file)
        return 'Saved'

smartphones = CRUDMixin()
print(smartphones.create(title = 'Redmi Note 10', description = 'The best for own price', qty = 10, price = 200))
print(smartphones.create(title = 'Redmi Note 20', description = 'Flagman of Redmi phones, Best!', qty = 3, price = 500))
print(smartphones.create(title = 'Iphone 14 Pro Max', description = 'New phone for ponts!', qty = 5, price = 1300))
print('-----------------')
print(smartphones.list())
print(smartphones.detail(3))
print(smartphones.detail(15))
print(smartphones.detail(1))
print()
print()
print(smartphones.update(1, title = 'Redmi Note 100 PRo Max', price = 1000))
print(smartphones.detail(1))
print(smartphones.update(2, qty = 1))
print()
print()
print(smartphones.detail(2))
print('--------------------')
print(smartphones.list())
print(smartphones.delete(1))
print(smartphones.list())
print(smartphones.create(title = 'Samsung Galaxy S22', description = 'New phone for Android lovers!', qty = 15, price = 900))
print(smartphones.create(title = 'Samsung Galaxy S9 Edge', description = 'At the time was super new phone with android system!', qty = 3, price = 300))
print(smartphones.save())