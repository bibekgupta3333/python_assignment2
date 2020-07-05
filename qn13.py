# 13. Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple. If the following list of
# tuples was passed in:
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
# it should write the following in the file:
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21
import csv


def writeIntoCSVFile(filename, list_of_tuple):
    if filename.split('.')[-1].lower() == 'csv':
        header = ('name', 'address', 'age')
        list_of_tuple.insert(0, header)
        with open(filename, 'w') as file:
            csv_writer = csv.writer(file, delimiter=',')
            for row in list_of_tuple:
                csv_writer.writerow(list(row))


if __name__ == "__main__":
    writeIntoCSVFile('names.csv', [('George', '4312 Abbey Road', 22),
                                   ('John', '54 Love Ave', 21)])
