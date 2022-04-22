from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"mesaaage": "pong!"})

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products": products, "message": "Here are your products!"})

@app.route('/products/<string:product_name>', methods=['GET'])
def getProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        return jsonify({"product": productFound[0], "message": "Here is your product!"})
    return jsonify({"message": "Product not found!"})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "id": request.json['id'],
        "name" : request.json['name'],
        "price" : request.json['price']
    }
    products.append(new_product)
    return jsonify({"message":"Product added successfully!", "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        return jsonify({"message": "Product updated successfully!", "product": productFound[0]})
    return jsonify({"message": "Product not found!"})

@app.route('/products/<int:product_id>', methods=['DELETE'])
def deleteProduct(product_id):
    productFound = [product for product in products if product['id'] == product_id]
    if (len(productFound) > 0):
        products.remove(productFound[0])
        return jsonify({"message": "Product deleted successfully!", "products": products})
    return jsonify({"message": "Product not found!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)