@app.route("/start", methods=["POST"])
def start():
    able_to_work = request.form["able_to_work"]
    no_break = request.form["no_break"]
    short_break = request.form["short_break"]
    long_break = request.form["long_break"]

    if correct1(able_to_work) == False:
        return render_template(
            "error.html", error_message="Неверный формат времени. Используйте HH:MM."
        )

    now = localtime()
    local_time = (
        now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec
    )  # текущее время в секундах

    new1 = [int(i) for i in able_to_work.split(":")]  # до скольки можете работать
    hours1 = new1[0]
    minutes1 = new1[1]

    if hours1 < 0 or hours1 > 23 or minutes1 < 0 or minutes1 > 59:
        return render_template(
            "error.html", error_message="Неверный формат времени. Используйте HH:MM."
        )

    _5 = hours1 * 60 * 60 + minutes1 * 60  # до скольки можете работать в секундах

    work_time = _5 - local_time

    if work_time <= 0:
        return render_template(
            "error.html", error_message="Неверный формат времени. Используйте HH:MM."
        )

    threading.Thread(
        target=timer_logic.run_timer,
        args=(able_to_work, no_break, short_break, long_break),
    ).start()
    # return render_template('started.html')

    timer_start = timer_logic.send_status()

    status1 = timer_start["1"][0] + timer_start["1"][1]
    status2 = timer_start["2"][0] + timer_start["2"][1]
    status3 = timer_start["3"]

    # print(status1)
    # print(status2)
    # print(status3)

    return render_template(
        "started.html",
        ## work_time=work_time,
        ## no_break=no_break,
        ## short_break=short_break,
        ## long_break=long_break,
        status1=status1,
        status2=status2,
        status3=status3,
    )
