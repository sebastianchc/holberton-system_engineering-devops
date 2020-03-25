# Setup SSH config file
file_line { 'No password authentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '#    PasswordAuthentication no'
}
file_line { 'Adding identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '#    IdentityFile ~/.ssh/holberton'
}