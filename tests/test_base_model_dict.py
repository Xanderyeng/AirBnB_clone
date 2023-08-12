import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModelDict(unittest.TestCase):

    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89

    def test_to_dict(self):
        my_model_json = self.my_model.to_dict()

        self.assertIsInstance(my_model_json, dict)
        self.assertTrue('id' in my_model_json)
        self.assertTrue('created_at' in my_model_json)
        self.assertTrue('updated_at' in my_model_json)
        self.assertTrue('name' in my_model_json)
        self.assertTrue('my_number' in my_model_json)
        self.assertEqual(my_model_json['name'], "My_First_Model")
        self.assertEqual(my_model_json['my_number'], 89)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')

        created_at = datetime.strptime(
            my_model_json['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        self.assertEqual(self.my_model.created_at, created_at)

    def test_from_dict(self):
        my_model_json = self.my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)

        self.assertIsInstance(my_new_model, BaseModel)
        self.assertEqual(my_new_model.id, self.my_model.id)
        self.assertEqual(my_new_model.name, "My_First_Model")
        self.assertEqual(my_new_model.my_number, 89)
        self.assertEqual(my_new_model.__class__.__name__, 'BaseModel')

    def test_instance_equality(self):
        my_new_model = BaseModel(**self.my_model.to_dict())

        self.assertIsNot(my_new_model, self.my_model)
        self.assertEqual(my_new_model.id, self.my_model.id)
        self.assertEqual(my_new_model.name, self.my_model.name)
        self.assertEqual(my_new_model.my_number, self.my_model.my_number)


if __name__ == '__main__':
    unittest.main()
