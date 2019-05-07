#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import urllib
import json
import socket
import urllib.request
import urllib.parse
import urllib.error

# 设置超时
import time
import string
import config as cfg

DEFAULT_IMAGE_DIR = "./images"
DEFAULT_IMAGE_SUFFIX = ".jpg"

class Crawler:
    __interval_time = 0.1   # 两次执行下载图片动作之间时间间隔
    __amount = 0            # 抓取图片的总数
    __start_amount = 0      # 开始下载的位置
    __counter = 0           # 当前已经下载的数量
    __image_dir = "./images/"
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}

    def __init__(self, interval):
        self.__interval_time = interval
        
    def load_config(self):
        print ("\n-  ------ IMAGE SPIDER SETUP ------  -\n")
        socket.setdefaulttimeout(cfg.CRAWL_TIMEOUT)

        if not os.path.isdir(DEFAULT_IMAGE_DIR):
            os.mkdir(DEFAULT_IMAGE_DIR)

        if cfg.CRAWL_SAVE_DIR == "auto":
            serial_number = ("%03d" % len(os.listdir(self.__image_dir)))
            self.__image_dir = self.__image_dir + serial_number + str("_") + cfg.CRAWL_KEYWORD
        else:
            self.__image_dir = self.__image_dir + cfg.CRAWL_SAVE_DIR

        if not os.path.exists(self.__image_dir):
            os.makedirs(self.__image_dir)

        self.__counter = len(os.listdir(self.__image_dir))

        if cfg.CRAWL_MODE == "continue":
            self.__amount = cfg.CRAWL_TOTAL
        elif cfg.CRAWL_MODE == "append":
            self.__amount = self.__counter + cfg.CRAWL_TOTAL
        else:
            print ("  CRAWL MODE", cfg.CRAWL_MODE, "is not exist")
            os._exit(-1)

        
        if cfg.CRAWL_IMAGE_SUFFIX != "auto" and self.suffix_is_support(cfg.CRAWL_IMAGE_SUFFIX) == False:
            print ("  IMAGE SUFFIX", cfg.CRAWL_IMAGE_SUFFIX, "is not support")
            os._exit(-1)


        print ( ( "  CRAWL KEYWORD: \"%s\"" ) % ( cfg.CRAWL_KEYWORD ))
        print ("  SAVE TO: ", self.__image_dir)
        print ("  HAVE DOWNLOADED: ", self.__counter)
        print ("  WILL BE DOWNLOAD: ", self.__amount - self.__counter)
        print ("  IMAGE FORMAT: ", cfg.CRAWL_IMAGE_SUFFIX)
        print ("  TIMEOUT: ", cfg.CRAWL_TIMEOUT)
        return
    
    def suffix_is_support(sefl, suffix):
        if cfg.CRAWL_IMAGE_SUFFIX not in {".jpg", ".jpeg", ".png", ".bmp", ".xbm", ".git", ".rgb", ".tiff", ".pgm", ".pbm"}:
            return False
        return True
        
    # 获取后缀名
    def get_suffix(self, image_name):
        if cfg.CRAWL_IMAGE_SUFFIX == "auto":
            suffix =  os.path.splitext(image_name)[-1]
            if self.suffix_is_support(suffix) == True:
                return suffix
            else:
                return DEFAULT_IMAGE_SUFFIX

        return cfg.CRAWL_IMAGE_SUFFIX

    # 获取referrer，用于生成referrer
    def get_referrer(self, url):
        par = urllib.parse.urlparse(url)
        if par.scheme:
            return par.scheme + '://' + par.netloc
        else:
            return par.netloc

    # 保存图片
    def save_image(self, rsp_data, word):
        # 判断名字是否重复，获取图片长度
        for image_info in rsp_data['imgs']:

            if self.__counter >= self.__amount:
                print ("\n-  ------  --- Complete ---  ------  -\n")
                os._exit(0)

            try:
                time.sleep(self.__interval_time * 2)

                img_url = image_info['objURL'] # utf-8 enconding, not support chinese
                img_url_chieses_extend = urllib.parse.quote(img_url, safe = string.printable)

                # 指定UA和referrer，减少403
                refer = self.get_referrer(img_url_chieses_extend)
                opener = urllib.request.build_opener()
                opener.addheaders = [
                    ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'),
                    ('Referer', refer)
                ]
                urllib.request.install_opener(opener)

                # 保存图片
                img_path = ("%s/%06d%s") % (self.__image_dir, self.__counter, self.get_suffix(refer))
                urllib.request.urlretrieve(img_url_chieses_extend, img_path)

            except urllib.error.HTTPError as urllib_err:
                print(urllib_err, "Discard: ", img_url)
                continue
            except Exception as err:
                time.sleep(1)
                print(err, " Discard: ", img_url)
                continue
            else:
                print (( "Catched %s < %s") % (os.path.basename(img_path), img_url))
                self.__counter += 1
                    
        return

    # 开始获取
    def get_images(self, word):
        search = urllib.parse.quote(word)
        # pn int 图片数
        pn = self.__start_amount
        while True:

            url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=' + search + '&cg=girl&pn=' + str(
                pn) + '&rn=60&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'

            # 设置header防ban
            try:
                time.sleep(self.__interval_time)
                req = urllib.request.Request(url=url, headers=self.headers)
                page = urllib.request.urlopen(req)
                content = page.read();
                
            except UnicodeDecodeError as e:
                print(e)
                print('-----UnicodeDecodeErrorurl:', url)
            except urllib.error.URLError as e:
                print(e)
                print("-----urlErrorurl:", url)
            except socket.timeout as e:
                print(e)
                print("-----socket timout:", url)
            else:
                rsp_data = json.loads(str(content, encoding='utf-8'), strict=False) # 解析json
                self.save_image(rsp_data, word)
                pn += 60 # 读取下一页

            finally:
                page.close()

        return

    def start(self):
        print ("\n-  ------ -- START CRAWL -- -------  -\n")
        self.get_images(cfg.CRAWL_KEYWORD)


if __name__ == '__main__':
    crawler = Crawler(0.1)  # 抓取延迟为 0.05
    crawler.load_config()
    crawler.start()
