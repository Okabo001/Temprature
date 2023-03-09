class Temperature:
    @staticmethod
    def convert_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit and print the result."""
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

    @staticmethod
    def convert_celsius(fahrenheit):
        """Convert Fahrenheit to Celsius and print the result."""
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
        temp = Temperature()
        temp.convert_fahrenheit(25)  # Output: 25 degrees Celsius is equal to 77.0 degrees Fahrenheit.
        temp.convert_celsius(75)
        # Output: 75 degrees Fahrenheit is equal to 23.88888888888889 degrees Celsius.