VOWELS = "aeiou"


class Chat:
    def __init__(self):
        self.dialogue = []

    def connect_human(self, human):
        human.set_mediator(self)

    def connect_robot(self, bot):
        bot.set_mediator(self)

    def show_human_dialogue(self):
        text = []
        for message in self.dialogue:
            text.append(f'{message[0]} said: {message[1]}')
        return '\n'.join(text)

    def show_robot_dialogue(self):
        text = []
        for message in self.dialogue:
            comp_text = ''
            for letter in message[1]:
                if letter.lower() in VOWELS:
                    comp_text += '0'
                else:
                    comp_text += '1'
            text.append(f'{message[0]} said: {comp_text}')
        return '\n'.join(text)

    def send(self, who, text):
        self.dialogue.append([who, text])


class Human:
    def __init__(self, name, mediator: Chat = None):
        self.name = name
        self._mediator = mediator

    def set_mediator(self, mediator):
        self._mediator = mediator

    def send(self, text):
        self._mediator.send(who=self.name, text=text)


class Robot:
    def __init__(self, serial_number, mediator: Chat = None):
        self.serial_number = serial_number
        self._mediator = mediator

    def set_mediator(self, mediator):
        self._mediator = mediator

    def send(self, text):
        self._mediator.send(who=self.serial_number, text=text)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

    print("Coding complete? Let's try tests!")
