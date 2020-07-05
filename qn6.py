# 6. Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.


def searchNameFromNamesList():
    people = ['ram', 'basnet',  'sikxant', 'lama', 'antman', 'brandster',
              'John', 'smith', 'bhanu', 'bhakta', 'abhram', 'linconn']
    input_search_name = input('please enter name to search: ')
    for each in people:
        if input_search_name == each:
            return "found"
    return "not found"


if __name__ == "__main__":

    print(searchNameFromNamesList())
