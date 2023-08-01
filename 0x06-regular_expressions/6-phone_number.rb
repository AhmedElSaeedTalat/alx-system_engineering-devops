#!/usr/bin/env ruby

arg = ARGV[0]
regex = /^\d{9}\d$/
puts regex.match("#{arg}")
