class TrafficLight:
    """
    Class representing a traffic light
    """

    permissible_values = ['green', 'yellow', 'red']

    def __init__(self):
        """
        Sets all the necessary attributes for the class TrafficLight
        """

        self.current_signal = 'green'
        self.index = 0

    def next_signal(self):
        """
        Method of changing the color of traffic light to next one
        :return: None
        """

        if self.index < len(TrafficLight.permissible_values) - 1:
            self.index += 1

        else:
            self.index = (self.index + 2) % 3
            TrafficLight.permissible_values = TrafficLight.permissible_values[-1::-1]

        self.current_signal = TrafficLight.permissible_values[self.index]

    def __repr__(self):
        """
        Method that represents data
        :return: current color of traffic light
        """
        return self.current_signal
