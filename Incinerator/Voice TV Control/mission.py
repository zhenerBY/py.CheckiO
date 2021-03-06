class VoiceCommand:
    def __init__(self, channels: list):
        self.channels = channels
        self._position = 1

    def first_channel(self):
        self._position = 1
        return self.current_channel()

    def last_channel(self):
        self._position = len(self.channels)
        return self.current_channel()

    def turn_channel(self, n):
        self._position = n
        return self.current_channel()

    def next_channel(self):
        self._position = self._position + 1 if self._position < len(self.channels) else 1
        return self.current_channel()

    def previous_channel(self):
        self._position = self._position - 1 if self._position > 2 else len(self.channels)
        return self.current_channel()

    def current_channel(self):
        return self.channels[self._position - 1]

    def is_exist(self, n):
        if n in self.channels:
            return 'Yes'
        return 'No'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)

    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"
    print("Coding complete? Let's try tests!")
