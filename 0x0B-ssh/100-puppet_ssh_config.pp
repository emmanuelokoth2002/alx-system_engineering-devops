#!/usr/bin/env bash
# SSH configuration file so that you can connect to a server without typing a password.
package { 'augeas-tools':
  ensure => installed,
}

augeas { 'Turn off passwd auth':
  context => '/files/etc/ssh/sshd_config',
  changes => [
    'set #comment[.="PasswordAuthentication"]/../PasswordAuthentication no',
  ],
}

augeas { 'Declare identity file':
  context => '/files/etc/ssh/ssh_config',
  changes => [
    'set #comment[.="IdentityFile"]/../IdentityFile ~/.ssh/school',
  ],
}
