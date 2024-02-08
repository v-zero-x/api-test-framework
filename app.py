from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database for demonstration purposes
# In a real application, this would likely be replaced with database calls
items = []

# items = [
#     {'id': 1, 'name': 'Item 1'},
#     {'id': 2, 'name': 'Item 2'},
# ]

@app.route('/items', methods=['GET'])
def get_items():
    """
    Retrieve and return the list of items.
    """
    return jsonify({'items': items})

@app.route('/items', methods=['POST'])
def create_item():
    """
    Create a new item with the data provided in the request.
    The new item is assigned a unique ID and added to the list of items.
    """
    new_item = request.json
    new_item['id'] = len(items) + 1  # Simple ID assignment strategy
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """
    Update an existing item identified by item_id with the data provided in the request.
    If the item does not exist, a 404 error is returned.
    """
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        item_data = request.json
        item.update(item_data)
        return jsonify(item)
    else:
        return jsonify({'message': 'Item not found'}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """
    Delete an existing item identified by item_id.
    If the item does not exist, the operation silently succeeds, mimicking idempotent behavior.
    """
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
