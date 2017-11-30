# -*- coding:utf-8 -*-
__author__ = "YXY"

import urllib.request
import re

class BDTB:

    def __init__(self, baseUrl, seeLZ, floorTag):
        self.base_url = baseUrl
        self.default_title = "百度贴吧"
        self.file = None
        self.seeLZ = seeLZ
        self.page_index = 1
        self.content_num = 1
        self.floor = 1
        self.floorTag = floorTag
        self.defaultTitle = "百度贴吧"

    def getPage(self, pageNum):
        try:
            url = self.base_url + "?see_lz=" + str(self.seeLZ) + '&pn=' + str(pageNum)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            return response.read().decode('utf-8')
        except urllib.request.URLError as e:
            if hasattr(e, "reason"):
                print("出错辣！", e.reason)
            return None

    def getTitle(self, page_html):
        title_pattern = re.compile('<h3.*?>(.*?)</h3>', re.S)
        result = re.search(title_pattern, page_html)
        if result:
            #print(result.group(1))
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self, page_html):
        pagenum_pattern = re.compile('<li class="l_reply_num".*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pagenum_pattern, page_html)
        if result:
            #print(result.group(1))
            return int(result.group(1))
        else:
            return None

    def getContent(self, page_html):
        content_pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        result = re.findall(content_pattern, page_html)
        if result:
            content = self.replace(result)
            return content
        else:
            return None

    def replace(self, result):
        str_contents = []
        for content in result:
            item = re.sub('''<img.*?>|<br>''', "\n", content)
            item = re.sub('''<a href.*?>|</a>| {4,7}''', "", item)
            str_contents.append(item.strip())
        return str_contents

    def setFileTitle(self, title):
        # 如果标题不是为None，即成功获取到标题
        if title is not None:
            self.file = open(title + ".txt", "w+")
        else:
            self.file = open(self.defaultTitle + ".txt", "w+")

    def writeData(self, contents):
        # 向文件写入每一楼的信息
        for item in contents:
            floorLine = "\n\n" + u"------------------------------  " + str(self.floor) + " Floor" + u"  ------------------------------\n\n"
            self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1

    def start(self):
        indexPage = self.getPage(1)
        indexcontent = self.getContent(indexPage)
        #print(indexcontent)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print("URL已失效，请重试")
            return
        print("该帖子共有" + str(pageNum) + "页")

        #print(self.getContent(indexPage))

        for i in range(1, pageNum + 1):
            print("正在写入第" + str(i) + "页数据")
            page = self.getPage(i)
            #print(self.getContent(page))
            contents = self.getContent(page)
            self.writeData(contents)

baseUrl = "http://tieba.baidu.com/p/5435414830"
seeLZ = 1
floorTag = 1
bdtb = BDTB(baseUrl, seeLZ, floorTag)
bdtb.start()