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

var sort_by_last = function(arr){
    return arr.sort((a, b)=>(last(a) - last(b)));
}

var sort_by_first = function(arr){
    return arr.sort((a, b)=>(a[0] - b[0]));
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
    return a.map(function(e, i){return [e, b[i]];});
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


var div = function(n, k) { return floor(n / k); }

// inclusive of both endpoints
var randint = function(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

var isin = function(s1, s2) {
    return s1.includes(s2);
}


/*
 * @lc app=leetcode id=950 lang=javascript
 *
 * [950] Reveal Cards In Increasing Order
 *
 * https://leetcode.com/problems/reveal-cards-in-increasing-order/description/
 *
 * algorithms
 * Medium (72.57%)
 * Total Accepted:    17K
 * Total Submissions: 23.4K
 * Testcase Example:  '[17,13,11,2,3,5,7]'
 *
 * In a deck of cards, every card has a unique integer.  You can order the deck
 * in any order you want.
 * 
 * Initially, all the cards start face down (unrevealed) in one deck.
 * 
 * Now, you do the following steps repeatedly, until all cards are
 * revealed:
 * 
 * 
 * Take the top card of the deck, reveal it, and take it out of the deck.
 * If there are still cards in the deck, put the next top card of the deck at
 * the bottom of the deck.
 * If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
 * 
 * 
 * Return an ordering of the deck that would reveal the cards in increasing
 * order.
 * 
 * The first entry in the answer is considered to be the top of the deck.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [17,13,11,2,3,5,7]
 * Output: [2,13,3,11,5,17,7]
 * Explanation: 
 * We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter),
 * and reorder it.
 * After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top
 * of the deck.
 * We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
 * We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
 * We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
 * We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
 * We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
 * We reveal 13, and move 17 to the bottom.  The deck is now [17].
 * We reveal 17.
 * Since all the cards revealed are in increasing order, the answer is
 * correct.
 * 
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 1 <= A.length <= 1000
 * 1 <= A[i] <= 10^6
 * A[i] != A[j] for all i != j
 * 
 * 
 * 
 * 
 */
/**
 * @param {number[]} deck
 * @return {number[]}
 */
var deckRevealedIncreasing = function(deck) {
    sorted(deck); 
    var deq = [last(deck)]; 
    for (var i = len(deck) - 2; i >= 0 ; i --) {
        deq.splice(0, 0, last(deq)); 
        deq.pop(); 
        deq.splice(0, 0, deck[i]);
    }
    return deq; 
};


print(deckRevealedIncreasing([17,13,11,2,3,5,7]));

