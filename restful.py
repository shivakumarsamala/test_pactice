from flask import Flask, request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required, current_identity
from security import authenticate,identity

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)

jwt =JWT(app,authenticate,identity)

items = []
class Item(Resource):
    @jwt_required()
    def get(self, name):
        return {'item': next(filter(lambda x: x['name'] == name, items), None)}
        '''item = next(filter(lambda x: x['name'] == name,items),None)
        for item in items:
            if item['name'] == name:
                return item
        return{'item': item}, 200 if item is not None else 404'''

    #@jwt_required
    def post(self,name):
        if next(filter(lambda x:x['name'] ==  name , items), None):
            return{'message' : "An Item with name '{}' already exists".format(name)}, 400
        data = request.get_json()
        item = {'name': name,'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self,name):
        global items
        items = list(filter(lambda x: x['name'] != name,items))
        return{'message': 'Item Deleted'}

    def put(self,name):
        data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item == None:
            item = {'name': name, 'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return(item)

class Itemslist(Resource):
    @jwt_required()
    def get(self):
        return{'items': items}

api.add_resource(Item,'/item/<string:name>')
api.add_resource(Itemslist,'/items')
if __name__ == '__main__':
    app.run(debug=True)



