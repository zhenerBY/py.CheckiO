from datetime import datetime


def date_time(time: str) -> str:
    # replace this for solution
    date = datetime.strptime(time, '%d.%m.%Y %H:%M').strftime('%d %B %Y year %H hours %M minutes')
    if date[0] == '0':
        date = date[1:]
    if date[-19] == '0':
        date = date[:-19] + date[-18:]
    if int(date[-19:-17]) == 1:
        date = date.replace('hours', 'hour')
    if date[-10] == '0':
        date = date[:-10] + date[-9:]
    if int(date[-9:-7]) == 1:
        date = date.replace('minutes', 'minute')
    return date


if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
            date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
            date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
            date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
