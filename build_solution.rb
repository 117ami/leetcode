require 'nokogiri'
require 'open-uri'

abort('Specify an url first') if ARGV[0].nil?
languages = {} # Choose which language
['c', '-c', 'cpp', '-cpp'].each { |c| languages[c] = '.cpp' }
['r', '-r', 'ruby', '-ruby', 'rb', '-rb'].each { |c| languages[c] = '.rb' }
['p', '-p', 'py', '-py', 'python', '-python'].each { |c| languages[c] = '.py' }

# default language is cpp;
# problem link is in ARGV[1]
cur_lan = languages[ARGV[0]] || '.cpp'
question_url = ARGV[1] || ARGV[0]
contents = Nokogiri::HTML(open(question_url))
# file = File.open("/home/alpha/Downloads/test.html")
# contents = Nokogiri::HTML(file)

rbfile = ''
contents.css('script').each do |c|
  con = c.content
  next if con.scan(/questionId/).empty?
  qid = con.scan(/questionId:\s*\'(\d+)\'/)[0][0]
  qtitle = con.scan(/questionTitleSlug:\s*\'(.*)\'/)[0][0].split('-').join('_')
  rbfile = [qid, qtitle].join('_') + cur_lan
  system("touch #{rbfile}")
end

des = ''
contents.css('meta').each do |c|
  next unless c.values[0] == 'description'
  if cur_lan == '.cpp' # creating cpp descriptions
    des = "/**\n" + c.values[1].gsub(/(\r\n)+/, "\n") + "\n #{question_url} \n **/\n"
    # pres = ['stdio.h', 'map', 'set', 'unordered_map', 'iostream', 'vector', 'algorithm', 'climits'].map { |i| "#include<#{i}>\n" }.join
    pres = "#include \"aux.cpp\"\n"

    des.insert(0, pres)
    des << "static const int _ = []() { ios::sync_with_stdio(false); cin.tie(NULL); return 0; }(); \n\n"
    des << "int main() { \n Solution s; \n}"
  elsif cur_lan == '.rb'        # creating ruby ...
    des = "=begin\n" + c.values[1].gsub(/(\r\n)+/, "\n") + "\n #{question_url} \n=end\nrequire './aux.rb'"
  else                          # creating python ...
    des = "'''\n" + c.values[1].gsub(/(\r\n)+/, "\n") + "\n'''\n"
  end
end

des.gsub!('&quot;', '"')
des.gsub!('&le;', '<=')
des.gsub!('&ge;', '>=')
des.gsub!('&gt;', '>')
des.gsub!('&lt;', '<')
des.gsub!('&nbsp;', '')
des.gsub!('&#39;', "\'")
des.gsub!('&rarr;', '->')
puts des
File.open(rbfile, 'w') { |wf| wf.puts(des) }

p '**file was created successfully**'
