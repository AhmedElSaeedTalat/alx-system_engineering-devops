#file to create config file
node default {
exec {'echo':
command => 'echo PasswordAuthentication no"\n"IdentityFile ~/.ssh/school >> /etc/ssh/ssh_config',
path    => '/usr/bin'
}
}
