from time import localtime

def format_time(seconds):
    seconds = int(seconds)
    minutes = seconds // 60
    seconds = seconds % 60
    if minutes == 0:
        return f"{seconds} сек"
    return f"{minutes} мин {seconds} сек"


def run_timer(_1, _2, _3, _4):
    global stop_flag, now
    stop_flag = False

    now = localtime()  # текущее время у пользователя формата (h:m:s)
    local_time = (now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec)  # текущее время в секундах

    new1 = [int(i) for i in _1.split(":")]
    hours1 = new1[0]  # до скольки часов готов работать
    minutes1 = new1[1]  # до скольки минут готов работать

    goal_time = hours1 * 60 * 60 + minutes1 * 60  # до скольки можете работать в секундах

    work_time = goal_time - local_time  # СКОЛЬКО ПОЛЬЗОВАТЕЛЬ ГОТОВ РАБОТАТЬ В СЕК

    work_without_timeout = int(_2) * 60 #в сек
    little_timeout = int(_3) * 60 #в сек
    long_timeout = int(_4) * 60 #в сек

    done = 0
    accounting = ""
    
    now = ["work", 0, work_without_timeout]

    while (not (done > work_time)):
        if stop_flag:
            print("Таймер остановлен.")
            return
        if accounting.count("ab") == 3:
            for s in range(0, work_without_timeout + 1):
                if done + 1 > work_time:
                    print(f"Время работы истекло! Вы продуктивно работали {done} сек.")
                    #(f"Время работы истекло! Вы продуктивно работали {done} сек.")
                if s != 0:
                    print(f"Вы работаете уже: {s} сек. Осталось до следущего отдыха {work_without_timeout - s} сек.")
                    done += 1
                    now = ['work', s, work_without_timeout - s]
                    #send_status()
                    # (f"Вы работаете уже: {s} сек. Осталось до следущего отдыха {work_without_timeout - s} сек.")
                time.sleep(1)
            accounting += "a"
            print("Пора сделать длинный перерыв!")
            for s in range(0, long_timeout + 1):
                if done + 1 > work_time:
                    print(f"Время работы истекло! Вы продуктивно работали {done} сек.")
                    #(f"Время работы истекло! Вы продуктивно работали {done} сек.")
                if s != 0:
                    print(f"Вы отдыхаете уже: {s} сек. До работы осталось {long_timeout - s} сек.")
                    done += 1
                    now = ['chill', s, long_timeout - s]
                    #(f"Вы отдыхаете уже: {s} сек. До работы осталось {long_timeout - s} сек.")
                time.sleep(1)
            accounting = ""
            print("Пора возвращаться к работе((")
        else:
            for s in range(0, work_without_timeout + 1):
                if done + 1 > work_time:
                    print(f"Время работы истекло! Вы продуктивно работали {done} сек.")
                    #(f"Время работы истекло! Вы продуктивно работали {done} сек.")
                if s != 0:
                    print(f"Вы работаете уже: {s} сек. Осталось до следущего отдыха {work_without_timeout - s} сек.")
                    done += 1
                    now = ['work', s, work_without_timeout - s]
                    #(f"Вы работаете уже: {s} сек. Осталось до следущего отдыха {work_without_timeout - s} сек.")
                time.sleep(1)
            accounting += "a"
            print("Пора сделать короткий перерыв!")
            for s in range(0, little_timeout + 1):
                if done + 1 > work_time:
                    print(f"Время работы истекло! Вы продуктивно работали {done} сек.")
                    #(f"Время работы истекло! Вы продуктивно работали {done} сек.")
                if s != 0:
                    print(f"Вы отдыхаете уже: {s} сек. До работы осталось {little_timeout - s} сек.")
                    done += 1
                    now = ['chill', s, little_timeout - s]
                    #(f"Вы отдыхаете уже: {s} сек. До работы осталось {little_timeout - s} сек.")
                time.sleep(1)
            accounting += "b"
            print("Пора возвращаться к работе((")