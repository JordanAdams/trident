import shutilwhich
import shutil
from os import path
from utils import stream_command, run_command

ASDF_PATH = path.join(path.expanduser('~'), '.asdf')
ASDF_BIN = path.join(ASDF_PATH, 'asdf.sh')


def install_asdf():
    return stream_command([
        'git',
        'clone',
        'https://github.com/asdf-vm/asdf.git',
        ASDF_PATH,
        '--branch',
        'v0.3.0'
    ])


def asdf_is_installed():
    return path.isfile(ASDF_BIN)


def installed_plugins():
    proc = run_command(['asdf', 'plugin-list'])
    return proc.output.decode('utf_8').splitlines()


def plugin_is_installed(plugin):
    return plugin in installed_plugins()


def install_plugin(plugin, repo):
    cmd = 'source {bin} && asdf plugin-add {plugin} {repo}'.format(
        bin=ASDF_BIN,
        plugin=plugin,
        repo=repo
    )

    return stream_command(['bash', '-c', cmd])


def asdf_is_installed():
    return path.isfile(ASDF_BIN)


def installed_versions(language):
    cmd = 'source {bin} && asdf list {language} || true'.format(
        bin=ASDF_BIN,
        language=language
    )
    proc = run_command(['bash', '-c', cmd])
    return proc.output.decode('utf_8').splitlines()


def version_is_installed(language, version):
    return version in installed_versions(language)


def install_version(language, version):
    cmd = 'source {bin} && asdf install {language} {version}'.format(
        bin=ASDF_BIN,
        language=language,
        version=version
    )

    return stream_command(['bash', '-c', cmd])


def import_node_keys():
    script_path = path.join(ASDF_PATH, 'plugins', 'nodejs', 'bin', 'import-release-team-keyring')

    return stream_command(['bash', script_path])


def set_global(language, version):
    cmd = 'source {bin} && asdf global {language} {version}'.format(
        bin=ASDF_BIN,
        language=language,
        version=version
    )

    return run_command(['bash', '-c', cmd])
