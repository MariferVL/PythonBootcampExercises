""" 1 """
# """ MRO """
# C3 Linearization Algorithm works on three rules:
        # + Inheritance graph determines the structure of method resolution order.
        # + User have to visit the super class only after the method of the local classes are visited.
        # + Monotonicity
# To get the MOR:  __mro__ attribute or mro() method    
# display the order in which methods are resolved. 
# For Example:
        # print((class name).__mro__) → User.__mro__
        # print((class name).mro())

""" 2 """
# """ Polymorphism """
        # means having many forms. 
        # In programming, polymorphism means the same function name (but different signatures) 
        # being used for different types.

""" 3 """
# """ isinstance() & issubclass() """
        # Cube--> child  & Square --> Parent
        # isinstance(Cube, Square) → return True    

""" 4 """
#""" BaseException """
        # SyntaxError: invalid syntax:
                # Syntax errors, aka parsing errors. Most common in the learning process.
                # When the proper syntax of the language is not followed then a syntax error is thrown. 
                # The error is caused by (or at least detected at) the token preceding an arrow.

        # Exception: logical errors.
                # occurs after passing the syntax test.
                # Types: 
                        # IOError: if the file can’t be opened
                        # KeyboardInterrupt: when an unrequired key is pressed by the user
                        # ValueError: when built-in function receives a wrong argument
                        # EOFError: if End-Of-File is hit without reading any data
                        # ImportError: if it is unable to find the module (not found)
                        # ZeroDivisionError: division by zero
                        # IndentationError: expected an indented block
                        # IndexError: When the wrong index of a list is retrieved.
                        # AssertionError: It occurs when the assert statement fails
                        # AttributeError: It occurs when an attribute assignment is failed.
                        # KeyError: It occurs when the key of the dictionary is not found.
                        # NameError: It occurs when the variable is not defined.
                        # MemoryError: It occurs when a program runs out of memory.
                        # TypeError: It occurs when a function and operation are applied in an incorrect type.

""" 5 """
# """ Benefits of handling errors """
        # Errors are the problems in a program due to which the program will stop the execution. 
        # On the other hand, exceptions are raised when some internal events occur which changes
        #   the normal flow of the program.
        # When an error and an exception are raised then we handle that with the help of the Handling method.
        # Exception handling in Python not only provides a way to respond to errors, 
        #   it allows you to elegantly structure your code and solve problems,
        #   reduces code, and sometimes speeds up your script.
        # We can handle errors by the Try/Except/Finally method. 
        #   We write unsafe code in the try, fall back code in except and final code in finally block.
