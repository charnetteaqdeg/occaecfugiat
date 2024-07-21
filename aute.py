    class CoreNormalizer(SpecMapper):
        def __init__(self):
            super().__init__()  # Call the constructor of the parent class (SpecMapper)
            # Additional initialization code for CoreNormalizer

        def normalize(self, data):
            # Method to normalize data
            print(f'Normalizing data in CoreNormalizer: {data}')

        # Optionally override methods from the parent class
        def map_spec(self, spec):
            # Custom implementation for mapping a specification
            print(f'Mapping spec in CoreNormalizer: {spec}')
    