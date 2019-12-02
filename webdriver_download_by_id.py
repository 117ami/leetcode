from selenium import webdriver
import sys
import os
from bs4 import BeautifulSoup
import time

def read_by_id(id='1024'):
    text = []
    c = webdriver.Chrome()
    c.get('https://leetcode.com/problemset/all/?search={}'.format(id))

    soup = BeautifulSoup(c.page_source, 'lxml')
    first_match = [
        e for e in soup.findAll('a') if e.attrs.get(
            'href', '').startswith('/problems/')][1]

    problem_url = 'https://leetcode.com' + first_match.attrs['href']
    text.append(problem_url)

    c.get(problem_url)
    while all([tag not in c.page_source for tag in ['"hard"', '"medium"', '"easy"']]):
        time.sleep(3)

    soup = BeautifulSoup(c.page_source, 'lxml')
    diff = soup.find('div', {'diff': ["hard", "medium", "easy"]}).text
    text.append(diff + " (Difficulty)\n")

    ps = soup.findAll('p') + soup.findAll('pre')
    for p in ps:
        text += p.text.split('\n')

    c.quit
    return text


def generate_python(text, id='1024'):
    fn = '{}.{}.py'.format(
        id,
        text[0].replace(
            'https://leetcode.com/problems/',
            '').replace(
            '/',
            '').replace(
                '-',
            '_'))

    with open(fn, 'w') as f:
        for t in text:
            f.write("# " + t + "\n")


def generate_cpp(text, id='1024'):
    fn = '{}.{}.cpp'.format(
        id,
        text[0].replace(
            'https://leetcode.com/problems/',
            '').replace(
            '/',
            '').replace(
                '-',
            '_'))

    with open(fn, 'w') as f:
        for t in text:
            f.write("// " + t + "\n")

    os.system("echo '#include \"aux.cpp\"' > test.cpp")
    os.system('cat c.cpp >> test.cpp')
    
    with open('test.cpp', 'a') as f:
        f.write('#include \"{}\"\n\n'.format(fn))
        ss = """int main(int argc, char const *argv[]) {
	    Solution s;
	    return 0;
}
        """
        f.write(ss)

if __name__ == "__main__":
    id = sys.argv[1].rstrip()
    text = read_by_id(id)
    generate_cpp(text, id)
    generate_python(text, id)
