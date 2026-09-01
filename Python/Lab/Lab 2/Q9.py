"""9.A software application contains configuration information that should not be accidentally modified during program
execution.
Example information may include:
=> Application name
=> Version
=> Supported environments
=> Database configuration
Design a suitable data structure for storing information that should remain unchanged.Requirement: Explain why
your selected structure is preferable to a mutable alternative and demonstrate what happens when an attempt is
made to modify it"""

# Here we can make use of tuple. Tuple is immutable. 
# Tuple is suitable because it prevents any changes in it. So if we preserve cofiguration info that should not be changed during program exection, the only option is preserving the info in tuple. 
# If we try to modify a tuple, it will not execute futher and will generate an error

tup = ("Python", "3.14.7", "VS Code", "None")