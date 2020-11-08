"""Task 1: Write a Python program to parse (split) the content of a csv file using string functions only
and store it in an appropriate data structure. Print out a table with all the data using the
following column headings (which are the first line in the css file): Title,Name,ID,Email,Company,Updated.
Remember to consider readability and use formatting instructions in the output. """

import datetime
from operator import itemgetter


def read_csv_to_list(filename):
    path = "C:/Users/redye/MASTERS YORK/Advanced Programming/Week 2 Labs/"
    file = open(path + filename, 'r')
    contents = []

    # read file into list structure
    for line in file:
        contents.append(line.split(","))
    file.close()

    return contents


# create list of longest entries for each column
def get_longest_entries(doc):
    longest_entries = []
    for i in range(len(doc[0])):
        max_len = 0
        for entry in doc:
            if len(entry[i]) > max_len:
                max_len = len(entry[i])
        longest_entries.append(max_len)
    return longest_entries


# print contents of list using longest entries to format correctly
def print_contents(doc, longest_entries):
    for item in doc:
        for index in range(len(item)):
            print(f"{item[index]:>{longest_entries[index] + 3}}", end="")
            index += 1
        print("\n")


# creates a date object from a string
def get_date_object_from_string(date_string):
    d = date_string.split("/")
    return datetime.date(int(d[2]), int(d[1]), int(d[0]))


# sorts table by column of dates in string format
def sort_by_date(doc_contents):
    # create a date object and append to each record
    for entry in doc_contents:
        if entry[0] != "Updated":
            entry.append(get_date_object_from_string(entry[0]))
        else:
            entry.append(datetime.date(1, 1, 1))  # ensure header remains first when sorted
    # sort the list using the datetime object column
    doc_contents = sorted(doc_contents, key=itemgetter(7))
    # delete extra date column used for sorting
    for entry in doc_contents:
        entry.pop()
    return doc_contents


# remove new line character from string
def remove_new_line_character(line):
    stripped_line = line.rstrip("\n")  # remove new line characters
    return stripped_line


# main application
def main():
    # read in csv file
    doc_contents = read_csv_to_list("PeopleTrainingDate.csv")

    # amend header column to have same number of elements
    doc_contents[0].insert(2, "Forename")
    # remove final entry of "\n"
    doc_contents.pop()

    # print formatted file
    print_contents(doc_contents, get_longest_entries(doc_contents))

    """ TASK 2: Rearrange the data extracted in exercise one and output it to file so that it is sorted 
    in date order (oldest date first) and Updated is the first column in the file (on the left). """

    # move updated to 1st column
    for entry in doc_contents:
        entry.insert(0, entry.pop(len(entry) - 1))
        entry[0] = remove_new_line_character(entry[0])
    # sort by date
    doc_contents = sort_by_date(doc_contents)
    # print formatted data
    print_contents(doc_contents, get_longest_entries(doc_contents))

    """TASK 3: A recent update to the PeopleTrainingDate file has arrived, PeopleTrainingDateUpdatePreview the document. 
    Unfortunately, the data has been formatted in a different order. Review the file and write a program to rearrange 
    the data and append it to the file you created in Exercise 2. You will also need to check that there are no errors 
    with the csv format."""

    # read new csv file
    updated_contents = read_csv_to_list("PeopleTrainingDateUpdate.csv")
    # split column with two values and rearrange in order
    for entry in updated_contents:
        entry.insert(5, entry[1].split(" ")[0])
        entry.insert(5, entry[1].split(" ")[1])
        entry.pop(1)

    # merge both lists
    final_contents = doc_contents + updated_contents
    # sort by date
    final_contents = sort_by_date(final_contents)
    # remove extra new line characters
    for entry in final_contents:
        entry[-1] = remove_new_line_character(entry[-1])
    # print formatted data
    print_contents(final_contents, get_longest_entries(final_contents))

if __name__ == "__main__":
    main()
