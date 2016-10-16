import os
import sys

import traceback
import time
import multiprocessing
import threading
import Queue


def run_time(func):
    def wrap(*args, **kwargs):
        # start = time.clock()
        start = time.time()
        ret = func(*args, **kwargs)
        # end = time.clock()
        end = time.time()
        # log.info("run_time: %s , func_name: %s" % ((end - start), func.__name__))
        print "run_time: %s , func_name: %s" % ((end - start), func.__name__)
        return ret
    return wrap


class WorkerTask(object):
    """A task to be performed by the ThreadPool."""

    def __init__(self, func, args=(), kwargs={}):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        self.func(*self.args, **self.kwargs)


class WorkerThread(threading.Thread):
    """A thread managed by a thread pool."""

    def __init__(self, pool, time_out=1):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.pool = pool
        self._started = False
        self.time_out = time_out

    def work(self):
        self._started = True
        self.start()

    def run(self):
        while True:
            try:
                task = self.pool._tasks.get(timeout=self.time_out)
                self.pool._free_thread_cnt -= 1
                # log.info("begin free_cnt: %s" % self.pool._free_thread_cnt)
                print "begin free_cnt: %s" % self.pool._free_thread_cnt
                task()
                self.pool._free_thread_cnt += 1
                # log.info("after free_cnt: %s" % self.pool._free_thread_cnt)
                print "after free_cnt: %s" % self.pool._free_thread_cnt
            except Queue.Empty:
                # TODO:  need to release this thread
                if self.pool._stop:
                    break
                time.sleep(1)
            except KeyboardInterrupt:
                break
            except Exception, ex:
                print str(ex)

            # TODO : use condition to notify


class ThreadPool(object):
    """Executes queued tasks in the background."""

    def __init__(self, max_pool_size=10):
        self.max_pool_size = max_pool_size
        self._threads = []
        self._free_thread_cnt = 0
        self._tasks = Queue.Queue()
        self._stop = False
        # self.con = threading.Condition()

    def _add_task(self, task):
        self._tasks.put(task)
        # log.info("thread_len: %s" % len(self._threads))
        if len(self._threads) < self.max_pool_size and self._free_thread_cnt == 0:
            worker_thread = WorkerThread(self)
            self._threads.append(worker_thread)
            self._free_thread_cnt += 1
            worker_thread.start()
        # self.con.notifyAll()

    def add_task(self, function, args=(), kwargs={}):
        if not self._stop:
            self._add_task(WorkerTask(function, args, kwargs))

    def close(self):
        self._stop = True

    def wait_complete(self):
        while len(self._threads):
            thread = self._threads.pop()
            if thread.isAlive():
                thread.join()


def print_test(args=(), kwargs={}):
    time.sleep(1)
    print "args: %s  \n" % (args)
    # print "kwargs: %s" % kwargs
    print "*" * 30


@run_time
def time_test():
    pool = ThreadPool(100)
    for i in range(100):
        pool.addTask(print_test, (i,))
        time.sleep(0.5)

    pool.close()
    pool.wait_complete()
    print "complete"


@run_time
def time_test3():
    pool = ThreadPool(3)
    for i in range(100):
        pool.addTask(print_test, (i,))
        time.sleep(0.5)

    pool.close()
    pool.wait_complete()
    print "complete"
if __name__ == "__main__":
    pool = ThreadPool(100)
    for i in range(100):
        pool.add_task(print_test, (i,))
        time.sleep(0.5)

    pool.close()
    pool.wait_complete()
    print "complete"
