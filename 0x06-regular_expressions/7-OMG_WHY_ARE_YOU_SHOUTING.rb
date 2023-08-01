#!/usr/bin/env ruby

arg = ARGV[0]
regex = /[A-Z]/
matches = arg.scan(regex)
matches.each { |match| print match }
print "\n"
