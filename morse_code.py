"""
12 de septiembre 2021
MorseCode class
Converts text to Morse Code
"""



class MorseCode():
    def __init__(self):
        self.morse_message=[]
        self.morse_code = {
            "a": [".", "-"],
            "b": ["-", ".", ".", "."],
            "c": ["-", ".", "-", "."],
            "d": ["-", ".", "."],
            "e": ["."],
            "f": [".", ".", "-", "."],
            "g": ["-", "-", "."],
            "h": [".", ".", ".", "."],
            "i": [".", "."],
            "j": [".", "-", "-", "-"],
            "k": ["-", ".", "-"],
            "l": [".", "-", ".", "."],
            "m": ["-", "-"],
            "n": ["-", "."],
            "o": ["-", "-", "-"],
            "p": [".", "-", "-", "."],
            "q": ["-", "-", ".", "-"],
            "r": [".", "-", "."],
            "s": [".", ".", "."],
            "t": ["-"],
            "u": [".", ".", "-"],
            "v": [".", ".", ".", "-"],
            "w": [".", "-", "-"],
            "x": ["-", ".", ".", "-"],
            "y": ["-", ".", "-", "-"],
            "z": ["-", "-", ".", "."],
            "1": [".", "-", "-", "-", "-"],
            "2": [".", ".", "-", "-", "-"],
            "3": [".", ".", ".", "-", "-"],
            "4": [".", ".", ".", ".", "-"],
            "5": [".", ".", ".", ".", "."],
            "6": ["-", ".", ".", ".", "."],
            "7": ["-", "-", ".", ".", "."],
            "8": ["-", "-", "-", ".", "."],
            "9": ["-", "-", "-", "-", "."],
            "0": ["-", "-", "-", "-", "-"],
            " ": ["/"],
        }

    def to_morse_code(self,the_message: str) -> list :
        """
        Return a list with the morse code of the text
        :param the_message: the text to convert
        :return: a Morse Code list
        """
        self.morse_message=[]
        the_message=the_message.lower()
        morse_message=[]
        for letter in the_message:
            if letter in self.morse_code:
                for ditdash in self.morse_code[letter]:
                    self.morse_message.append(ditdash)
            else:
                print(f"error for {letter}")
        return self.morse_message
