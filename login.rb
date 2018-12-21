#!/user/bin/env ruby
require 'colorize'
require 'pty'
require 'expect'

def is_login
  !`leetcode user`.include?('ERROR')
end

def login_account(credfile)
  username, passwd = `head -n 2 #{credfile}`.split("\n")
  10.times do
    break if is_login
    puts '[Sign in ...]'.blue

    PTY.spawn('leetcode user -l') do |reader, writer|
      # cont. in 5s if input doesn't match
      reader.expect(/login:/, 5)
      writer.puts(username)
      reader.expect(/pass:/, 5)
      writer.puts(passwd)
      # sleep(3)
      puts "cmd response: #{reader.gets}"
    end
  end
  puts is_login ? '[Login succeed!]'.green : '[Login failed, try again later.]'.red
end

login_account('/usr/local/info/credential.dat')
