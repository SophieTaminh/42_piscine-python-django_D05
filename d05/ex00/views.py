from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import psycopg2


def init(request):
		
	try:
		conn = psycopg2.connect(
			database = 'formationdjango',
			host = 'localhost',
			user = 'djangouser',
			password = 'secret'
			)

		curr = conn.cursor()

		curr.execute(""" CREATE TABLE IF NOT EXISTS ex00_movies (
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
		
		