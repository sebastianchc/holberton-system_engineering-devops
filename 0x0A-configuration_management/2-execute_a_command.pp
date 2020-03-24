# kill a process named killmenow
exec { 'Terminated':
  command => 'pkill killmenow',
  path    => '/usr/bin/',
  returns => [0,1],
}