class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name, description, function):
        self.tools[name] = {
            "description": description,
            "function": function,
        }

    def list_tools(self):
        return self.tools
