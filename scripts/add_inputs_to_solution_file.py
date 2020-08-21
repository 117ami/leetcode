import re
import sys

global_vars = []


def _oneline_formatter(st, lang='python'):
    global global_vars
    if lang == 'cpp':
        st = st.replace('[', '{').replace(']', '}')

    variable_names, data = [], []
    pre_comma_index, pre_equal_index = -1, 0
    ret = ""
    for i, c in enumerate(st):
        if c == ',':
            pre_comma_index = i
        elif c == '=':
            variable_names.append(st[pre_comma_index + 1:i].strip())
            if pre_comma_index > 0:
                data.append(st[pre_equal_index + 1:pre_comma_index].strip())
            pre_equal_index = i
        elif c == ';':
            data.append(st[pre_equal_index + 1:i].strip())
    if lang == 'python':
        return ', '.join(variable_names) + " = " + ', '.join(data)
    else:
        for i, var in enumerate(variable_names):
            dtype = 'string' if '"' in data[i] else 'int'
            if data[i].startswith("{{"):
                ret += f"std::vector<vector<{dtype}>> {var} = {data[i]} ;\n"
            elif data[i].startswith("{"):
                ret += f"std::vector<{dtype}> {var} = {data[i]} ;\n"
            else:
                ret += f"{dtype} {var} = {data[i]} ;\n"
    global_vars = variable_names
    return ret


tmpfile = open('tmp.file', 'r').read()
sinputs = re.findall(r'Input:(.*?)Output', tmpfile, re.DOTALL)
for i, s in enumerate(sinputs):
    ss = s.replace('\n', ' ').strip() + ';'
    print(_oneline_formatter(ss))
    cpp_s = _oneline_formatter(ss, 'cpp')

    mode = 'a' if i > 0 else 'w'
    open('cpp_testcases.tmpfile', mode).write(cpp_s + '\n')

# Add function name
python_file = sys.argv[1]
with open(python_file, 'r') as f:
    for l in f.readlines():
        if 'def' in l and 'self' in l:
            func_name = re.search(r"def (.*)\(", l.strip())
            args = ', '.join(global_vars)
            extra_line = f'print(sol.{func_name[1]}({args}))'
            print(extra_line)
