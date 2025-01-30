from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# In-memory list of restaurants (will reset when app restarts)
restaurants = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_restaurant():
    """Adds a restaurant to the list."""
    data = request.get_json()
    restaurant_name = data.get("name")
    
    if restaurant_name and restaurant_name not in restaurants:
        restaurants.append(restaurant_name)
        return jsonify({"message": "Restaurant added!", "restaurants": restaurants}), 201
    else:
        return jsonify({"message": "Invalid or duplicate entry"}), 400

@app.route('/pick', methods=['GET'])
def pick_restaurant():
    """Picks a random restaurant."""
    if restaurants:
        selected = random.choice(restaurants)
        return jsonify({"restaurant": selected}), 200
    else:
        return jsonify({"message": "No restaurants available"}), 404

@app.route('/list', methods=['GET'])
def list_restaurants():
    """Returns the list of available restaurants."""
    return jsonify({"restaurants": restaurants}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
