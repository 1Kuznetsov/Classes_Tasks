class NotSleeping:
    """
    Class representing a person who is struggling to fall asleep.
    """

    def __init__(self):
        """
        Sets all the necessary attributes for the class NotSleeping
        Initial count_sheeps is 0
        """

        self.count_sheeps = 0

    def add_sheep(self):
        """
        Method to count sheep to help fall asleep.
        :return: None
        """

        self.count_sheeps += 1
