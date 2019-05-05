# ImageSpider

<hr>

[TOC]



## 1. 运行环境： 

>  Python 3



## 2. 使用方法

> 修改 config.py 文件中的 **CRAWL_KEYWORD** 和 **CRAWL_TOTAL** 

``` python
# file: config.py

CRAWL_KEYWORD = "七龙珠"          # 爬取图片使用的搜索关键字

CRAWL_TOTAL = 20                 # 爬取图片的总量
CRAWL_MODE = "continue"          # [continue|append] , apppend 追加下载 TOTAL 张图片， continue 只下载 TOTAL 张图片
CRAWL_SAVE_DIR = "auto"          # [auto] is XXX_CRAWL_KEYWORD
CRAWL_IMAGE_SUFFIX = ".jpg"      # value "auto" is save as origin format
CRAWL_TIMEOUT = 5             
```

> 然后执行

```bash
python3 crawl_baidu.py
```

> 爬取到的图片将保存在工程根目录下的 ***image*** 下



## 3. 效果

```bash
$ python3 crawl_baidu.py 

-  ------ IMAGE SPIDER SETUP ------  -

  CRAWL KEYWORD: "七龙珠"
  SAVE TO:  ./images/七龙珠
  HAVE DOWNLOADED:  0
  WILL BE DOWNLOAD:  20
  IMAGE FORMAT:  .jpg
  TIMEOUT:  5

-  ------ -- START CRAWL -- -------  -

HTTP Error 403: Forbidden Discard:  http://hbimg.b0.upaiyun.com/6a75f7fdd49ce7b7711afdbdf3c5f22773d7c24013cff-CVmbhn_fw658
Catched 000000.jpg < http://image.tupian114.com/20130514/11281510.jpg
Catched 000001.jpg < http://img3.duitang.com/uploads/item/201409/10/20140910211009_mwmfG.thumb.700_0.jpeg
HTTP Error 403: Forbidden Discard:  http://hbimg.b0.upaiyun.com/23abe6db85a2a459aef5ef23404cf5fa97ab8f27286da-1fwpJ1_fw658
Catched 000002.jpg < http://b-ssl.duitang.com/uploads/item/201607/25/20160725091110_KskjH.jpeg
Catched 000003.jpg < http://www.animen.com.tw/FilesUpload/CK-Images/151116_9_15.jpg
Catched 000004.jpg < http://cdn.duitang.com/uploads/item/201607/25/20160725091600_UCezt.thumb.700_0.jpeg
Catched 000005.jpg < http://img3.duitang.com/uploads/item/201205/29/20120529153509_5s2u8.thumb.700_0.jpeg
Catched 000006.jpg < http://img5.duitang.com/uploads/item/201309/27/20130927005220_JsTrM.thumb.700_0.jpeg
Catched 000007.jpg < http://b-ssl.duitang.com/uploads/item/201607/25/20160725091422_fjKGX.jpeg
HTTP Error 403: Forbidden Discard:  http://hbimg.b0.upaiyun.com/c9964fdd1c6cc7ed94ff82fa6d360b06b933c26d116cf-ZJqQbS_fw658
Catched 000008.jpg < http://b-ssl.duitang.com/uploads/item/201705/31/20170531235052_XQ4wf.png
HTTP Error 404: Not Found Discard:  http://a4.att.hudong.com/61/42/31300543240754143926426776724.jpg
Catched 000009.jpg < http://b-ssl.duitang.com/uploads/item/201712/09/20171209200918_BFJ5n.png
Catched 000010.jpg < http://b-ssl.duitang.com/uploads/item/201706/26/20170626194734_dt3fL.thumb.700_0.jpeg
Catched 000011.jpg < http://b-ssl.duitang.com/uploads/item/201805/29/20180529194524_kjdtu.thumb.700_0.jpg
Catched 000012.jpg < http://pic9.nipic.com/20100912/3355022_183800001499_2.png
Catched 000013.jpg < http://b-ssl.duitang.com/uploads/item/201412/20/20141220160459_RAuyY.jpeg
Catched 000014.jpg < http://b-ssl.duitang.com/uploads/item/201807/25/20180725221908_ilyht.jpeg
Catched 000015.jpg < http://t-1.tuzhan.com/a581c948c7d4/c-2/l/2013/05/30/09/e49f961f80a741b2b75e32a02de86d8e.jpg
Catched 000016.jpg < http://b-ssl.duitang.com/uploads/item/201803/13/20180313065241_sYVn8.thumb.700_0.jpeg
HTTP Error 403: Forbidden Discard:  http://hbimg.b0.upaiyun.com/57674bfaf08dc0752781edb0770fb05b5fd80c571a6f8-QkeqX2_fw658
Catched 000017.jpg < http://images.ali213.net/picfile/pic/2012-08-22/927_956275557.jpg
Catched 000018.jpg < http://b-ssl.duitang.com/uploads/item/201706/01/20170601153542_zeaZ8.thumb.700_0.png
Catched 000019.jpg < http://imgsrc.baidu.com/forum/w=580/sign=bbe25aeed258ccbf1bbcb53229d9bcd4/58dcd72a6059252ddc16ee58379b033b5bb5b90a.jpg

-  ------  --- Complete ---  ------  -


```

![exampe one](https://raw.githubusercontent.com/red-stream/ImageSpider/master/images/exampe_1.png)

![exampe two](https://raw.githubusercontent.com/red-stream/ImageSpider/master/images/exampe_2.png)


## 4. 欢迎反馈使用过程中的问题与BUG
