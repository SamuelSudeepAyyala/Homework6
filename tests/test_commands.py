import pytest
from app import App
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand


def test_add_command(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5 3')
    command = AddCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Additon result: 8" in out, "The AddCommand should print the correct addition result."

def test_subtract_command(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5 3')
    command = SubtractCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Subtraction result: 2" in out, "The SubtractCommand should print the correct subtraction result."

def test_multiply_command(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5 3')
    command = MultiplyCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Multiplication result: 15" in out, "The MultiplyCommand should print the correct multiplication result."

def test_divide_command(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '9 3')
    command = DivideCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Division result: 3" in out, "The DivideCommand should print the correct division result."

def test_dividebyzero_command(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '9 0')
    command = DivideCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Error Occured! DivisionByzero or DivisionByNegative" in out, "Error should be Occured."

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"


