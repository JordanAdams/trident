# coding: utf-8
from termcolor import cprint, colored


def print_heading(heading):
    heading = '\n{}'.format(heading)
    line_length = len(heading) + 10
    line = '-' * line_length

    cprint('\n{}'.format(heading), 'white', attrs=['bold'])
    cprint(line, 'grey', attrs=['dark'])


def print_success(text):
    cprint('✔ {}'.format(text), 'green')


def print_error(text):
    cprint('! {}'.format(text), 'red', attrs=['bold'])


def print_skipping(subject):
    cprint('• Skipping {}'.format(subject), 'blue')


def confirm_install(subject):
    return confirm('✘ {} is missing. Install it?'.format(subject))


def confirm(question):
    question = '{} (Y/n): '.format(question)
    question = colored(question, 'yellow')
    answer = raw_input(question)
    return answer.lower() not in ['n', 'no']
