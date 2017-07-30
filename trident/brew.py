import shutilwhich
import shutil
from utils import stream_command, run_command

installed_packages_cache = []


def install_brew(arg):
    return stream_command([
        '/usr/bin/ruby',
        '-e',
        '"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'
    ])


def brew_is_installed():
    return shutil.which('brew') != None


def install(package):
    global installed_packages_cache
    stream_command(['brew', 'install', package])
    installed_packages_cache.append(package)


def list():
    global installed_packages_cache
    if installed_packages_cache:
        return installed_packages_cache
    else:
        proc = run_command(['brew', 'list'])
        installed_packages_cache = proc.output.decode('utf_8').splitlines()
        return installed_packages_cache


def is_installed(package):
    return package in list()
