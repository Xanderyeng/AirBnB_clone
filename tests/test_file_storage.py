import unittest
from models import FileStorage
from models import BaseModel

class TestFileStorage(unittest.TestCase):

    def test_new(self):
        storage = FileStorage()
        my_model = BaseModel()
        storage.new(my_model)
        self.assertIn(my_model, storage.all().values())

    def test_save_reload(self):
        storage = FileStorage()
        my_model = BaseModel()
        storage.new(my_model)
        storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        reloaded_model = new_storage.get(BaseModel, my_model.id)
        self.assertIsNotNone(reloaded_model)
        self.assertEqual(my_model.id, reloaded_model.id)
        self.assertEqual(my_model.created_at, reloaded_model.created_at)
        self.assertEqual(my_model.updated_at, reloaded_model.updated_at)

