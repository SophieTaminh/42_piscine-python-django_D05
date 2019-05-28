from django.shortcuts import render
from .models import Movies
from django.http import HttpResponse


def init(request):
# 127.0.0.1:8000/ex04/init
	
	try:
		conn = psycopg2.connect(
			database = 'formationdjango',
			host = 'localhost',
			user = 'djangouser',
			password = 'secret'
			)

		curr = conn.cursor()

		curr.execute(""" CREATE TABLE IF NOT EXISTS ex04_movies (
			title VARCHAR(64) NOT NULL,
			episode_nb SERIAL PRIMARY KEY,
			opening_craw TEXT,
			director VARCHAR(32) NOT NULL,
			producer VARCHAR(128) NOT NULL,
			release_date DATE NOT NULL)""")
		conn.commit()

		conn.close()

	except Exception as e:
		return HttpResponse("{}".format(e))	
		
	return HttpResponse('ok')

# 127.0.0.1:8000/ex04/populate
try:
		conn = psycopg2.connect(
			database = 'formationdjango',
			host = 'localhost',
			user = 'djangouser',
			password = 'secret'
			)

		curr = conn.cursor()

		svg_title = 'The Phantom Menaces'
		curr.execute(""" INSERT INTO ex02_movies (title, episode_nb, opening_craw, director, producer, release_date) 
							VALUES
						('The Phantom Menace', 1, '', 'George Lucas', 'Rick McCallum', '1999-05-19')
					""")
		conn.commit()
		insertion_return = "ok <br>"

		svg_title = 'Attack of the Clones'
		curr.execute(""" INSERT INTO ex02_movies (title, episode_nb, opening_craw, director, producer, release_date) 
							VALUES
						('Attack of the Clones', 2, '', 'George Lucas', 'Rick McCallum', '2005-05-16')
					""")
		conn.commit()
		insertion_return = insertion_return + "ok <br>"

		svg_title = 'Revenge of the Sith'
		curr.execute(""" INSERT INTO ex02_movies (title, episode_nb, opening_craw, director, producer, release_date) 
							VALUES
						('Revenge of the Sith',3, '', 'George Lucas', 'Rick McCallum', '2005-05-19')
					""")
		conn.commit()
		insertion_return = insertion_return + "ok <br>"

		svg_title = 'A New Hope'
		curr.execute(""" INSERT INTO ex02_movies (title, episode_nb, opening_craw, director, producer, release_date) 
							VALUES
						('A New Hope',4, '', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25')
					""")
		conn.commit()
		insertion_return = insertion_return + "ok <br>"

		svg_title = 'The Empire Strikes Back'
		curr.execute(""" INSERT INTO ex02_movies (title, episode_nb, opening_craw, director, producer, release_date) 
							VALUES
						('The Empire Strikes Back',5, '', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17')
					""")
		conn.commit()
		insertion_return = insertion_return + "ok <br>"

		svg_title = 'Return of the Jedi'
		curr.execute(""" INSERT INTO ex02_movies (title, episode_nb, opening_craw, director, producer, release_date) 
							VALUES
						('Return of the Jedi',6, '', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25')
					""")
		conn.commit()
		insertion_return = insertion_return + "ok <br>"

		svg_title = 'The Force Awakens'
		curr.execute(""" INSERT INTO ex02_movies (title, episode_nb, opening_craw, director, producer, release_date) 
							VALUES
						('The Force Awakens',7, '', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', ' 2015-12-11')
					""")
		conn.commit()
		insertion_return = insertion_return + "ok <br>"

		# je ferme la collection
		conn.close()

	except Exception as e:
		return HttpResponse("Le titre non insere est {}<br>erreur{}".format(svg_title,e))	
		
	return HttpResponse(insertion_return)


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


# 127.0.0.1:8000/ex03/display
def remove(request):
	pass
