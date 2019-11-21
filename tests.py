import unittest
from itertools import combinations

from marshal_combination_serializer import CombinationsSerializer


class CombinationsSerializerTest(unittest.TestCase):
    serializer = CombinationsSerializer(objects_size=5, n_samples=2)

    def test_combination_generator(self):
        self.serializer.possible_combinations = self.serializer.generate_combinations()
        self.assertEqual(self.serializer.possible_combinations, list(combinations([1, 2, 3, 4, 5], 2)))
    
    def test_serialize(self):
        self.serializer.serialize()
        self.assertEqual(f"{open(self.serializer.output_file_path).closed}", "False")
    
    def test_deserialize(self):
        deserialized_object = self.serializer.deserialize()
        self.assertEqual(deserialized_object, self.serializer.possible_combinations)