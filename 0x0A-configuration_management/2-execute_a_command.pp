#create a manifest to kill process named killmenow
exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => '/usr/bin:/usr/sbin:/bin:/sbin',
  refreshonly => true,
}
