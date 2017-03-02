from django.shortcuts import render
from blog.models import article


def blog_index_view(request):
	all_articles = article.objects.all()
	return render(request, 'blog/index.html', {"articles": all_articles})
