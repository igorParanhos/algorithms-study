import time


def benchmark(fn):
    start = time.perf_counter_ns()
    result = fn()
    elapsed_time = time.perf_counter_ns() - start

    fn_name = fn.__name__.replace('_', ' ').title()
    print('{} \n\t-> Result = {} \n\t-> Executed in {}mS({:.10f}s)\n'.format(
        fn_name, 
        result, 
        elapsed_time / 1000,
        elapsed_time / 1000 / 1000 / 1000))