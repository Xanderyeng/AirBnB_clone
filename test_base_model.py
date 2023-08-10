import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()
        self.base_model.name = "My_First_Model"
        self.base_model.my_number = 89

    def test_instance_attributes(self):
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertEqual(self.base_model.name, "My_First_Model")
        self.assertEqual(self.base_model.my_number, 89)

    def test_save_method(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['name'], "My_First_Model")
        self.assertEqual(model_dict['my_number'], 89)
        self.assertEqual(type(model_dict['created_at']), str)
        self.assertEqual(type(model_dict['updated_at']), str)

    def test_from_dict_method(self):
        model_dict = self.base_model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.base_model.id, new_model.id)
        self.assertEqual(self.base_model.name, new_model.name)
        self.assertEqual(self.base_model.my_number, new_model.my_number)
        self.assertEqual(self.base_model.created_at, new_model.created_at)
        self.assertEqual(self.base_model.updated_at, new_model.updated_at)


if __name__ == '__main__':
    unittest.main()