#!/usr/bin/perl -w 
use v5.18.2;


if ($#ARGV == 0 || lc($ARGV[0]) eq 'xiu') {
    say "🐬🐬🐬 Submint through account : XIU";
    `cp /Users/alpha/.lc/xiu.json /Users/alpha/.lc/leetcode/user.json `;
}  elsif ( $#ARGV >= 1 && lc($ARGV[0]) eq '117') {
    say "🐐🐐🐐 Submint through account : 117";
    `cp /Users/alpha/.lc/firefly.json /Users/alpha/.lc/leetcode/user.json `;
} else {
    die "Choices are either XIU or 117";
}

say `/usr/local/bin/proxychains4 -q /usr/local/bin/leetcode submit $ARGV[$#ARGV]`;
