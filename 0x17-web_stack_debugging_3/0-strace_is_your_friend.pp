# puppet scritp edit name if incorrect file
node default {
  exec {'exec':
    command  => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php;
    service apache2 restart',
    provider => shell
  }
}
