#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/21 10:42
# @Author  : name
# @File    : 02.线程池在爬虫案例中的应用.py
import requests
from lxml import etree
import re
import os
from multiprocessing.dummy import Pool
#需求：爬取梨视频的视频教程

def get_urls():
    '''
    :return: return urls# 储存所有视频的链接和名字
    '''

    # 1.获取到通往各个视频的url (非视频下载链接)
    url = 'https://www.pearvideo.com/category_5'
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    a_list = tree.xpath('//*[@id="listvideoList"]/ul/li/div/a')  # 得到相应的a标签
    urls = []  # 储存所有视频的连接和名字
    for a in a_list:
        video_href = 'https://www.pearvideo.com/' + a.xpath('./@href')[0]
        video_name = a.xpath('./div[2]/text()')[0] + '.mp4'
        contId = re.findall(r'\d+', a.xpath('./@href')[0])[0]  # '1720760'
        # print(contId)

        # 2.获取各个视频的下载链接
        request_url = 'https://www.pearvideo.com/videoStatus.jsp'
        data = {
            'contId': contId
        }
        # 在header中加入'Referer'就不会显示该视频已下架
        ajax_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
            'Referer': 'https://www.pearvideo.com/video_' + contId
        }
        res_json = requests.get(url=request_url, headers=ajax_headers, params=data).json()
        # print(res_json)
        video_url = res_json['videoInfo']['videos']['srcUrl']
        # 此处视频地址做了加密即ajax中得到的地址需要加上cont -, 并且修改一段数字为id才是真地址
        # 真地址："https://video.pearvideo.com/mp4/adshort/20210220/cont-1720760-15611215_adpkg-ad_hd.mp4"
        # 伪地址："https://video.pearvideo.com/mp4/adshort/20210220/1613883904693-15611215_adpkg-ad_hd.mp4"

        # 开始拼接 (不要被这个吓到，慢慢来很简单的)
        # ['https:', '', 'video.pearvideo.com', 'mp4', 'adshort', '20210220', '1613883904693-15611215_adpkg-ad_hd.mp4']
        tmp = video_url.split('/')
        # 'https://video.pearvideo.com/mp4/adshort/20210220/cont-1720760-'
        real_url_tmp = tmp[0] + '//' + tmp[2] + '/' + tmp[3] + '/' + tmp[4] + '/' + tmp[
            5] + '/' + 'cont-' + contId + '-'
        # ['https://video.pearvideo.com/mp4/adshort/20210220/1613883904693', '15611215_adpkg', 'ad_hd.mp4']
        tmp2 = video_url.split('-')
        real_url = real_url_tmp + tmp2[1] + '-' + tmp2[2]
        dict = {
            'name': video_name,
            'url': real_url
        }
        urls.append(dict)
    return urls

# 使用线程池对视频数据进行请求(较为耗时的阻塞操作)
def get_video_data(dict):
    url = dict['url']
    print(dict['name'], '正在下载...')
    video_data = requests.get(url=url, headers=headers).content
    video_path = './video/' + dict['name']
    with open(video_path, 'wb') as fp:
        fp.write(video_data)
        print(dict['name'], '下载成功！')

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    if not os.path.exists('./video'):
        os.mkdir('./video')
    pool = Pool(4)
    urls = get_urls()
    pool.map(get_video_data, urls)

    pool.close()
    pool.join()

