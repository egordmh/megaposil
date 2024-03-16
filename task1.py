# python

def time_to_sec(hms):
    """
    Описание функции time_to_sec:
    Первеводит время из строки формата ЧЧ:ММ:СС в секунды
    :параметер hms: строка временеи в формате ЧЧ:ММ:СС
    :возвращаемое значение: время в секундах
    """
    h, m, s = map(int, hms.split(":"))
    t = h * 3600 + m * 60 + s
    return t


def sec_to_time(sec):
    """
    Описание функции sec_to_time:
    Переводит время из секунд в формат ЧЧ:ММ:СС
    :параметер sec: время в секундах
    :возвращаемое значение:строка времени в формате ЧЧ:ММ:СС
    """
    h = (sec // 3600) % 24
    if h < 10:
        h = "0" + str(h)
    else:
        h = str(h)
    sec = sec % 3600
    m = sec // 60
    if m < 10:
        m = "0" + str(m)
    else:
        m = str(m)
    sec = sec % 60
    if sec < 10:
        sec = "0" + str(sec)
    else:
        sec = str(sec)
    return str(h) + ":" + str(m) + ":" + str(sec)


def main():
    """
    Описание функции main:
    Восстанавливает текущее время в каютах станций
    :input: csv-файл содержащий строки со значениями: WatchNumber,numberStation,cabinNumber,timeStop,count
    :output: txt-файл содержащий строки с восстановленным временем
    """
    fi = open("astronaut_time.csv", "r", encoding="utf8")
    fo = open("new_time.txt", "w", encoding="utf8")

    l = fi.readlines()[1::]
    for x in range(len(l)):
        wn, ns, cn, ts, c = map(str, l[x].split(","))
        wn = int(wn)
        c = int(c)
        tf = sec_to_time(time_to_sec(ts) + c)
        rs = "На станции " + ns + " в каюте " + cn + " восстановлено время. Актуальное время: " + tf + "\n"
        print(rs)
        fo.write(rs)


main()
