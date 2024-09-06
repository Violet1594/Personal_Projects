class UserInterface:
    def get_user_input(self):
        sequence_type = input("Enter sequence type (arithmetic, fibonacci, geometric, combinations, permutations, binomial): ")

        if sequence_type == "arithmetic":
            length = int(input("Enter the length of the sequence: "))
            start = int(input("Enter the starting number: "))
            diff = int(input("Enter the difference: "))
            return sequence_type, start, diff, length

        elif sequence_type == "geometric":
            length = int(input("Enter the length of the sequence: "))
            start = int(input("Enter the starting number: "))
            ratio = int(input("Enter the ratio: "))
            return sequence_type, start, ratio, length

        elif sequence_type == "fibonacci":
            length = int(input("Enter the length of the sequence: "))
            return sequence_type, length

        elif sequence_type == "combinations":
            elements = input("Enter elements separated by spaces: ").split()
            r = int(input("Enter the size of each combination: "))
            return sequence_type, elements, r

        elif sequence_type == "permutations":
            elements = input("Enter elements separated by spaces: ").split()
            return sequence_type, elements

        elif sequence_type == "binomial":
            n = int(input("Enter n for binomial coefficient: "))
            k_max = int(input("Enter max value for k: "))
            return sequence_type, n, k_max

    def display_prediction(self, prediction):
        print(f"The predicted next item is: {prediction}")