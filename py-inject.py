import gdb

class PyInject(gdb.Command):
    """Inject Python code into the running process."""

    def __init__(self):
        super(PyInject, self).__init__("py-inject", gdb.COMMAND_USER)

    def invoke(self, code, from_tty):
        gdb.execute("set $gstate = ((int(*)()) PyGILState_Ensure)()")
        gdb.execute(
            'call ((int(*)(const char*)) PyRun_SimpleString)("%s")'
            % code.replace('"', '\\"')
        )
        gdb.execute("call ((void(*)(int)) PyGILState_Release)($gstate)")

PyInject()
