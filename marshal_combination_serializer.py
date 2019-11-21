import marshal
from datetime import datetime
from itertools import combinations


class CombinationsSerializer:

    @classmethod
    def __init__(cls, objects_size=1, n_samples=1):
        """
        initialize Serializer with objects_size and number of samples
        """
        cls.n_objects = [x for x in range(1, objects_size+1)]
        cls.samples = n_samples

    @classmethod
    def generate_combinations(cls):
        cls.possible_combinations = list(combinations(cls.n_objects, cls.samples))
        return cls.possible_combinations
    
    @classmethod
    def serialize(cls, output_file_path=f"serializedCombination_{datetime.now().date()}"):
        """
        Function serializes generated combinations to a file (default to "./serializedCombination_[current_date])
        This file can be uploaded to a bucket/db for deserialization 
        """
        cls.output_file_path = f"serializedCombination_{datetime.now().date()}"
        with open(cls.output_file_path, 'wb') as output_file:
            serialized_object = marshal.dump(cls.possible_combinations, output_file)
        return serialized_object
    
    @classmethod
    def deserialize(cls, input_file_path=f"serializedCombination_{datetime.now().date()}"):
        """
        Function deserializes a marshal file to python object (default file path is "./serializedCombination_[current_date])
        """
        with open(input_file_path, 'rb') as input_file:
            deserialized_object = marshal.load(input_file)
        return deserialized_object

if __name__ == "__main__":
    serializer = CombinationsSerializer(37, 5)
    
    start_time = datetime.now()
    serializer.generate_combinations()
    end_time = datetime.now()
    print("{} combinations generated in {}".format(len(serializer.possible_combinations), end_time-start_time))

    start_time = datetime.now()
    serializer.serialize()
    end_time = datetime.now()
    print("{} combinations serialized in {}".format(len(serializer.possible_combinations), end_time-start_time))

    start_time = datetime.now()
    possible_combinations = serializer.deserialize()
    end_time = datetime.now()
    print("File deserialized in {}".format(end_time-start_time))
    
    echo_result = input("Print combinations? press 'N' to skip\n>> ")
    if echo_result.lower() != "n":
        print(possible_combinations)
    print("Completed!")
