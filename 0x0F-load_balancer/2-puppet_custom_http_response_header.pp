#script o add header
node default {
    package {'nginx':
        ensure   => 'installed',
        provider => 'apt'
    }
    exec {'exec':
        command => "sed -i 's|# First attempt to serve request as file, then|add_header X-Served-By \$hostname;|g'\
 /etc/nginx/sites-available/default",
        path    => '/usr/bin',
    }
    exec {'service':
        command => 'service nginx restart',
        path    => '/usr/sbin:/usr/bin',
        require => Package['nginx']
    }
}
