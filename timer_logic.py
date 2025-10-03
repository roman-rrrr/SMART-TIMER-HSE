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
