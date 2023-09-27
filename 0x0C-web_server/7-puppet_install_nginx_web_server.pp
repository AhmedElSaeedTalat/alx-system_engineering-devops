# script in install nginx
node default {
    package {'nginx':
        ensure   => 'installed',
        provider => 'apt',
    }

exec {'edit line':
        command => 'sed -i "s|# SSL configuration|rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;|g" /etc/nginx/sites-available/default',
        path    => '/usr/bin'
    }
file {'/var/www/html/index.nginx-debian.html':
        ensure  => 'present',
        content => 'Hello World!',
    }
exec {'sevice nginx restart':
        command => 'service nginx start',
        path    => '/usr/sbin:usr/bin',
        require => Package['nginx'],
    }
}
