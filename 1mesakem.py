#Name: Tamir David

def print_longest_name():
    """
    Prints the longest name from the file names.txt.
    """
    # Read the contents of the file "names.txt" and split it into a list of names
    names = open("names.txt").read().splitlines()

    # Find the longest name in the list using the `max()` function with the `key` parameter set to `len` and print it
    print(max(names, key=len))

def print_sum_of_lengths():
    """
    Prints the sum of the lengths of the words in the file names.txt.
    """
    # Read the contents of the file "names.txt" and split it into a list of names
    names = open("names.txt").read().splitlines()

    # Calculate the sum of the lengths of each name in the list using a generator expression and print it
    print(sum(len(name) for name in names))

def print_shortest_names():
    """
    Prints the shortest names from the file names.txt, with each name on a separate line.
    """
    # Read the contents of the file "names.txt" and split it into a list of names
    names = open("names.txt").read().splitlines()

    # Find the length of the shortest name in the list
    shortest_length = min(len(name) for name in names)

    # Print all the names with the shortest length, each on a separate line
    print('\n'.join(name for name in names if len(name) == shortest_length))

def create_name_length_file():
    """
    Creates a new file named name_length.txt that contains the length of every name in names.txt,
    with each length on a different line, according to the original order in names.txt.
    """
    # Read the contents of the file "names.txt" and split it into a list of names
    names = open("names.txt").read().splitlines()

    # Create a new file named "name_length.txt" and write the length of each name on a new line
    with open("name_length.txt", "w") as f:
        f.write('\n'.join(str(len(name)) for name in names))

def print_names_by_length():
    """
    Asks for user input of a number representing the length of a word and prints
    all names from the file names.txt that have that length.
    """
    # Read the contents of the file "names.txt" and split it into a list of names
    names = open("names.txt").read().splitlines()

    # Ask for user input of the desired word length
    length = int(input("Enter the length of a word: "))

    # Print all the names from the list that have a length equal to the user input
    print('\n'.join(name for name in names if len(name) == length))

print_longest_name()
print_sum_of_lengths()
print_shortest_names()
create_name_length_file()
print_names_by_length()