class Game:
    """
    Class representing basketball game
    """

    def __init__(self, teams):
        """
        Sets all the necessary attributes for the class Game
        :param teams:
        """

        self.teams = teams

    def ball_thrown(self, command, points):
        """
        Method of adding points
        :param command:
        :param points:
        :return:
        """

        self.teams[command] += points

    def get_score(self):
        """
        Method showing the score of teams
        :return:
        """

        return tuple(self.teams.values())

    def get_winner(self):
        """
        Method of determination the winner
        :return: command that won the game or tie if there are no winner
        """

        max_val = max(self.teams.values())
        cnt = list(self.teams.values()).count(max_val)

        if cnt > 1:
            return 'Tie'
        else:
            ind = list(self.teams.values()).index(max_val)
            return list(self.teams.keys())[ind]
