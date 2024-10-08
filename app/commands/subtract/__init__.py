from app.commands import Command


class SubtractCommand(Command):
    def subtract():
        numbers = input("Enter two space-separated numbers: ")
        num1, num2 = map(int, numbers.split())
        result = num1 - num2
        return result

    def execute(self):
        print("Subtraction result:", SubtractCommand.subtract())
        