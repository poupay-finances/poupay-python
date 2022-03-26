import timeit

def get_time_response(function_test):
    time_response = timeit.timeit(lambda : function_test)
    return round(time_response, 2)