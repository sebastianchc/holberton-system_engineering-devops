# Install and configure NGINX
exec { 'Update' :
     command => '/usr/bin/apt-get -y update'
}

exec { 'Install' :
     require => Exec['Update'],
     command => '/usr/bin/apt-get -y install nginx'
}

exec { 'Content' :
     require => Exec['Install'],
     command => '/bin/echo "Holberton School" > /var/www/html/index.nginx-debian.html'
}

exec { 'Redirection' :
     require => Exec['Content'],
     command => '/bin/sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;/" /etc/nginx/sites-enabled/default'
}

exec { 'Start' :
     require => Exec['Redirection'],
     command => '/usr/sbin/service nginx start'
}