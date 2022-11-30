# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 17:46:25 2022

@author: 16921
"""

# =============================================================================
# # 1. 爬虫
# 1 获取网页内容:网址发送请求,返回整个网页书库
# 2 解析网页内容:提取数据
# 3 保存数据
# 
# 
# Request(获取)+Beautiful Soup(解析)
# Biopython库(Entrez模块),pymed库
# 利用第三方库直接下载PDF
# 调用接口实现自动英译汉
# 
# Selenium(获取)+Beautiful Soup(解析)
# jiba等库进行自然语言分析获取领域热词
# 
# 爬取生信数据
# Biopython处理多种生物信息学问题
# pysam处理基因序列工具
# 
# # Robots 协议
# 
# # 2. 爬虫常用库
# Urllib库
#     + 
# Requests库
# 
# Selenium库
# =============================================================================

import requests
# 1. 无参数的get请求
# response=requests.get('http://www.baidu.com/')
# response.raise_for_status()
# response.encoding=response.apparent_encoding
# print(response.text)
# 2. 有参数的get请求
# url = 'http://www.baidu.com/s'
# response = requests.get(url,params={'wd':'python'})
# response.raise_for_status()
# response.encoding=response.apparent_encoding
# file = open('test.html','w',encoding='utf-8')
# file.write(response.text)
# file.close()
# Post请求
# data = {'dxy':'python','key2':'value2'}
# post = requests.post('http://httpbin.org/post', data=data)
# post.raise_for_status()
# post.encoding=post.apparent_encoding
# file = open('test1.html','w',encoding='utf-8')
# file.write(post.text)
# file.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time
import re
#---------------------------------
# 2. Selenium
# 驱动浏览器
# browser = webdriver.Chrome()

# # 访问网页
# browser.get('http://www.baidu.com')
# # 定位元素
# in_elem = browser.find_element(By.ID,'kw')
# sub_elem = browser.find_element(By.ID,'su')
# # 操作元素
# in_elem.send_keys("Python")
# time.sleep(3)
# # 鼠标操作
# chains = ActionChains(browser)
# chains.click(sub_elem).perform()
# # 截取屏幕
# time.sleep(5)
# browser.get_screenshot_as_file('./screen.png')
# ----------------
# 下拉栏操作
# browser.get('http://sahitest.com/demo/selectTest.htm')
# browser.implicitly_wait(10)
# pro = Select(browser.find_element(By.ID,'s1'))
# for opt in pro.options:
#     print(opt.text)
# pro.select_by_value('46')
# time.sleep(3)
# browser.get_screenshot_as_file("./edit.png")
# 关闭浏览器
# browser.close()
# ----------------------
response = requests.get('http://www.baidu.com/')
response.raise_for_status()
response.encoding = response.apparent_encoding
title = re.findall(r'<title>(.*?)</title>', response.text)
print(title[0])

