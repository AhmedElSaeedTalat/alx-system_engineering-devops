#!/usr/bin/env ruby

arg = ARGV[0]
regex = /^h\wn$/
puts regex.match("#{arg}")
