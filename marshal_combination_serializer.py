from itertools import combinations
import marshal
from datetime import datetime

class CombinationsSerializer:

    def __init__(self, objects_size=1, n_samples=1):
        """
        initialize Serializer with objects_size and number of samples
        """
        self.n_objects = [x for x in range(1, objects_size+1)]
        self.samples = n_samples

    def generate_combinations(self):
        self.possible_combinations = list(combinations(self.n_objects, self.samples))
    def serialize(self, output_file_source=f"serializedCombination_{datetime.now().date()}"):
        """
        Function serializes generated combinations to a file (default to "./serializedCombination_[current_date])
        This file can be uploaded to a bucket/db for deserialization 
        """
        with open(output_file_source, 'wb') as output_file:
            serialized_object = marshal.dump(self.possible_combinations, output_file)
        return serialized_object

    def deserialize(self, input_file_source=f"serializedCombination_{datetime.now().date()}"):
        """
        Function deserializes a marshal file to python object (default file source is "./serializedCombination_[current_date])
        """
        with open(input_file_source, 'rb') as input_file:
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