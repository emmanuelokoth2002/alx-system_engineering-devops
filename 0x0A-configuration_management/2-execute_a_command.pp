#create a manifest to kill process named killmenow
exec { '/usr/bin/env pkill -9 killmenow':
}
