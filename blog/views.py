from django.shortcuts import render, get_object_or_404
from blog.models import article


def blog_index_view(request):
	all_articles = article.objects.all()
	return render(request, 'blog/index.html', {"articles": all_articles})


def blog_post_view(request, pk):
	the_article = get_object_or_404(article, pk=pk)
	the_article.views += 1
	the_article.save()
	return render(request, 'blog/article.html', {"article": the_article})


def super_user_view(request):
	if request.user.is_authenticated:
		return render(request, "blog/superuser.html")
	else:
		return render(request, "blog/superuser_login.html")
