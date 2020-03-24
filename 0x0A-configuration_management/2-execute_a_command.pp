# kill a process named killmenow
exec { 'Terminated':
  path     => ['/bin', '/sbin', '/usr/bin', '/usr/sbin'],
  command  => 'pkill killmenow',
  provider => 'shell',
}