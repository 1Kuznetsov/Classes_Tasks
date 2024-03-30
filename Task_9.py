class StrandsDNA:
    """
    Class representing chains of DNA
    """

    all_strands = []

    def add_strands(self, strands):
        """
        Method of adding new strands without repeating
        :param strands: string of chains
        :return: None
        """

        new_strands = strands.split()
        for chain in new_strands:
            if chain not in StrandsDNA.all_strands:
                StrandsDNA.all_strands.append(chain)

    def get_max_strands(self):
        """
        Method of determination string with max length
        :return: string of chains with max length
        """

        if len(StrandsDNA.all_strands) == 0:
            return ''

        max_length = max(len(strand) for strand in StrandsDNA.all_strands)
        max_strands = [strand for strand in StrandsDNA.all_strands if len(strand) == max_length]
        max_strands.sort()

        return ' '.join(max_strands)
