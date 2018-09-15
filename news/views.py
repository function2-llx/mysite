from django.shortcuts import render

newsDirectory = '../news/'

def displayNews(request, newsId: int):
	context = {}
	with open(newsDirectory + str(newsId) + '.txt', 'r') as f:
		context['title'] = f.readline()
		context['pubtime'] = f.readline()
		context['body'] = f.read()
	
	return render(request, 'news.html', context)
