from UseFul import FunctionLog
from logbook import StreamHandler
from sys import stdout

StreamHandler(stdout).push_application()

func_log = FunctionLog('function')


@func_log(info="88:88:88:88:88")
def check(name, lastname, age=30):
    if isinstance(age, float):
        check.error = True
        check.log.info('age should be int')
        return
    return (name, lastname, age,)


print(check("hamed", "knew", 18.6))
