#!/usr/bin/env bash
# script to install HAproxy
sudo apt-get -y update
sudo apt-get -y install haproxy
back_end='
frontend http\n\t
        bind *:80\n\t
        mode http\n\t
        default_backend web-backend\n\n

backend web-backend\n\t
        balance roundrobin\n\t
        server 386537-web-01 52.23.178.138:80 check\n\t
        server 386537-web-02 100.25.29.150:80 check'
echo -e "$back_end" | sudo tee -a /etc/haproxy/haproxy.cfg > /dev/null
sudo service haproxy restart
