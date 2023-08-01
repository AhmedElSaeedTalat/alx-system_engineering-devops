#!/usr/bin/env ruby

arg = ARGV[0]
regex = /^\d{9}[^- ]/
puts regex.match("#{arg}")
