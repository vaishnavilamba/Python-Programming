from flask import Flask,request,jsonify

app = Flask(__name__)

##Initialized data in my todo list
items = [
    {'id':1,'name':'Joey','description':'This is item 1'},
    {'id':2,'name':'Monica','description':'This is item 2'},
    {'id':3,'name':'Chandler','description':'This is item 3'},
    {'id':4,'name':'Ross','description':'This is item 4'},
    {'id':5,'name':'Rachel','description':'This is item 5'},
    {'id':6,'name':'Pheebe','description':'This is item 6'}
]

@app.route('/')
def welcome():
    return "Welcome to the sample Todo List App"

#Get : Retrive all the items

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

##get : Retrive specific item by id
@app.route('/items/<int:items_id>',methods = ['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':"Item not found"})
    return jsonify(item)

#Post : create new task
@app.route('/items',methods = ['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'error':"Item not found"})
    new_item = {
        'id':items[-1]['id'] + 1 if items else 1,
        'name':request.json['name'],
        'description':request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

## Put : update an exisiting item
app.route('/items/<int:item_id>',methods = ['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':'Item not found'})
    item['name'] = request.json.get('name',item['name'])
    item['description'] = request.json.get('description',item['description'])
    return jsonify(item)

#Delete : Delete an item
@app.route('/items/<int:item_id>',methods = ['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id']!=item_id]
    return jsonify({'result':"Item deleted"})



if __name__=='__main__':
    app.run(debug=True)
