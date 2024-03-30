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


class Segment:
    """
    Class representing segment in plane
    """

    one_intersection = None

    def __init__(self, point_1, point_2):
        """
        Sets all the necessary attributes for the class Segment
        :param point_1: coordinates of the first point
        :param point_2: coordinates of the second point
        """

        self.point_1 = point_1
        self.point_2 = point_2


class CoordinateSystem:
    """
    Class representing Euclidean plane
    """

    segments = []

    def add_segment(self, segment):
        """
        Method adding new segment
        :param segment: two point of the segment
        :return: None
        """
        CoordinateSystem.segments.append(segment)

    def axis_intersection(self):
        """
        Method of calculation amount of segments intersecting only one axis
        :return: amount of segments intersecting only one axis
        """

        count = 0

        for item in CoordinateSystem.segments:
            a_x, a_y = item.point_1.get_x(), item.point_1.get_y()
            b_x, b_y = item.point_2.get_x(), item.point_2.get_y()

            if a_x > 0:
                if a_y > 0:
                    if not (b_x < 0 and b_y < 0):
                        count += 1
                elif a_y < 0:
                    if not (b_x < 0 and b_y > 0):
                        count += 1
            elif a_x < 0:
                if a_y > 0:
                    if not (b_x > 0 and b_y < 0):
                        count += 1
                elif a_y < 0:
                    if not (b_x > 0 and b_y > 0):
                        count += 1
        return count
