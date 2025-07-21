from flask import Flask, request, jsonify
from datastructure import FamilyStructure

app = Flask(__name__)

# Inicializar la estructura de datos de la familia Jackson
jackson_family = FamilyStructure('Jackson')

# Agregar los miembros iniciales de la familia
jackson_family.add_member({
    'id': 1,
    'first_name': 'John',
    'age': 33,
    'lucky_numbers': [7, 13, 22]
})

jackson_family.add_member({
    'id': 2,
    'first_name': 'Jane',
    'age': 35,
    'lucky_numbers': [10, 14, 3]
})

jackson_family.add_member({
    'id': 3,
    'first_name': 'Jimmy',
    'age': 5,
    'lucky_numbers': [1]
})

# Endpoint para obtener todos los miembros de la familia
@app.route('/members', methods=['GET'])
def get_all_members():
    try:
        members = jackson_family.get_all_members()
        return jsonify(members), 200
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

# Endpoint para obtener un miembro específico por ID
@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    try:
        member = jackson_family.get_member(member_id)
        if member is None:
            return jsonify({'error': 'Member not found'}), 404
        return jsonify(member), 200
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

# Endpoint para agregar un nuevo miembro
@app.route('/members', methods=['POST'])
def add_member():
    try:
        # Obtener los datos del request
        member_data = request.get_json()
        
        # Validar que se proporcionaron los datos necesarios
        if not member_data:
            return jsonify({'error': 'No data provided'}), 400
        
        required_fields = ['first_name', 'age', 'lucky_numbers']
        for field in required_fields:
            if field not in member_data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Validar tipos de datos
        if not isinstance(member_data['age'], int) or member_data['age'] <= 0:
            return jsonify({'error': 'Age must be a positive integer'}), 400
        
        if not isinstance(member_data['lucky_numbers'], list):
            return jsonify({'error': 'Lucky numbers must be a list'}), 400
        
        # Agregar el miembro
        new_member = jackson_family.add_member(member_data)
        return jsonify(new_member), 200
        
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

# Endpoint para eliminar un miembro
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    try:
        deleted_member = jackson_family.delete_member(member_id)
        if deleted_member is None:
            return jsonify({'error': 'Member not found'}), 404
        
        return jsonify({'done': True}), 200
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)