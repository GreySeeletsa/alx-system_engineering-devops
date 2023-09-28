#!/usr/bin/env bash
# Puppet to make changes to our configuration file

file { 'etc/ssh/ssh_config':
	ensure => present,

content =>"

	#client SSH configuration file
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
