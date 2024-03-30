class Dog:
    """
    Class representing a dog animal saying woof
    """

    def __init__(self, name):
        """
        Sets all the necessary attributes for the class Dog
        :param name: name of dog
        """

        self.name = name

    def say(self):
        """
        Saying woof
        :return:None
        """

        print('Гав!')
