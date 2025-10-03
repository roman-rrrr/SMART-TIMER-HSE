import os
import time
from time import localtime

stop_flag = False
now = [None, 0, 0]


def format_time(seconds):
    seconds = int(seconds)
    minutes = seconds // 60
    seconds = seconds % 60
    if minutes == 0:
        return f"{seconds} сек"
    return f"{minutes} мин {seconds} сек"


def send_status():
    global now
    if now[0] is not None:
        if now[0] == "work":
            return {
                "1": ["Вы работаете уже: ", format_time(now[1])],
                "2": ["До перерыва осталось: ", format_time(now[2])],
                "3": "Не отвлекайтесь на телефон!",
            }
        else:
            return {
                "1": ["Вы отдыхаете уже: ", format_time(now[1])],
                "2": ["До работы осталось: ", format_time(now[2])],
                "3": "тут будет полезная ссылка",
            }


def run_timer(_1, _2, _3, _4):
    global stop_flag, now
    stop_flag = False

    now = localtime()
    local_time = (
        now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec
    )  # текущее время в секундах

    new1 = [int(i) for i in _1.split(":")]  # до скольки можете работать
    hours1 = new1[0]
    minutes1 = new1[1]
    if len(str(minutes1)) and str(minutes1)[0] == "0":
        minutes1 = int(str(minutes1)[1])
    if len(str(hours1)) and str(hours1)[0] == "0":
        hours1 = int(str(hours1)[1])

    _5 = hours1 * 60 * 60 + minutes1 * 60  # до скольки можете работать в секундах

    work_time = _5 - local_time

    work_without_timeout = int(_2) * 60
    little_timeout = int(_3) * 60
    long_timeout = int(_4) * 60

    done = 0
    accounting = ""

    now = ["work", 0, work_without_timeout]

    while not (done > work_time):
        if stop_flag:
            print("Таймер остановлен.")
            return
        if accounting.count("ab") == 3:
            for s in range(0, work_without_timeout + 1):
                if done + 1 > work_time:
                    print(f"Время работы истекло! Вы продуктивно работали {done} сек.")
                    os.system("afplay Время_истекло.mp3")
                if s != 0:
                    print(
                        f"Вы работаете уже: {s} сек. Осталось до следущего отдыха {work_without_timeout - s} сек."
                    )
                    done += 1
                    now = ["work", s, work_without_timeout - s]
                time.sleep(1)
            accounting += "a"
            print("Пора сделать длинный перерыв!")
            os.system("afplay Длинный.mp3")
            for s in range(0, long_timeout + 1):
                if done + 1 > work_time:
                    print(f"Время работы истекло! Вы продуктивно работали {done} сек.")
                    os.system("afplay Время_истекло.mp3")
                if s != 0:
                    print(
                        f"Вы отдыхаете уже: {s} сек. До работы осталось {long_timeout - s} сек."
                    )
                    done += 1
                    now = ["chill", s, long_timeout - s]
                time.sleep(1)
            accounting = ""
            print("Пора возвращаться к работе((")
            os.system("afplay Пора_возвращаться_к_работе.mp3")
        else:
            for s in range(0, work_without_timeout + 1):
                if done + 1 > work_time:
                    print(f"Время работы истекло! Вы продуктивно работали {done} сек.")
                    os.system("afplay Время_истекло.mp3")
                if s != 0:
                    print(
                        f"Вы работаете уже: {s} сек. Осталось до следущего отдыха {work_without_timeout - s} сек."
                    )
                    done += 1
                    now = ["work", s, work_without_timeout - s]
                time.sleep(1)
            accounting += "a"
            print("Пора сделать короткий перерыв!")
            os.system("afplay Короткий.mp3")
            for s in range(0, little_timeout + 1):
                if done + 1 > work_time:
                    print(f"Время работы истекло! Вы продуктивно работали {done} сек.")
                    os.system("afplay Время_истекло.mp3")
                if s != 0:
                    print(
                        f"Вы отдыхаете уже: {s} сек. До работы осталось {little_timeout - s} сек."
                    )
                    done += 1
                    now = ["chill", s, little_timeout - s]
                time.sleep(1)
            accounting += "b"
            print("Пора возвращаться к работе((")
            os.system("afplay Пора_возвращаться_к_работе.mp3")

