import time


def runtime(func, *args, run_count=100000, **kwargs):
    start_time = time.time()
    for _ in range(run_count):
        func(*args, **kwargs)
    print('{}运行{}次耗时{:.5}s'.format(func.__name__, run_count, time.time() - start_time))
