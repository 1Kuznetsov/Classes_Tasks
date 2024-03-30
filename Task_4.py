class User:
    """
    Class representing data about user
    """

    def __init__(self, id, nick_name, first_name, last_name, middle_name, gender):
        """
        Sets all the necessary attributes for the class User
        :param id:
        :param nick_name:
        :param first_name:
        :param last_name:
        :param middle_name:
        :param gender:
        """

        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self, new_nick_name=None, new_first_name=None, new_last_name=None,
               new_middle_name=None, new_gender=None):
        """
        Method of updating data, requires name parameters
        :param new_nick_name:
        :param new_first_name:
        :param new_last_name:
        :param new_middle_name:
        :param new_gender:
        :return:
        """

        if new_nick_name:
            self.nick_name = new_nick_name
        if new_first_name:
            self.first_name = new_first_name
        if new_last_name:
            self.last_name = new_last_name
        if new_middle_name:
            self.middle_name = new_middle_name
        if new_gender:
            self.gender = new_gender

    def __repr__(self):
        """
        Method that represents data
        :return: formatted data
        """

        return f' Information about user: \n id: {self.id} \n nick_name: {self.nick_name}\n ' \
               f'first_name: {self.first_name} \n last_name: {self.last_name} \n ' \
               f'middle_name: {self.middle_name} \n gender: {self.gender} \n '
