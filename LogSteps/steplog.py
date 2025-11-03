import os
import gdb

script_dir = os.path.dirname(__file__)

class StepLogger(gdb.Command):
    def __init__(self):
        super(StepLogger, self).__init__("logstep", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        logfile = open(os.path.join(script_dir, "regs.log"), "w")
        # default steps
        steps = 100

        # parse -n NUM argument
        args = gdb.string_to_argv(arg)
        if len(args) >= 2 and args[0] == "-n":
            try:
                steps = int(args[1])
            except ValueError:
                print("Invalid number for -n")
                return

        for _ in range(steps):
            gdb.execute("stepi", to_string=True)

            pc_dism = gdb.execute("x/i $pc", to_string=True)
            regs = gdb.execute("info registers", to_string=True)

            logfile.write(pc_dism + "\n")
            logfile.write(regs + "\n")
            logfile.write("----------------------------------------------------- \n")
            logfile.flush()

StepLogger()
