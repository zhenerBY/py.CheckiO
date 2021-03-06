class HackerLanguage:
    def __init__(self):
        self.text = ''

    def write(self, text):
        self.text += text

    def delete(self, count):
        self.text = self.text[:-count]

    def send(self):
        newtext = ''
        for letter in self.text:
            if letter.isalpha():
                newtext += str(bin(ord(letter))[2:])
            elif letter == ' ':
                newtext += '1000000'
            else:
                newtext += letter
        return newtext

    def read(self, text):
        counter = 0
        newtext = ''
        while counter < len(text):
            if text[counter:counter + 7] == '1000000':
                newtext += ' '
                counter += 7
            elif text[counter:counter + 7].isdigit():
                newtext += chr(int(text[counter:counter + 7], 2))
                counter += 7
            else:
                newtext += text[counter]
                counter += 1
        return newtext


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"
    print("Coding complete? Let's try tests!")
