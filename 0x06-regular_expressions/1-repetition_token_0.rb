#!/usr/bin/env ruby

arg = ARGV[0]
regex = /\bhbt{2,5}n\b/
puts regex.match("#{arg}")
