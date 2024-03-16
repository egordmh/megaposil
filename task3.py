#python

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


def Ui(l):
    n = str(input("Ведите номер станции: "))
    if n!="stop":
        for x in l:
            if n in x:
                wn, ns, cn, ts, c = map(str, x.split(","))
                wn = int(wn)
                c = int(c)
                tf = sec_to_time(time_to_sec(ts) + c*3600)
                rs = "На станции " + ns + " восстановлено время. Актуальное время: " + tf + "\n"
                print(rs)
                return(True)
        print("На этой станции все хорошо")
    else:
        return(False)




def main():
    fi = open("astronaut_time.csv", "r", encoding="utf8")


    l = fi.readlines()[1::]

    while(Ui(l)):
        pass

main()
