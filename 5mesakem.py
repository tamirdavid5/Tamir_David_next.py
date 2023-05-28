#Name: Tamir David

class IDIterator:
    def __init__(self, start_id=0):
        self._id = start_id

    def __iter__(self):
        return self

    def __next__(self):
        if self._id > 999999999:
            raise StopIteration

        while True:
            if self.check_id_valid(self._id):
                valid_id = self._id
                self._id += 1
                return valid_id
            else:
                self._id += 1

    @staticmethod
    def check_id_valid(id_number):
        return sum(int(digit) if index % 2 == 0 else sum(int(d) for d in str(int(digit) * 2)) for index, digit in enumerate(str(id_number))) % 10 == 0

def id_generator(start_id):
    while start_id <= 999999999:
        if IDIterator.check_id_valid(start_id):
            yield start_id
        start_id += 1
def main():
    # Ask for ID input
    id_input = input("Enter a 9-digit ID number: ")

    # Ask for iterator or generator choice
    choice = input("Enter 'it' for iterator or 'gen' for generator: ")

    # Convert input to integer and create an iterator or generator based on the choice
    start_id = int(id_input) + 1
    if choice == "it":
        iterator = IDIterator(start_id)
        ids = [next(iterator) for _ in range(10)]
    elif choice == "gen":
        generator = id_generator(start_id)
        ids = [next(generator) for _ in range(10)]

    # Print the generated IDs
    for id_number in ids:
        print(id_number)


# Execute the main function
if __name__ == "__main__":
    main()








