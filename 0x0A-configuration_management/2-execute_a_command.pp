# script to kill processes
node default{
exec {'killmenow':
command => 'pkill killmenow',
path    => '/usr/bin'
}
}
