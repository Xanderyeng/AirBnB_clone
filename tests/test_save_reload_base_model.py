import unittest
from models import storage
from models.base_model import BaseModel


class TestSaveReloadBaseModel(unittest.TestCase):

    def test_save_reload(self):
        storage.reload()

        all_objs = storage.all()

        # Check if reloaded objects are present
        self.assertTrue(all_objs)

        # Create a new object
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

        # Check if the new object was saved
        saved_model = storage.get(BaseModel, my_model.id)
        self.assertEqual(saved_model.id, my_model.id)
        self.assertEqual(saved_model.name, "My_First_Model")
        self.assertEqual(saved_model.my_number, 89)


if __name__ == '__main__':
    unittest.main()
