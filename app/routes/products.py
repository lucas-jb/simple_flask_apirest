from flask import Blueprint, request, jsonify
#from app.services.products import products
from app.models.products import products as productsBD

app = Blueprint('products', __name__, url_prefix='/products')

#products = products.Products()

@app.route('', methods=['GET'])
def getProducts():
    return jsonify({"products": productsBD, "message": "Here are your products!"})

@app.route('', methods=['POST'])
def addProduct():
    new_product = {
        "id": request.json['id'],
        "name" : request.json['name'],
        "price" : request.json['price']
    }
    productsBD.append(new_product)
    return jsonify({"message":"Product added successfully!", "products": productsBD})


@app.route('/<string:product_name>', methods=['GET'])
def getProduct(product_name):
    productFound = [product for product in productsBD if product['name'] == product_name]
    if (len(productFound) > 0):
        return jsonify({"product": productFound[0], "message": "Here is your product!"})
    return jsonify({"message": "Product not found!"})

@app.route('/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in productsBD if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        return jsonify({"message": "Product updated successfully!", "product": productFound[0]})
    return jsonify({"message": "Product not found!"})

@app.route('/<int:product_id>', methods=['DELETE'])
def deleteProduct(product_id):
    productFound = [product for product in productsBD if product['id'] == product_id]
    if (len(productFound) > 0):
        productsBD.remove(productFound[0])
        return jsonify({"message": "Product deleted successfully!", "products": productsBD})
    return jsonify({"message": "Product not found!"})