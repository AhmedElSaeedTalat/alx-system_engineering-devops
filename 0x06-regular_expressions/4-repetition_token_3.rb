#!/usr/bin/env ruby

arg = ARGV[0]
regex = /hb(t+)?n/
puts regex.match("#{arg}")
