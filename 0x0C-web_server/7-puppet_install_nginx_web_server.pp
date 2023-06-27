#!/usr/bin/env bash
# Puppet manifest containing commands to automatically configure an Ubuntu machine
class nginx_server {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => '
      server {
        listen 80;
        root /var/www/html;
        
        location / {
          return 301 http://example.com/redirect_me;
        }

        location /redirect_me {
          return 200 "Hello World!";
        }
      }
    ',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure => running,
    enable => true,
    require => File['/etc/nginx/sites-available/default'],
  }
}

include nginx_server

