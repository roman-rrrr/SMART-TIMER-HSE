import time
import threading
from time import localtime
from playsound import playsound

lock = threading.Lock()
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
    with lock:
        if now[0] is not None:
            if now[0] == 'work':
                return {
                    "1": ["Вы работаете уже: ", format_time(now[1])],
                    "2": ["До перерыва осталось: ", format_time(now[2])],
                    "3": "Не отвлекайтесь на телефон!"
                }
            elif now[0] == 'chill':
                return {
                    "1": ["Вы отдыхаете уже: ", format_time(now[1])],
                    "2": ["До работы осталось: ", format_time(now[2])],
                    "3": "тут будет полезная ссылка"
                }
        else:
            return None

def run_timer(_1, _2, _3, _4):
    global stop_flag, now
    with lock:
        stop_flag = False
        now = [None, 0, 0]

    now_time = localtime()
    local_time = now_time.tm_hour * 3600 + now_time.tm_min * 60 + now_time.tm_sec

    hours1, minutes1 = [int(i) for i in _1.split(":")]
    goal_time = hours1 * 60 * 60 + minutes1 * 60
    work_time = goal_time - local_time

    work_without_timeout = int(_2) * 60
    little_timeout = int(_3) * 60
    long_timeout = int(_4) * 60

    done = 0
    accounting = "s"
    while done < work_time:
        if accounting.count("ab") == 3:
            # НАЧАЛО РАБОТЫ
            playsound("back_to_work.mp3")
            for s in range(1, work_without_timeout + 1):
                with lock:
                    if stop_flag:
                        now = [None, 0, 0]
                        return
                    now = ['work', s, work_without_timeout - s]
                done += 1
                time.sleep(1)
                if done >= work_time:
                    break
            accounting += "a"
            # НАЧАЛО ДЛИННОГО ПЕРЕРЫВА
            playsound("long.mp3")
            for s in range(1, long_timeout + 1):
                with lock:
                    if stop_flag:
                        now = [None, 0, 0]
                        return
                    now = ['chill', s, long_timeout - s]
                done += 1
                time.sleep(1)
                if done >= work_time:
                    break
            accounting = ""
        else:
            # НАЧАЛО РАБОТЫ
            if accounting != "s":
                playsound("back_to_work.mp3")
            for s in range(1, work_without_timeout + 1):
                with lock:
                    if stop_flag:
                        now = [None, 0, 0]
                        return
                    now = ['work', s, work_without_timeout - s]
                done += 1
                time.sleep(1)
                if done >= work_time:
                    break
            accounting += "a"
            # НАЧАЛО КОРОТКОГО ПЕРЕРЫВА
            playsound("short.mp3")
            for s in range(1, little_timeout + 1):
                with lock:
                    if stop_flag:
                        now = [None, 0, 0]
                        return
                    now = ['chill', s, little_timeout - s]
                done += 1
                time.sleep(1)
                if done >= work_time:
                    break
            accounting += "b"
    # ЗАВЕРШЕНИЕ РАБОТЫ
    playsound("time_end.mp3")
    with lock:
        now = [None, 0, 0]