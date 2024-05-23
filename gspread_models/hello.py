


class Hello:
    def __init__(self):
        """yeup yup yup"""
        self.message = "hello"

    def announce(self, location:str) -> str:
        """Announcement 1
        """
        return f"hello, we are visiting {location}"


    def departing(self, location:str) -> str:
        """
        Departing

        This is some text.

            Indended one

                Indented two
        """
        return f"hello, we are leaving {location}"



class MyClass:
    """
    This is an example class.

    Attributes
    ----------
    attr1 : str
        Description of attribute `attr1`.
    attr2 : int
        Description of attribute `attr2`.

    Methods
    -------
    my_method(param1, param2)
        Description of `my_method`.
    """

    def __init__(self, attr1: str, attr2: int):
        """
        Parameters
        ----------
        attr1 : str
            Description of parameter `attr1`.
        attr2 : int
            Description of parameter `attr2`.
        """
        self.attr1 = attr1
        self.attr2 = attr2

    def my_method(self, param1: str, param2: int) -> str:
        """
        Description of method `my_method`.

        Parameters
        ----------
        param1 : str
            Description of parameter `param1`.
        param2 : int
            Description of parameter `param2`.

        Returns
        -------
        str
            Description of return value.
        """
        return f"{param1} {param2}"
