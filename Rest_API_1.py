# from flask import Flask

# app=Flask(__name__)

# @app.route('/') # this is important

# def home():
#     return 'hello world!'

# app.run(port=5000) # change port if error 4999




s,*y=[23,4,5,6,7]
print(s)
print(y)


class p:
    def __init__(self,n,a):
        self.n=n
        self.a=a

    
b=p('sha',9)
print(b)
        


class p:
    def __init__(self,n,a):
        self.n=n
        self.a=a
    def __str__(self):# covert object to string
        return 'hello' 
           
    
b=p('sha',9)
print(b)
        

class book:
    s=('w','r') # class property
    def __init__(self,n,a):
        self.n=n
        self.a=a

    def __repr__(self):
        return f"book {self.n},{self.a},ok by "
        
    @classmethod
    def sk(cls,n):
        return book(n,book.s[1])


k=book.sk('shahid')
print(k)





from flask import Flask,jsonify,render_template,request

app=Flask(__name__)

stores=[
    {
        "name":"shahid",
        "items":[
            {
                "name":"my item",
                "price":12.02
            }
        ]
    }
]


@app.route('/')
def home():
    return render_template('index.html')





# post/store
@app.route('/store',methods=['POST']) # this is important
def create_store():
    request_data=request.get_json()
    new_store={
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)


# get/store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message':'store not found'}) 


# get/store
@app.route('/store')
def get_stores():
    return jsonify({"stores":stores}) # we r converting in json and it should be a dictionary format.


#post/store/<string:name>/item
@app.route('/store/<string:name>/item',methods=['POST']) 
def create_item_in_store(name):
    request_data=request.get_json()
    for store in stores:
        if store['name']==name:
            new_item={
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['item'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'}) 

#  get/store/<string:name>/item
@app.route('/store/<string:name>/item') 
def get_item_in_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'store not found'}) 


app.run(port=5000) # change port if error 4999



