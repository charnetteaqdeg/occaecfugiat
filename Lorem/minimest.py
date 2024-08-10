def example_function(arg=None):
    if arg is not None:
        print(f"Аргумент передан: {arg}")
    else:
        print("Аргумент не передан.")

example_function()  # Output: "Аргумент не передан."
example_function('test')  # Output: "Аргумент передан: test"
