from flask import Flask, request, render_template, redirect, url_for, jsonify
import threading
from time import localtime
import timer_logic

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('test.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    timer_start = timer_logic.send_status()
    if timer_start is None:
        return jsonify({"1": ["ожидание", ""], "2": ["", ""], "3": ""})
    return jsonify(timer_start)

def correct1(value):
    if ":" not in value:
        return False
    return True

@app.route('/start', methods=['POST'])
def start():
    # Проверяем, не запущен ли уже таймер
    if timer_logic.now[0] is not None:
        return render_template('error.html', error_message="Таймер уже запущен. Остановите текущий таймер перед запуском нового.")

    able_to_work = request.form['able_to_work']
    no_break = request.form['no_break']
    short_break = request.form['short_break']
    long_break = request.form['long_break']

    if not correct1(able_to_work):
        return render_template('error.html', error_message="Неверный формат времени. Используйте HH:MM.")

    now = localtime()
    local_time = now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec

    try:
        new1 = [int(i) for i in able_to_work.split(":")]
        hours1 = new1[0]
        minutes1 = new1[1]
    except Exception:
        return render_template('error.html', error_message="Неверный формат времени. Используйте HH:MM.")

    if hours1 < 0 or hours1 > 23 or minutes1 < 0 or minutes1 > 59:
        return render_template('error.html', error_message="Неверный формат времени. Используйте HH:MM.")

    goal_time = hours1 * 60 * 60 + minutes1 * 60
    work_time = goal_time - local_time

    if work_time <= 0:
        return render_template('error.html', error_message="Неверный формат времени. Используйте HH:MM.")

    threading.Thread(target=timer_logic.run_timer, args=(able_to_work, no_break, short_break, long_break)).start()

    return render_template('started.html')

@app.route('/stop', methods=['POST'])
def stop():
    with timer_logic.lock:
        timer_logic.stop_flag = True
        timer_logic.now = [None, 0, 0]
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
