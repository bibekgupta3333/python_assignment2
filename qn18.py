# 18. Find a package in the Python standard library for dealing with
# JSON. Import the library module and inspect the attributes of the
# module. Use the help function to learn more about how to use the
# module. Serialize a dictionary mapping 'name' to your name and 'age'
# to your age, to a JSON string. Deserialize the JSON back into
# Python.

import json


def deserialize(input_data):
    input_data = json.loads(input_data)
    print('json str to', type(input_data))
    return input_data


def serialize(input_data):
    input_data = json.dumps(input_data, indent=4, sort_keys=True)
    print('json str to', type(input_data))
    return input_data


if __name__ == "__main__":
    data = '''
    {"name":"Bibek Gupta","age":20
    }
    '''
    print(deserialize(data))
    data = deserialize(data)
    print('================================')
    print(serialize(data))
