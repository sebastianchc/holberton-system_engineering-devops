# Web stack debugging 3
exec { 'fix-wordpress':
     command => '/bin/sed -i "s/phpp/php/" /var/www/html/wp-settings.php; /usr/sbin/service apache2 restart'
}
