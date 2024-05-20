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

    def addCommand(self, command, function):
        """
        Adds a command and its corresponding function to the CmdDict.

        Args:
            command (str): The command to be added.
            function (function): The function to be associated with the command.
        """
        self.CmdDict[command] = function

    def execCommand(self, command):
        """
        Executes the function associated with the given command.

        Args:
            command (str): The command to be executed.

        Raises:
            KeyError: If the command is not found in the CmdDict.
        """
        if command in self.CmdDict:
            function = self.CmdDict[command]
            function()
        else:
            raise KeyError("Command not found.")
