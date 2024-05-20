import unittest
from unittest.mock import patch
from IRCommands import IRCommands

class TestIRCommands(unittest.TestCase):
    def setUp(self):
        self.ir_commands = IRCommands()

    def test_addCommand(self):
        self.ir_commands.addCommand("command1", "cmd1", self.function1)
        self.ir_commands.addCommand("command2", "cmd2", self.function2)
        self.ir_commands.addCommand("command3", "cmd3", self.function3)

        self.assertEqual(len(self.ir_commands.CmdDict), 3)
        self.assertEqual(self.ir_commands.CmdDict["command1"][1], self.function1)
        self.assertEqual(self.ir_commands.CmdDict["command2"][1], self.function2)
        self.assertEqual(self.ir_commands.CmdDict["command3"][1], self.function3)

    def test_execCommand(self):
        self.ir_commands.addCommand("command1", "cmd1", self.function1)
        self.ir_commands.addCommand("command2", "cmd2", self.function2)
        self.ir_commands.addCommand("command3", "cmd3", self.function3)

        print(self.ir_commands.count(), " commands added")
        print (self.ir_commands)

        with patch('builtins.print') as mock_print:
            self.ir_commands.execCommand("command1")
            mock_print.assert_called_with("Executing function1")

            self.ir_commands.execCommand("command2")
            mock_print.assert_called_with("Executing function2")

            self.ir_commands.execCommand("command3")
            mock_print.assert_called_with("Executing function3")

    def test_execCommand_keyError(self):
        with self.assertRaises(KeyError):
            self.ir_commands.execCommand("invalid_command")

    def function1(self):
        print("Executing function1")

    def function2(self):
        print("Executing function2")

    def function3(self):
        print("Executing function3")

if __name__ == "__main__":
    unittest.main()