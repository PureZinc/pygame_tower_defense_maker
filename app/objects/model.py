# The class that defines how to save and manage objects
import uuid
from datetime import datetime


class Model:
    def __init__(self):
        self._store = {}
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self._unload()
    
    def _unload(self):
        return self._store

    def get(self, obj_id):
        obj = self._store.get(obj_id, None)
        if not obj:
            raise ValueError("Object not found")
        return obj

    def create(self, **attributes):
        obj = Model()
        for key, value in attributes.items():
            setattr(obj, key, value)
        obj.updated_at = datetime.now()
        self._store[obj.id] = obj
        return obj

    def update(self, obj_id, **updates):
        obj = self.get(obj_id)
        for key, value in updates.items():
            setattr(obj, key, value)
        obj.updated_at = datetime.now()
        self._store[obj_id] = obj
        return obj

    def delete(self, obj_id):
        if obj_id in self._store:
            del self._store[obj_id]
        else:
            raise ValueError("Object not found")
        
    def query(self, **kwargs):
        pass

    def save(self):
        pass