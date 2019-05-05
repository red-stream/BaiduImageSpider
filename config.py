#!/usr/bin/env python
# -*- coding:utf-8 -*-

CRAWL_KEYWORD = "七龙珠"          # 爬取图片使用的搜索关键字

CRAWL_TOTAL = 20               # 爬取图片的总量
CRAWL_MODE = "continue"         # [continue|append] , apppend 追加下载 TOTAL 张图片， continue 只下载 TOTAL 张图片
CRAWL_SAVE_DIR = "auto"         # [auto] is XXX_CRAWL_KEYWORD
CRAWL_IMAGE_SUFFIX = ".jpg"     # value "auto" is save as origin format
CRAWL_TIMEOUT = 5             
