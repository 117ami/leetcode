# coding: gbk

# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# click to show corner cases.
#
# Corner Cases:
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".
# =

# @param {String} path
# @return {String}
def simplify_path(path)
  stack = []
  path.split('/').each do |pp|
    next if pp == '.' || pp == ''
    if pp == '..'
      stack.pop
    else
      stack << pp
    end
  end
  return '/' if stack.empty?
  stack.unshift('') if stack[0] != '' || stack.size == 1
  stack.join('/')
end

pa = '/home/'
pa = 'home//foo/'
# pa = 'home/foo'
# pa = "/a/./b/../../c/"
# pa = '/////.'
p pa.split('/')
p simplify_path(pa)
