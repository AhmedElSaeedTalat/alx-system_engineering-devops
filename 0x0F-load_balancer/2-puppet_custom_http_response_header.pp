#script o add header
node default {
    exec {'exec':
        command  => 'apt-get -y update;
        apt-get -y install nginx;
        sed -i "s|# First attempt to serve request as file, then|add_header X-Served-By \$hostname;|g" /etc/nginx/sites-available/default;
        service nginx restart',
        provider => shell
    }
}
