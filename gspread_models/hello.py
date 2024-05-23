


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
