#!/usr/bin/env bash
# SSH configuration file so that you can connect to a server without typing a password.
file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => "PasswordAuthentication no\nIdentityFile ~/.ssh/school\n",
}

service { 'ssh':
  ensure => running,
  enable => true,
}
