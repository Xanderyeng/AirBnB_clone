import unittest
from models import FileStorage
from models import BaseModel


class TestFileStorage(unittest.TestCase):

    def test_all(self):
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        my_model = BaseModel()
        storage.new(my_model)
        all_objs = storage.all()
        self.assertIn(my_model, all_objs.values())

    def test_save(self):
        my_model = BaseModel()
        storage.new(my_model)
        storage.save()
        # Verify that the file.json is updated with serialized objects

    def test_reload(self):
        # Create and save a BaseModel instance
        my_model = BaseModel()
        storage.new(my_model)
        storage.save()

        # Create a new storage instance and reload data from file.json
        new_storage = FileStorage()
        new_storage.reload()

        # Retrieve the saved BaseModel instance from the new storage
        loaded_model = new_storage.get(BaseModel, my_model.id)
        self.assertIsNotNone(loaded_model)
        self.assertEqual(my_model.to_dict(), loaded_model.to_dict())


if __name__ == '__main__':
    unittest.main()
