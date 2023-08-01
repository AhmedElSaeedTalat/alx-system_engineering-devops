#!/usr/bin/env ruby

arg = ARGV[0]
regex = /^\d+\d$/
puts regex.match("#{arg}")
