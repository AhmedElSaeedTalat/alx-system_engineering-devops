#file to create config file
node default {
file {'/home/vagrant/.ssh/config':
ensure  => 'present',
content => "Host *\n\
				PasswordAuthentication	no\n\
				IdentityFile	~/.ssh/school",
mode    => '0600'
}
}
