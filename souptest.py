from bs4 import BeautifulSoup
MyHtml = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>handsome boy</title>
</head>
<h1>这个字体比较大</h1>
<h1>this is another h1</h1>
<h2>this letter is smaller</h2>
<p>this is my first html contents</p>
<body>

</body>
</html>'''
soup = BeautifulSoup(MyHtml,'html.parser')
Myh1 = soup.findAll('h1')
for i in Myh1:
    if 'another' in i.string:
        print(i.string)