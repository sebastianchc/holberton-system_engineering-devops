# kill proccess
exec { 'killmenow' :
  command => '/usr/bin/pkill'
}