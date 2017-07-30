import sys
import brew
import asdf
import tasks
from interface import print_heading

print_heading('Packages')

tasks.install_brew()
tasks.install_asdf()

required_brews = ['git', 'zsh', 'fzf', 'mackup', 'zplug', 'hub', 'peco', 'coreutils', 'automake',
                  'autoconf', 'openssl', 'libyaml', 'readline', 'libxslt', 'libtool', 'unixodbc',
                  'gnupg', 'wxmac', 'erlang']
for package in required_brews:
    tasks.install_brew_package(package)

print_heading('Languages')

tasks.install_asdf_plugin('Node', 'node', 'https://github.com/asdf-vm/asdf-nodejs.git')
tasks.install_asdf_version('Node', 'node', '8.2.1')
asdf.set_global('node', '8.2.1')

tasks.install_asdf_plugin('Elixir', 'elixir', 'https://github.com/asdf-vm/asdf-elixir.git')
tasks.install_asdf_version('Elixir', 'elixir', '1.5.0')
asdf.set_global('elixir', '1.5.0')
