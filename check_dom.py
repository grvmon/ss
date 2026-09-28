from bs4 import BeautifulSoup

with open('self-storage-calculator/index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

bar = soup.find(id='calc-mobile-bar')
path = []
curr = bar
while curr and curr.name != '[document]':
    path.append(curr.name)
    curr = curr.parent

print(" -> ".join(path[::-1]))
