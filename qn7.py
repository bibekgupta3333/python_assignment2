# 7. Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.


def printOldAndYoungAccordingToAvgAge():
    people = [('ram', 'basnet', 21), ('sikxant', 'lama', 23), ('antman', 'brandster', 32),
              ('John', 'smith', 50),
              ('John', 'doe', 90),
              ('hemant', 'timalsina', 100), ('bhanu', 'bhakta', 95), ('abhram', 'linconn', 121)]
    avg_age = int(sum([each[2] for each in people])/len(people))
    print("the average is", avg_age)
    for each in people:
        if each[2] > avg_age:
            print('old ', each[0], each[1], each[2])
        else:
            print('young ', each[0], each[1], each[2])


if __name__ == "__main__":
    printOldAndYoungAccordingToAvgAge()
