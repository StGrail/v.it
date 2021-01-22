from django.db import models


class TrainingSamplesForRecommendation(models.Model):
    user_id = models.IntegerField()
    vacancy_id = models.IntegerField()
    user_rating = models.IntegerField()
