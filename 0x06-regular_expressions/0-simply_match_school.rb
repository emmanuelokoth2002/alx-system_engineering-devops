#!/usr/bin/env ruby

string = ARGV[0]
regex = /School/
matches = string.scan(regex).join('$') + '$'
puts matches
