# Add HTTP header
exec { 'Update':
     command => '/usr/bin/apt-get -y update'
}

exec { 'Install':
     require => Exec['Update'],
     command => '/usr/bin/apt-get -y install nginx'
}

exec { 'Header':
     require => Exec['Install'],
     command => '/bin/sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-enabled/default'
}

exec { 'Start':
     require => Exec['Header'],
     command => '/usr/sbin/service nginx start'
}
