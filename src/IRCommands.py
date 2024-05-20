class IRCommands(object):
    """
    A class that represents a collection of IR commands.

    Attributes:
        CmdDict (dict): A dictionary that maps commands to functions.
    """

    def __init__(self):
        """
        Initializes a new instance of the IRCommands class.
        """
        self.CmdDict = {}

    def addCommand(self, command, name, function):
        """
        Adds a command and its corresponding function to the CmdDict.

        Args:
            command (str): The command to be added.
            name (str): The name of the command.
            function (function): The function to be associated with the command.
        """
        self.CmdDict[command] = [name, function]

    def execCommand(self, command):
        """
        Executes the function associated with the given command.

        Args:
            command (str): The command to be executed.

        Raises:
            KeyError: If the command is not found in the CmdDict.
        """
        if command in self.CmdDict:
            print("Executing " + self.CmdDict[command][0])
            function = self.CmdDict[command][1]
            function()
        else:
            raise KeyError("Command not found.")
        
    def count(self):
        """
        Returns the number of commands in the CmdDict.

        Returns:
            int: The number of commands in the CmdDict.
        """
        return len(self.CmdDict)
    
    def __str__(self):
        """
        Returns a string representation of the IRCommands object.

        Returns:
            str: A string representation of the IRCommands object.
        """
        return "\n".join([" ".join([key, self.CmdDict[key][0], self.CmdDict[key][1].__name__]) for key in self.CmdDict.keys()])

def function1():
    """
    Function that represents command1.

    Example:
        function1()
    """
    print("Executing function1")

def function2():
    """
    Function that represents command2.

    Example:
        function2()
    """
    print("Executing function2")

def function3():
    """
    Function that represents command3.

    Example:
        function3()
    """
    print("Executing function3")

def main():
    """
    The main function of the program.

    Creates an instance of IRCommands, adds commands and their corresponding functions,
    and executes a command.

    Example:
        ir_commands = IRCommands()
        ir_commands.addCommand("command1", "name1", function1)
        ir_commands.addCommand("command2", "name2", function2)
        ir_commands.addCommand("command3", "name3", function3)
        ir_commands.execCommand("command1")
    """
    # Create an instance of IRCommands
    ir_commands = IRCommands()

    # Add commands and their corresponding functions
    ir_commands.addCommand("command1", "name1", function1)
    ir_commands.addCommand("command2", "name2", function2)
    ir_commands.addCommand("command3", "name3", function3)

    # Execute a command
    try:
        ir_commands.execCommand("command1")
    except KeyError as e:
        print(str(e))

if __name__ == "__main__":
    main()