import unittest
import threading
import datetime
import time
import abc


class TimerTask(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @abc.abstractmethod
    def run(self, *args, **kwargs):
        pass


def run_time(func):
    def wrap(*args, **kwargs):
        # start = time.clock()
        start = time.time()
        ret = func(*args, **kwargs)
        # end = time.clock()
        end = time.time()
        print "run_time: %s , func_name: %s" % ((end - start), func.__name__)
        # log.info("run_time: %s , func_name: %s" % ((end - start), func.__name__))
        return ret
    return wrap


class BaseTimer(threading.Thread):
    """docstring for TimerTask"""

    def __init__(self):
        super(BaseTimer, self).__init__()
        self.finished = threading.Event()
        self.interval = 0

    @run_time
    def schedule(self, task, delay=0, interval=0):
        if isinstance(task, TimerTask):
            self.task = task
            self.delay = delay
            self.interval = interval
            self.start()

    def run(self):
        time.sleep(self.delay)
        if self.interval:
            while True:
                self.finished.wait(self.interval)
                if not self.finished.is_set():
                    self.task.run(self.task.args, self.task.kwargs)
                else:
                    break
        else:
            self.finished.wait(self.interval)
            if not self.finished.is_set():
                self.task.run(self.task.args, self.task.kwargs)

    def cancel(self):
        self.finished.set()


class PrintTask(TimerTask):
    def __init__(self, *args, **kwargs):
        super(PrintTask, self).__init__(args, kwargs)

    def run(self, *args, **kwargs):
        print "task_%s:%s" % (self.args, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


# class TimerTest(unittest.TestCase):

#     def test_base_opration(self):
#         def base_func():
#             print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#         base_timer = threading.Timer(1, base_func)
#         print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         base_timer.start()


class BaseTimerTest(unittest.TestCase):
    def test_schedule(self):
        task = PrintTask(1)
        task_timer = BaseTimer()
        print "begin: %s " % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        task_timer.schedule(task, 2, 1)

    def test_schedule_once(self):
        task = PrintTask(2)
        task_timer = BaseTimer()
        print "begin: %s " % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        task_timer.schedule(task, 2)

    def test_cancel(self):
        print "test cancel"
        task = PrintTask(3)
        task_timer = BaseTimer()

        task_timer.schedule(task, 2, 1)
        task_timer.cancel()


if __name__ == '__main__':
    unittest.main()
    while True:
        time.sleep(1)
