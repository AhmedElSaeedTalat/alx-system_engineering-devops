#!/usr/bin/env ruby

arg = ARGV[0]
regex = /(?<=from:|to:|flags:)[^\]]*/
matches = arg.scan(regex)
result = matches.join(",")
print result.chomp(",")
print "\n"
