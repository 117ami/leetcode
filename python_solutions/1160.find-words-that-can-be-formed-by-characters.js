var bisect_left = function(nums, target) {
    var i = 0,
        j = nums.length - 1,
        mid;
    while (i < j) {
        mid = ~~((i + j) / 2);
        if (nums[mid] < target)
            i = mid + 1;
        else
            j = mid;
    }
    return i;
}

var bisect_right = function(nums, target) {
    var i = 0,
        j = nums.length - 1,
        mid;
    while (i < j) {
        mid = Math.ceil((i + j) / 2);
        if (nums[mid] > target)
            j = mid - 1;
        else
            i = mid;
    }
    return j;
}

var two_d_array = function(m, n) {
    return new Array(m).fill(0).map(() => new Array(n).fill(0));
}

var reverse = function(s) {
    return [...str].reverse().join('');
}


// simple print
var print = function(a) {
    console.log(a);
}

// For counting elements in a list 
var counter = function(array_or_string) {
    var dict = {};
    for (let i = 0; i < array_or_string.length; i++) {
        let e = array_or_string[i];
        dict[e] = dict[e] ? dict[e] += 1 : 1;
    }
    return dict;
}

var sum = function(array) {
    return array.reduce(function(a, b) {
        return a + b;
    }, 0);
}

var isodd = function(n) {
    return n % 2 == 1;
}

var iseven = function(n) {
    return n % 2 == 0;
}

var list = function(size, value) {
    return Array(size).fill(value);
}


var len = function(str_or_array) {
    return str_or_array.length;
}

var sorted = function(arr) {
    return arr.sort((a, b) => (a - b));
}

var sort_by_last = function(arr) {
    return arr.sort((a, b) => (last(a) - last(b)));
}

var sort_by_first = function(arr) {
    return arr.sort((a, b) => (a[0] - b[0]));
}

// print out a Map 
function printMap(m) {
    m.forEach(function(v, k) {
        console.log(k + " " + v);
    })
}

var gcd = function(a, b) {
    return b == 0 ? a : gcd(b, a % b);
}

var say = function(a) {
    console.log(a)
};


var two_d_array = function(m, n, v = 0) {
    return [...Array(m)].map(x => Array(n).fill(v));
}

function floor(float_number) {
    return Math.floor(float_number)
}

function ceil(float_number) {
    return Math.ceil(float_number)
}


var max = function(arr) {
    return Math.max(...arr);
}

var min = function(arr) {
    return Math.min(...arr)
};

var pairmax = function(a, b) {
    return Math.max(a, b)
}

var pairmin = function(a, b) {
    return Math.min(a, b)
}

// create an array with elements from 0 to n
var nlist = function(n) {
    return [...Array(n + 1).keys()];
}

var ispalindrome = function(s) {
    var i = 0,
        j = len(s) - 1;
    while (i < j) {
        if (s[i] != s[j]) return false;
        i += 1;
        j -= 1;
    }
    return true;
}

function permutations(inputArr) {
    var results = [];

    function permute(arr, memo) {
        var cur, memo = memo || [];

        for (var i = 0; i < arr.length; i++) {
            cur = arr.splice(i, 1);
            if (arr.length === 0) {
                results.push(memo.concat(cur));
            }
            permute(arr.slice(), memo.concat(cur));
            arr.splice(i, 0, cur[0]);
        }

        return results;
    }

    return permute(inputArr);
}

var directions = [
    [-1, -1],
    [-1, 1],
    [0, -1],
    [0, 1],
    [-1, 0],
    [1, -1],
    [1, 0],
    [1, 1]
]

var inf = Infinity;

var last = function(arr) {
    return arr[len(arr) - 1];
}

var first = function(arr) {
    return arr[0];
}

var second = function(arr) {
    return arr[1];
}

var third = function(arr) {
    return arr[2];
}

function exist(hash, key) {
    return (key in hash);
}

// shortest common super-sequence
var scs = function(s, t) {
    var m = len(s),
        n = len(t),
        dp = two_d_array(m + 1, n + 1);
    for (let i = 1; i <= m; i++)
        for (let j = 1; j <= n; j++)
            if (s[i - 1] == t[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            else
                dp[i][j] = pairmax(dp[i - 1][j], dp[i][j - 1]);

    var i = m,
        j = n,
        index = m + n - last(last(dp)),
        res = list(index, '*');

    while (i > 0 && j > 0) {
        if (s[i - 1] == t[j - 1]) {
            res[index - 1] = s[i - 1];
            i -= 1;
            j -= 1;
        } else if (dp[i - 1][j] > dp[i][j - 1]) {
            res[index - 1] = s[i - 1];
            i -= 1;
        } else {
            res[index - 1] = t[j - 1];
            j -= 1;
        }
        index -= 1;
    }


    if (i + j == 0) return res.join('');
    if (j > 0) {
        i = j;
        s = t;
    }

    while (i > 0) {
        res[index - 1] = s[i - 1];
        index -= 1;
        i -= 1;
    }
    return res.join('');
}

// longest common subsequence
var lcs = function(s, t) {
    var m = len(s),
        n = len(t),
        dp = two_d_array(m + 1, n + 1);
    for (let i = 1; i <= m; i++)
        for (let j = 1; j <= n; j++)
            if (s[i - 1] == t[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            else
                dp[i][j] = pairmax(dp[i - 1][j], dp[i][j - 1]);

    var i = m,
        j = n,
        index = last(last(dp)),
        res = list(index, '*');

    while (i > 0 && j > 0) {
        if (s[i - 1] == t[j - 1]) {
            res[index - 1] = s[i - 1];
            index -= 1;
            i -= 1;
            j -= 1;
        } else if (dp[i - 1][j] > dp[i][j - 1]) {
            i -= 1;
        } else {
            j -= 1;
        }
    }
    return res.join('');
}


var zip = function(lista, listb) {
    return a.map(function(e, i) {
        return [e, b[i]];
    });
}

class Counter {
    constructor() {
        this.m = {};
    }

    read(key) {
        return exist(key, this.m) ? this.m[key] : 0;
    }

    plusone(key) {
        if (!this.m[key]) this.m[key] = 0;
        this.m[key] += 1;
    }
}


var div = function(n, k) {
    return floor(n / k);
}

// inclusive of both endpoints
var randint = function(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

var isin = function(s1, s2) {
    return s1.includes(s2);
}


var reverseList = function(head) {
    if (head == null) return head;
    var pre, cur;
    pre = null;
    while (head) {
        cur = head.next;
        head.next = pre;
        pre = head;
        head = cur;
    }
    return pre;
};


/*
 * @lc app=leetcode id=1160 lang=javascript
 *
 * [1160] Find Words That Can Be Formed by Characters
 *
 * https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
 *
 * algorithms
 * Easy (72.76%)
 * Total Accepted:    4.9K
 * Total Submissions: 6.8K
 * Testcase Example:  '["cat","bt","hat","tree"]\n"atach"'
 *
 * You are given an array of strings words and a string chars.
 * 
 * A string is good if it can be formed by characters from chars (each
 * character can only be used once).
 * 
 * Return the sum of lengths of all good strings in words.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: words = ["cat","bt","hat","tree"], chars = "atach"
 * Output: 6
 * Explanation: 
 * The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 =
 * 6.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
 * Output: 10
 * Explanation: 
 * The strings that can be formed are "hello" and "world" so the answer is 5 +
 * 5 = 10.
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= words.length <= 1000
 * 1 <= words[i].length, chars.length <= 100
 * All strings contain lowercase English letters only.
 * 
 */
/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 */

var char_counter = function(chars) {
    var res = list(26, 0);
    for (var c of chars)
        res[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
    return res;
}

var countCharacters = function(words, chars) {
    var cntchars = char_counter(chars),
        res = 0;
    // print(cntchars);
    for (var w of words) {
        var cnttmp = char_counter(w),
            valid = true;
        for (var c of w) {
            let idx = c.charCodeAt(0) - 'a'.charCodeAt(0);
            if (cnttmp[idx] > cntchars[idx]) {
                valid = false;
                break;
            }
        }

        if (valid) {
            res += len(w);
        }
    }
    return res;
};
var words = ["cat", "bt", "hat", "tree"],
    chars = "atach";
words = ["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin", "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb", "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl", "boygirdlggnh", "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx", "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop", "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx", "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr", "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo", "oxgaskztzroxuntiwlfyufddl", "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp", "qnagrpfzlyrouolqquytwnwnsqnmuzphne", "eeilfdaookieawrrbvtnqfzcricvhpiv", "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz", "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue", "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv", "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo", "teyygdmmyadppuopvqdodaczob", "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs", "qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"];
chars = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp";
print(countCharacters(words, chars));


