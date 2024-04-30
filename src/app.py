from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]

from flask import jsonify
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


from flask import jsonify
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body) # Agrega el nuevo todo a la lista
    return jsonify(todos)  # Devuelve la lista de todos como JSON


from flask import jsonify
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if position <len(todos):
        del todos[position] # Elimina el elemento en la posición indicada
        return jsonify(todos) # Devuelve la lista de todos actualizada
    else:
        return jsonify({"error": "La posición indicada está fuera de rango"}), 404
    

# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

