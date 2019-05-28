from django.shortcuts import render
from .models import Movies
from django.http import HttpResponse

# 127.0.0.1:8000/ex05/populate
def populate(request):
	try:

		svg_title = 'The Phantom Menace'
		try:
			test_exist = Movies.objects.get(pk = 1)
		except ObjectDoesNotExist:		
			Movies_insert = Movies(
					title = 'The Phantom Menace ',
					episode_nb = 1,
					opening_crawl = '',
					director = 'George Lucas',
					producer = 'Rick McCallum',
					release_date = '1999-05-19')
			Movies_insert.save()
			insert_return = "ok<br>"
		insert_return = "l'episode numero {} exite deja<br>".format(svg_title)

		svg_title = 'Attack of the Clones'
		try:
			test_exist = Movies.objects.get(pk = 2)
		except ObjectDoesNotExist:			
			Movies_insert, created = Movies.objects.get_or_create(
					title = 'Attack of the Clones',
					episode_nb = 2,
					opening_crawl = '',
					director = 'George Lucas',
					producer = 'Rick McCallum',
					release_date = '2002-05-16')
			Movies_insert.save()
			insert_return = insert_return + "ok<br>"
		insert_return = insert_return + "l'episode numero {} exite deja<br>".format(svg_title)

		svg_title = 'Revenge of the Sith'
		try:
			test_exist = Movies.objects.get(pk = 3)
		except ObjectDoesNotExist:	
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
		try:
			test_exist = Movies.objects.get(pk = 4)
		except ObjectDoesNotExist:	
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
		try:
			test_exist = Movies.objects.get(pk = 5)
		except ObjectDoesNotExist:	
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
		try:
			test_exist = Movies.objects.get(pk = 6)
		except ObjectDoesNotExist:	
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
		try:
			test_exist = Movies.objects.get(pk = 7)
		except ObjectDoesNotExist:	
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
		return HttpResponse("Erreur grave sur le titre {}<br>Erreur {}".format(svg_title,e))

	return HttpResponse(insert_return)


# 127.0.0.1:8000/ex05/display
def display(request):

	try:
		select_response = Movies.objects.all()
		
		if response:
			select_return = "<table>"
			select_return = select_return + '<td>title</td><td> episode </td><td> opening_craw </td> </td><td> directed </td> <td> producer </td><td> released </td>'
			for row in response:
				each_row = '<td> {} </td><td> {} </td><td> {} </td> </td><td> {}</td> <td> {}</td> <td>{}</td>'.format(row[0], row[1], row[2], row[3], row[4], row[5])
				select_return = select_return + "<tr>" + each_row + "</tr>"
			select_return = select_return + "</table>"
		else: 
			select_return = "No data Available"

	except Exception as e:
		return HttpResponse("{}".format(e))

	return HttpResponse(select_return)


# 127.0.0.1:8000/ex05/display
def remove(request):
	pass
