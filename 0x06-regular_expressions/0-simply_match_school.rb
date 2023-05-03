#!/usr/bin/env ruby

string = ARGV[0]
regex = /School/
matches = string.scan(Oniguruma::ORegexp.new(regex)).join('$') + '$'
puts matches
