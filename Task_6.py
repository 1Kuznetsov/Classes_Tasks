class Point:
    """
    Class representing a point on the plane
    """

    def __init__(self, coord=(0, 0)):
        """
        Sets all the necessary attributes for the class Point
        :param coord: coordinates of the point
        """

        self.coord = coord

    def get_x(self):
        """
        Method of getting the x coordinate of the point
        :return: x-axis coordinate
        """

        return self.coord[0]

    def get_y(self):
        """
        Method of getting the y coordinate of the point
        :return: y-axis coordinate
        """

        return self.coord[1]

    def distance(self, other):
        """
        Method of calculating the distance betwixt two points
        :param other: coordinates of another point
        :return: distance betwixt two points
        """

        dist_x = (other[0] - self.coord[0]) ** 2
        dist_y = (other[1] - self.coord[1]) ** 2
        return (dist_x + dist_y) ** 0.5

    def sum(self, other):
        """
        Method of getting new point by summarizing coordinates of the two points
        :param other: coordinates of another point
        :return: new point
        """

        new_x = self.coord[0] + other[0]
        new_y = self.coord[1] + other[1]
        return Point((new_x, new_y))

    def __repr__(self):
        """
        Method that represents data
        :return: formatted data
        """
        return f'This point has following coordinates: x={self.coord[0]}, y={self.coord[1]}'
