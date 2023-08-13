#!/usr/bin/env python3

import unittest
from datetime import datetime
from models import FileStorage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)

    def test_to_dict(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('__class__', my_model_dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)

    def test_save(self):
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_str_representation(self):
        my_model = BaseModel()
        str_repr = str(my_model)
        self.assertIsInstance(str_repr, str)
        self.assertIn(my_model.id, str_repr)

    def test_reload(self):
        my_model = BaseModel()
        my_model.save()
        initial_updated_at = my_model.updated_at

        new_storage = FileStorage()
        new_storage.reload()

        reloaded_model = new_storage.get(BaseModel, my_model.id)
        self.assertIsNotNone(reloaded_model)
        self.assertEqual(initial_updated_at, reloaded_model.updated_at)


if __name__ == '__main__':
    unittest.main()
