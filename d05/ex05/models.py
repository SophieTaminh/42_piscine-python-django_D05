from django.db import models

# Creation du modele Movies, c'est a dire de la table Movies
class Movies(models.Model):
	title = models.CharField(max_length=64,null=False)
	episode_nb = models.IntegerField(primary_key=True)
	opening_crawl = models.TextField()
	director = models.CharField(max_length=32,null=False)
	producer = models.CharField(max_length=128,null=False)
	release_date = models.DateField(null=False)

# Ce modèle doit également redéfinir la methode __str__ 
# afin que celle-ci renvoie l’attribut title
	def __str__(self):
		return(self.title)