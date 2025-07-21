class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    # Este método genera un 'id' único al agregar miembros a la lista (no debes modificar esta función)
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # Si no se proporciona un id, generar uno automáticamente
        if 'id' not in member or member['id'] is None:
            member['id'] = self._generate_id()
        else:
            # Si se proporciona un id, asegurarse de que _next_id sea mayor
            if member['id'] >= self._next_id:
                self._next_id = member['id'] + 1
        
        # Asegurar que el apellido sea siempre Jackson
        member['last_name'] = self.last_name
        
        # Agregar el miembro a la lista
        self._members.append(member)
        return member

    def delete_member(self, id):
        # Recorre la lista y elimina el miembro con el id proporcionado
        for i, member in enumerate(self._members):
            if member['id'] == id:
                return self._members.pop(i)
        return None

    def get_member(self, id):
        # Recorre la lista y obtén el miembro con el id proporcionado
        for member in self._members:
            if member['id'] == id:
                return member
        return None

    def get_all_members(self):
        return self._members