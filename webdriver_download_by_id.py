from selenium import webdriver
import sys
import os
from bs4 import BeautifulSoup
import time

def read_by_id(id='1024'):
    text = []
    o = webdriver.chrome.options.Options()
    o.add_argument('--headless')
    c = webdriver.Chrome(options=o)
    c.get('https://leetcode.com/problemset/all/?search={}'.format(id))
    
    pro_hrefs = []
    while len(pro_hrefs) < 2:
        soup = BeautifulSoup(c.page_source, 'lxml')
        pro_hrefs = [e for e in soup.findAll('a') if e.attrs.get('href', '').startswith('/problems/')]
        time.sleep(1)

    first_match = pro_hrefs[1]
    problem_url = 'https://leetcode.com' + first_match.attrs['href']
    print('Problem link: {}'.format(problem_url))
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
    
    while 'ant-select-selection-selected-value' not in c.page_source:
        time.sleep(1)

    time.sleep(3)        
    c.find_element_by_xpath('//div[@class="ant-select-selection-selected-value"]').click()

    time.sleep(1)
    c.find_elements_by_xpath('//li[@class="ant-select-dropdown-menu-item"]')[2].click()  # Choose Python3
    pycode = BeautifulSoup(c.page_source, 'lxml').find('input', {'name': 'code'})['value'] # Python 3 Code
    # soup = BeautifulSoup(c.page_source, 'lxml')
    # py3code = soup.find('input', {'name': 'code'})
    text += pycode.split("\n")

    # print(c.page_source, text)
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
    print(">> DONE")