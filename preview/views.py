from django.shortcuts import render

tot = 15

lim = 10000

def displayList(request, pagenum: int = 0):
	if not pagenum:
		pagenum = 0
	else:
		pagenum = int(pagenum)
	start = pagenum * tot
	infoList = []
	for i in range(tot):
		cur = start + i
		if cur >= lim:
			break
		with open('../news/%d.txt' % cur, 'r') as f:
			infoList.append((f.readline(), f.readline(), '/news/%d' % cur))

	return render(request, 'preview.html', {
		'infoList': infoList
	})
