#
# @lc app=leetcode id=535 lang=ruby
#
# [535] Encode and Decode TinyURL
#
# https://leetcode.com/problems/encode-and-decode-tinyurl/description/
#
# algorithms
# Medium (75.12%)
# Total Accepted:    61.9K
# Total Submissions: 82.1K
# Testcase Example:  '"https://leetcode.com/problems/design-tinyurl"'
#
# Note: This is a companion problem to the System Design problem: Design
# TinyURL.
#
# TinyURL is a URL shortening service where you enter a URL such as
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such
# as http://tinyurl.com/4e9iAk.
#
# Design the encode and decode methods for the TinyURL service. There is no
# restriction on how your encode/decode algorithm should work. You just need to
# ensure that a URL can be encoded to a tiny URL and the tiny URL can be
# decoded to the original URL.
#
#
# Encodes a URL to a shortened URL.
#
# @param {string} longUrl
# @return {string}
$urls = []

def encode(longUrl)
	$urls << longUrl
	'http://tinyurl.com/' + $urls.size.to_s
end

# Decodes a shortened URL to its original URL.
#
# @param {string} shortUrl
# @return {string}
def decode(shortUrl)
	idx = shortUrl.split('/').last.to_i - 1
	$urls[idx]
end

# Your functions will be called as such:
# decode(encode(url))
p encode('httpsaaa')
p decode('/1')
