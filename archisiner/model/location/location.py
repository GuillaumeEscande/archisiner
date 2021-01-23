"""
Define the location concept
"""


class Location():
    """
    Define the location concept
    """
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        """ Getter of name """
        return self.__name
