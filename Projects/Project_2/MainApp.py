from SequenceGenerator import SequenceGenerator
from PatternPredictor import PatternPredictor
from UserInterface import UserInterface

import numpy as np
class MainApp:
    def __init__(self):
        self.sequence_generator = SequenceGenerator()
        self.pattern_predictor = PatternPredictor()
        self.ui = UserInterface()

    def run(self):
        print("Starting program...")  # Debugging output
        seq_type, *params = self.ui.get_user_input()

        # Generate sequence based on user input
        if seq_type == "arithmetic":
            sequence = self.sequence_generator.generate_arithmetic_sequence(*params)
        elif seq_type == "geometric":
            sequence = self.sequence_generator.generate_geometric_sequence(*params)
        elif seq_type == "fibonacci":
            sequence = self.sequence_generator.generate_fibonacci_sequence(params[0])
        elif seq_type == "combinations":
            sequence = self.sequence_generator.generate_combinations(params[0], params[1])
        elif seq_type == "permutations":
            sequence = self.sequence_generator.generate_permutations(params[0])
        elif seq_type == "binomial":
            sequence = self.sequence_generator.generate_binomial_coefficients(params[0], params[1])

        print(f"Generated sequence: {sequence}")  # Debugging output

        # Create a mapping from unique elements to numbers
        unique_elements = sorted(set([item for sublist in sequence for item in sublist]))
        element_to_number = {element: i+1 for i, element in enumerate(unique_elements)}
        print(f"Element to Number Mapping: {element_to_number}")  # Debugging output

        # Convert sequence to numeric form
        numeric_sequence = [[element_to_number[item] for item in sublist] for sublist in sequence]
        print(f"Numeric sequence: {numeric_sequence}")  # Debugging output

        # Prepare training data (X, y)
        X, y = self.sequence_generator.generate_training_data(numeric_sequence)
        print(f"Training data (X): {X}, labels (y): {y}")  # Debugging output

        # Flatten the data for the machine learning model
        X_flat = [np.ravel(x) for x in X]  # Flatten each sublist in X
        y_flat = np.ravel(y)  # Flatten the labels

        print(f"Flattened X: {X_flat}")
        print(f"Flattened y: {y_flat}")

        # Train model
        self.pattern_predictor.train_model(X_flat, y_flat)
        print("Model trained.")  # Debugging output

        # Predict the next item
        prediction = self.pattern_predictor.predict_next(numeric_sequence)
        print(f"Predicted next item (numeric): {prediction}")  # Debugging output

        # Since prediction is a single value, no need to iterate, map it directly
        number_to_element = {v: k for k, v in element_to_number.items()}
        prediction_original = number_to_element[int(prediction)]
        print(f"Predicted next item (original): {prediction_original}")  # Debugging output

        # Display prediction
        self.ui.display_prediction(prediction_original)

if __name__ == "__main__":
    app = MainApp()
    app.run()