from django.shortcuts import render
from django.http import HttpRequest

content = str()
info = str()
newsIds = []

def home(request: HttpRequest):
	global content
	content = ''
	return render(request, 'search.html', {'searchFlag': False})

indexDirectory = '../index/'
newsDirectory = '../news/'

import os
import time



from django.core.paginator import Paginator

def search():
	global newsIds
	global info
	start = time.clock()
	filename = indexDirectory + content + '_index.txt'
	if os.path.exists(filename):
		with open(filename, 'r') as f:
			newsIds = f.read().strip().split(' ')
			info = '共找到 %d 条消息，用时 %f 秒' % (len(newsIds), time.clock() - start)
	else:
		info = '未找到相关新闻'
		newsIds = []
	# p = Paginator(newsIds, 10)
	# newsInfos = []
	# for newsId in newsIds:
	# 	with open(newsDirectory + newsId + '.txt') as f:
	# 		title = f.readline()
	# 		pubTime = f.readline()
	# 		body = f.read()
	# 		url = '/news/' + newsId
	# 		if len(body) > 100:
	# 			body = body[0:100] + '……'
	# 		newsInfos.append((title, pubTime, body, url, ))
	# context = {}
	# context['searchFlag'] = True
	# context['content'] = content
	# context['newsInfos'] = newsInfos
	# context['info'] = info
	# return render(request, 'search.html', context)

def display(request: HttpRequest):
	global content
	global info
	if content != request.GET['content']:
		content = request.GET['content']
		search()
	paginator = Paginator(newsIds, 10)
	if 'pagenum' in request.GET:
		pagenum = request.GET['pagenum']
	else:
		pagenum = 1
	
	page = paginator.page(pagenum)
	newsInfos = []
	for newsId in page:
		with open(newsDirectory + newsId + '.txt') as f:
			title = f.readline()
			pubTime = f.readline()
			body = f.read()
			url = '/news/' + newsId
			if len(body) > 100:
				body = body[0:100] + '……'
			newsInfos.append((title, pubTime, body, url, ))
	return render(request, 'search.html', {
		'info': info,
		'content': content,
		'newsInfos': newsInfos,
		'page': page,
		'searchFlag': True
	})
	