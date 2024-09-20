from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load data
df = pd.read_csv('clean_bike_share_data.csv')
data = df.to_dict(orient='records')

@app.route('/data', methods=['GET'])
def get_all_data():
    return jsonify({"data": data})

@app.route('/data/<int:index>', methods=['DELETE'])
def delete_entry(index):
    if 0 <= index < len(data):
        deleted_item = data.pop(index)
        return jsonify({"message": f"Item at index {index} deleted", "deleted_item": deleted_item})
    else:
        return jsonify({"error": "Index out of range"}), 404

# Uncomment and run the following lines to start the server
# if __name__ == '__main__':