from time import localtime


def format_time(seconds):
    seconds = int(seconds)
    minutes = seconds // 60
    seconds = seconds % 60
    if minutes == 0:
        return f"{seconds} сек"
    return f"{minutes} мин {seconds} сек"


_1 = input()  # ввод времени до которого пользоаватель готов работать формат (h:m)

now = localtime()  # текущее время у пользователя формата (h:m:s)
local_time = (
    now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec
)  # текущее время в секундах

new1 = [int(i) for i in _1.split(":")]
hours1 = new1[0]  # до скольки часов готов работать
minutes1 = new1[1]  # до скольки минут готов работать

goal_time = hours1 * 60 * 60 + minutes1 * 60  # до скольки можете работать в секундах

work_time = goal_time - local_time  # СКОЛЬКО ПОЛЬЗОВАТЕЛЬ ГОТОВ РАБОТАТЬ В СЕК

print(work_time)
