#!/usr/bin/env ruby

arg = ARGV[0]
regex = /hb?tn/
puts regex.match("#{arg}")
