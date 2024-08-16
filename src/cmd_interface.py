import os
import subprocess
import shlex


def exec_command(command_line):
    args = shlex.split(command_line)
    process = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode('cp866')