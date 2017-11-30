
Baidu Tieba crawler
===============================

This is my first python web crawler project!

## Operating environment：

Ubuntu 16.04 LTS<br>
python 3.5<br>

## Use the project:
baseUrl = web address.<br>
seeLZ = Whether you only look at the landlord.<br>

## Module detailed solution
`def getPage(self, pageNum)`: input a page number, output html file. <br>
`def getTitle(self, page_html)`: input a html file, output a title of the file. <br>
`def getPageNum(self, page_html)`: input a html file, output total for page. <br>
`def getContent(self, page_html)`: input a html file, output the content of file. <br>
`def replace(self, result)`: input a content file, output delete other unrelated things. <br>
`def setFileTitle(self, title)`: inout a title, open a file and name it by title. <br>
`def writeData(self, contents)`: input a content file, and write this content to the file. <br>
`def start(self)`: the program begin. <br>

## Connect with me

- QQ:522278346
