from datetime import datetime


class MicrowaveBase:
    def __init__(self):
        self.time = 0

    def set_time(self, string):
        self.time = int(string[:2]) * 60 + int(string[-2:])

    def add_time(self, string):
        if string[-1] == 's':
            self.time += int(string[:-1])
            if self.time > 90 * 60:
                self.time = 90 * 60
        if string[-1] == 'm':
            self.time += int(string[:-1]) * 60
            if self.time > 90 * 60:
                self.time = 90 * 60

    def del_time(self, string):
        if string[-1] == 's':
            self.time -= int(string[:-1])
            if self.time < 0:
                self.time = 0
        if string[-1] == 'm':
            self.time -= int(string[:-1]) * 60
            if self.time < 0:
                self.time = 0

    def show_time(self):
        return str(self.time // 60).rjust(2, '0') + ':' + str(self.time % 60).rjust(2, '0')


class Microwave1(MicrowaveBase):
    def show_time(self):
        text = super().show_time()
        return '_' + text[1:]


class Microwave2(MicrowaveBase):
    def show_time(self):
        text = super().show_time()
        return text[:-1] + '_'


class Microwave3(MicrowaveBase):
    pass


class RemoteControl:
    def __init__(self, mw: MicrowaveBase):
        self.instance = mw

    def __getattr__(self, item):
        return getattr(self.instance, item)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")

    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")

    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"
    print("Coding complete? Let's try tests!")
