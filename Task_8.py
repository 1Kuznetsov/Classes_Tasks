class MorseMsg:
    """
    Class representing message written in Morse code
    """

    def __init__(self, ptr):
        """
        Sets all the necessary attributes for the class MorseMsg
        :param ptr: string written in Morse code
        """

        self.ptr = ptr.split()

    def eng_decode(self):
        """
        Method of translation message written in Morse code to english message
        :return: decoded english message
        """

        morse_code_eng = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..'
        }
        decoded = ''

        for letter in self.ptr:
            for key, value in morse_code_eng.items():
                if letter == value:
                    decoded += key

        return decoded

    def ru_decode(self):
        """
        Method of translation message written in Morse code to russian message
        :return: decoded russian message
        """

        morse_code_ru = {
            'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ё': '.', 'Ж': '...-', 'З': '--..',
            'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.',
            'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----',
            'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'
        }
        decoded_ru = ''

        for letter in self.ptr:
            for key, value in morse_code_ru.items():
                if letter == value:
                    decoded_ru += key
                    break

        return decoded_ru

    def get_vowels(self, lang):
        """
        Method of getting vowels in message written in Morse code and decoded in lang
        :param lang: language for decoding message
        :return: list of vowels
        """

        vowels_eng = ['A', 'E', 'I', 'O', 'U']
        vowels_ru = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
        vowels = []

        if lang == 'eng':
            decoded = self.eng_decode()
            for letter in decoded:
                if letter in vowels_eng:
                    vowels.append(letter)

        elif lang == 'ru':
            decoded = self.ru_decode()
            for letter in decoded:
                if letter in vowels_ru:
                    vowels.append(letter)

        return vowels

    def get_consonants(self, lang):
        """
        Method of getting consonants in message written in Morse code and decoded in lang
        :param lang: language for decoding message
        :return: list of consonants
        """

        consonants_eng = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X',
                          'Y', 'Z']
        consonants_ru = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш',
                         'Щ']
        consonants = []

        if lang == 'eng':
            decoded = self.eng_decode()
            for letter in decoded:
                if letter in consonants_eng:
                    consonants.append(letter)

        elif lang == 'ru':
            decoded = self.ru_decode()
            for letter in decoded:
                if letter in consonants_ru:
                    consonants.append(letter)

        return consonants
