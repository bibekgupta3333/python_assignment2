# 14. Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.
# For the data in the previous example it would return:
# [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
# 'John', 'address': '54 Love Ave', 'age': 21}]
import csv


def readFromCSVFile(filename):
    if filename.split('.')[-1].lower() == 'csv':
        output_list = []
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                output_list.append(dict(row))
        return output_list


if __name__ == "__main__":
    print(readFromCSVFile('C:\\Users\\BibekG\\Desktop\\Python_homeWork\\names.csv'))
