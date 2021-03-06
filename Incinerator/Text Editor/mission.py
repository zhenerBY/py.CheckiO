class Text:
    def __init__(self, text='', font=None):
        self.text = text
        self.font = font

    def write(self, text):
        self.text += text

    def set_font(self, font):
        self.font = font

    def show(self):
        if self.font is None:
            return self.text
        return f'[{self.font}]{self.text}[{self.font}]'

    def restore(self, saved):
        self.text = saved[0]
        self.font = saved[1]


class SavedText:
    def __init__(self):
        self.counter = 0
        self.mem = {}

    def save_text(self, text: Text):
        self.mem[self.counter] = [text.text, text.font]
        self.counter += 1

    def get_version(self, number):
        return self.mem[number]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")
