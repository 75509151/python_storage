import threading
import random
import time

glo_dic = dict()


def set_value(dic):
    while True:
        for i in range(255):
            if i not in dic:
                a = random.randint(0, 999999)
                b = random.randint(0, 999999)
                c = a - b
                val = "%s %s %s" % (a, b, c)
                dic[i] = val
        # time.sleep(1)


def int_s(s):
    return int(s)


def judge_value(dic):
    while True:
        for i in range(255):
            if i in dic:
                a, b, c = map(int_s, dic.pop(i).split())
                if c == a - b:
                    print "right: %s, %s, %s   %s" % (a, b, c, i)

                else:
                    print "err: %s, %s, %s" % (a, b, c)
                    raise
        # time.sleep(1)


def main():
    t1 = threading._start_new_thread(set_value, (glo_dic,))
    t2 = threading._start_new_thread(judge_value, (glo_dic,))
    t3 = threading._start_new_thread(judge_value, (glo_dic,))
    # a.start()
    # b.start()
    # t.join()
    # b.join()
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
