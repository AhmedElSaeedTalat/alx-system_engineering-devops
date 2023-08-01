#!/usr/bin/env ruby

arg = ARGV[0]
regex = /hbt+n/
puts regex.match("#{arg}")
