from django.shortcuts import render
from django.http import HttpResponse

import psycopg2

# 127.0.0.1:8000/ex04/init
def init(request):

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
def populate(request):

	try:
		conn = psycopg2.connect(
			database = 'formationdjango',
			host = 'localhost',
			user = 'djangouser',
			password = 'secret'
			)
		#creation d un curseur pour inter agir avec sql
		curr = conn.cursor()

		svg_title = 'The Phantom Menaces'
		curr.execute(""" SELECT episode_nb from ex04_movies WHERE episode_nb = 1 """)
		if not curr.fetchone():
			curr.execute(""" INSERT INTO ex04_movies (title, episode_nb, opening_craw, director, producer, release_date) 
								VALUES
							('The Phantom Menace', 1, '', 'George Lucas', 'Rick McCallum', '1999-05-19')
						""")
			conn.commit()
			insertion_return = "ok <br>"
		else :
			insertion_return = "l'episode 1 existe deja<br>"


		svg_title = 'Attack of the Clones'
		curr.execute(""" SELECT episode_nb from ex04_movies WHERE episode_nb = 2 """)
		if not curr.fetchone():
			curr.execute(""" INSERT INTO ex04_movies (title, episode_nb, opening_craw, director, producer, release_date) 
								VALUES
							('Attack of the Clones', 2, '', 'George Lucas', 'Rick McCallum', '2005-05-16')
						""")
			conn.commit()
			insertion_return = insertion_return + "ok <br>"
		else :
			insertion_return = insertion_return +"l'episode 2 existe deja<br>"

		svg_title = 'Revenge of the Sith'
		curr.execute(""" SELECT episode_nb from ex04_movies WHERE episode_nb = 3 """)
		if not curr.fetchone():
			curr.execute(""" INSERT INTO ex04_movies (title, episode_nb, opening_craw, director, producer, release_date) 
								VALUES
							('Revenge of the Sith',3, '', 'George Lucas', 'Rick McCallum', '2005-05-19')
						""")
			conn.commit()
			insertion_return = insertion_return + "ok <br>"
		else :
			insertion_return = insertion_return +"l'episode 3 existe deja<br>"

		svg_title = 'A New Hope'
		curr.execute(""" SELECT episode_nb from ex04_movies WHERE episode_nb = 4 """)
		if not curr.fetchone():
			curr.execute(""" INSERT INTO ex04_movies (title, episode_nb, opening_craw, director, producer, release_date) 
								VALUES
							('A New Hope',4, '', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25')
						""")
			conn.commit()
			insertion_return = insertion_return + "ok <br>"
		else :
			insertion_return = insertion_return + "l'episode 4 existe deja<br>"

		svg_title = 'The Empire Strikes Back'
		curr.execute(""" SELECT episode_nb from ex04_movies WHERE episode_nb = 5 """)
		if not curr.fetchone():
			curr.execute(""" INSERT INTO ex04_movies (title, episode_nb, opening_craw, director, producer, release_date) 
								VALUES
							('The Empire Strikes Back',5, '', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17')
						""")
			conn.commit()
			insertion_return = insertion_return + "ok <br>"
		else :
			insertion_return = insertion_return + "l'episode 5 existe deja<br>"

		svg_title = 'Return of the Jedi'
		curr.execute(""" SELECT episode_nb from ex04_movies WHERE episode_nb = 6 """)
		if not curr.fetchone():
			curr.execute(""" INSERT INTO ex04_movies (title, episode_nb, opening_craw, director, producer, release_date) 
								VALUES
							('Return of the Jedi',6, '', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25')
						""")
			conn.commit()
			insertion_return = insertion_return + "ok <br>"
		else :
			insertion_return = insertion_return +"l'episode 6 existe deja<br>"

		svg_title = 'The Force Awakens'
		curr.execute(""" SELECT episode_nb from ex04_movies WHERE episode_nb = 7 """)
		if not curr.fetchone():
			curr.execute(""" INSERT INTO ex04_movies (title, episode_nb, opening_craw, director, producer, release_date) 
								VALUES
							('The Force Awakens',7, '', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', ' 2015-12-11')
						""")
			conn.commit()
			insertion_return = insertion_return + "ok <br>"
		else :
			insertion_return = insertion_return +"l'episode 7 existe deja<br>"

		# je ferme la collection
		conn.close()

	except Exception as e:
		return HttpResponse("Le titre non insere est {}<br>erreur{}".format(svg_title,e))	
		
	return HttpResponse(insertion_return)


# 127.0.0.1:8000/ex03/display
def display(request):

	try:
		# connection a la librairie
		conn = psycopg2.connect(
			database = 'formationdjango',
			host = 'localhost',
			user = 'djangouser',
			password = 'secret'
			)

		#creation d un curseur pour inter agir avec sql
		curr = conn.cursor()

		# executer des commamdes sql
		curr.execute(""" SELECT * FROM ex04_movies 
			""")
		response = curr.fetchall()
		
		# je ferme la collection
		conn.close()

	except Exception as e:
		return HttpResponse("{}".format(e))

	if response:
		select_return = "<table>"
		select_return = select_return + '<td>title</td><td> episode </td><td> opening_craw </td> </td><td> directed </td> <td> producer </td><td> released </td>'
		for row in response:
			each_row = '<td> {} </td><td> {} </td><td> {} </td> </td><td> {}</td> <td> {}</td> <td>{}</td>'.format(row[0], row[1], row[2], row[3], row[4], row[5])
			select_return = select_return + "<tr>" + each_row + "</tr>"
		select_return = select_return + "</table>"
	else: 
		select_return = "No data Available"

	return HttpResponse(select_return)


# 127.0.0.1:8000/ex03/display
def remove(request):
	pass
