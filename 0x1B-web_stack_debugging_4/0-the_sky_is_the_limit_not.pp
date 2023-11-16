node default{
    exec {'set up limits':
        command  => 'sed -i "s/15/5000/g" /etc/default/nginx;
        service nginx restart',
        provider => shell
    }
}
