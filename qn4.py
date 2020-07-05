# 4. Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?


def createListThenSortAndGetFirstSecondItem():
    input_list = []
    i = 1
    while(i != 0):
        input_names = input('please enter the names of colleges or friend: ')
        input_list.append(input_names)
        i = input('!!!don\'t want to enter name then press zero(0): ')
        if i.isnumeric() and int(i) == 0:
            i = 0
            continue
        if not i.isnumeric():
            i = 1
    if len(input_list) >= 2:
        return sorted(input_list)[:2], len(input_list)
    else:
        return "*"*5+'add more item in the list"'+"*"*5


if __name__ == "__main__":
    print(createListThenSortAndGetFirstSecondItem())
