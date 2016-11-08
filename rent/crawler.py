html_doc = """
<html><head><title>Hello</title></head>
<body>
<p class="title">Hello world</p>

<p class="story">Hello,Hello,Hello
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, "html.parser")

print(soup.title)