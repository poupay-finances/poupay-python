import timeit

def get_time_response(function_test):
    time_response = timeit.timeit(lambda : function_test)
    return round(time_response, 2)

def randomValor(peso, variacao):
    base = 1_000_000
    return (base * peso) + (variacao * base * peso)
