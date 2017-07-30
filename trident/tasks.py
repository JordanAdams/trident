import brew
import asdf
import sys
from interface import print_success, print_heading, print_error, print_skipping, confirm_install, print_skipping


def install_brew():
    if brew.brew_is_installed():
        print_success('Brew')
    elif confirm_install('Brew'):
        brew.install_brew()
    else:
        print_error('Brew is required to continue. Aborting.')
        sys.exit(1)


def install_brew_package(package):
    if brew.is_installed(package):
        print_success(package)
    elif confirm_install(package):
        brew.install(package)
    else:
        print_skipping(package)


def install_asdf():
    if asdf.asdf_is_installed():
        print_success('Asdf')
    elif confirm_install('Asdf'):
        asdf.install_asdf()
    else:
        print_error('Asdf is required to continue. Aborting.', 'red')
        sys.exit(1)


def install_asdf_plugin(display_name, name, repo):
    display_name = '{}'.format(display_name)
    if asdf.plugin_is_installed(name):
        print_success(display_name)
    elif confirm_install(display_name):
        asdf.install_plugin(name, repo)
    else:
        print_skipping(display_name)


def install_asdf_version(display_name, name, version):
    display_name = '{} {}'.format(display_name, version)
    if asdf.version_is_installed(name, version):
        print_success(display_name)
    elif confirm_install(display_name):
        asdf.install_version(name, version)
    else:
        print_skipping(display_name)
