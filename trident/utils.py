import command
from termcolor import cprint


def run_command(cmd):
    return command.run(cmd)


def stream_command(cmd):
    return command.run(cmd, debug=_print_output)


def _print_output(raw_line):
    line = '>> {}'.format(raw_line.decode('utf_8'))
    cprint(line, 'grey', attrs=['dark'])
