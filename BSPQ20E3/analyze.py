'''Simple module for performance testing'''

import cProfile, io, pstats
from pstats import SortKey
from panel.githubcsv import get_csv_from_github


n = 1

def test_dat_performance(file_name='perf_file', func=None, test_type=1, *args, **kwargs):

    """
    Description
    -----------
    Simple function to do basic profiling tasks on functions and dump statistics into a .txt file

    Attributes
    ----------
    file_name: str
      name of the file t dump the profiling stats to
      default value: 'perf_file' + '_{n}', where n is some static constant of the script

    func: Callable
      function to be profiled
      default value: None

    test_type: int
      type of profiling test to perform on the function passed

      1 -> cumulative (monitor cumulative time of execution)
      2 -> time (monitor time spent within each function)
      3 -> calls (monitor number of calls)

      default value: 1

    *args and **kwargs
      parameters of the funciton to be profiled, you can pass them as keyword parameters or old-school

    """

    global n

    # initialize the profiler
    profiler = cProfile.Profile()

    # actually profile the function with the given params
    profiler.enable()
    func(*args, **kwargs)
    profiler.disable()

    # io stream to dump stats into human-readable format
    stats_iostream = io.StringIO()

    # neat class to manage statistics of profiler and its results
    statistics = pstats.Stats(profiler, stream=stats_iostream)

    sortkey = None
    if test_type == 1:
        sortkey = SortKey.CUMULATIVE
    elif test_type == 2:
        sortkey = SortKey.TIME
    elif test_type == 3:
        sortkey = SortKey.CALLS

    # print the stats into the stream
    statistics.sort_stats(sortkey).print_stats()

    # dump the stast into a .txt file
    if file_name == 'perf_file':
        with open(f'perftest/perf_file_{n}.text', 'w') as f:
            f.write(stats_iostream.getvalue())
        n = n + 1
    else:
        with open(f'perftest/{file_name}.text', 'w') as f:
            f.write(stats_iostream.getvalue())

    # close up all the things
    profiler.clear()
    stats_iostream.close()


if __name__ == "__main__":

    test_dat_performance(
        func=get_csv_from_github,
        test_type=1,
        date='24-04-2020'
    )