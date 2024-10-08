from app.commands import Command


class MultiplyCommand(Command):
    def multiply():
        numbers = input("Enter two space-separated numbers: ")
        num1, num2 = map(int, numbers.split())
        result = num1 * num2
        return result

    def execute(self):
        print("Multiplication result:", MultiplyCommand.multiply())
        