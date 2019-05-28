from django.shortcuts import render
from .models import Movies
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# 127.0.0.1:8000/ex03/populate
def populate(request):
	try:

		svg_title = 'The Phantom Menace'
		Movies_insert = Movies(
				title = 'The Phantom Menace ',
				episode_nb = 1,
				opening_crawl = '',
				director = 'George Lucas',
				producer = 'Rick McCallum',
				release_date = '1999-05-19')
		Movies_insert.save()
		insert_return = "ok<br>"

		svg_title = 'Attack of the Clones'
		Movies_insert = Movies(
				title = 'Attack of the Clones',
				episode_nb = 2,
				opening_crawl = '',
				director = 'George Lucas',
				producer = 'Rick McCallum',
				release_date = '2002-05-16')
		Movies_insert.save()
		insert_return = insert_return + "ok<br>"

		svg_title = 'Revenge of the Sith'
		Movies_insert = Movies(
				title = 'Revenge of the Sith',
				episode_nb = 3,
				opening_crawl = '',
				director = 'George Lucas',
				producer = 'Rick McCallum',
				release_date = '2005-05-19')
		Movies_insert.save()
		insert_return = insert_return + "ok<br>"

		svg_title = 'A New Hope'
		Movies_insert = Movies(
				title = 'A New Hope',
				episode_nb = 4,
				opening_crawl = '',
				director = 'George Lucas',
				producer = 'Gary Kurtz, Rick McCallum ',
				release_date = '1977-05-25')
		Movies_insert.save()
		insert_return = insert_return + "ok<br>"

		svg_title = 'The Empire Strikes Back'
		Movies_insert = Movies(
				title = 'The Empire Strikes Back',
				episode_nb = 5,
				opening_crawl = '',
				director = 'Irvin Kershner',
				producer = ' Gary Kutz, Rick McCallum',
				release_date = '1980-05-17')
		Movies_insert.save()
		insert_return = insert_return + "ok<br>"

		svg_title = 'Return of the Jedi'
		Movies_insert = Movies(
				title = 'Return of the Jedi',
				episode_nb = 6,
				opening_crawl = '',
				director = 'Richard Marquand',
				producer = 'Howard G. Kazanjian, George Lucas, Rick McCallum',
				release_date = '1983-05-25')
		Movies_insert.save()
		insert_return = insert_return + "ok<br>"

		svg_title = 'The Force Awakens'
		Movies_insert = Movies(
				title = 'The Force Awakens',
				episode_nb = 7,
				opening_crawl = '',
				director = 'J. J. Abrams',
				producer = 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
				release_date = '2015-12-11')
		Movies_insert.save()
		insert_return = insert_return + "ok<br>"

	except Exception as e:
		return HttpResponse("Le titre non insere est {}<br>erreur{}".format(svg_title,e))

	return HttpResponse(insert_return)


# 127.0.0.1:8000/ex03/display
def display(request):

	try:
		select_response = Movies.objects.all()
		
		if select_response:
			select_return = "<table>"
			for row in select_response:
				each_row = 'title : {} -- episode_nb : {} -- opening_craw {} -- directed by {}-- producer by {}-- released by {}'.format(row.title, row.episode_nb, row.opening_crawl, row.director, row.producer, row.release_date)
				select_return = select_return + "<tr><td>" + each_row + "</td></tr><br>"
			select_return = select_return + "</table>"
		else: 
			select_return = "No data Available"

	except Exception as e:
		return HttpResponse("{}".format(e))

	return HttpResponse(select_return)

# Create your views here.
