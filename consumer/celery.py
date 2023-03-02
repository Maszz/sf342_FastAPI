from celery import Celery,worker
from dotenv import dotenv_values
from nlp.thai_sentiment_analysis import ThaiSentimentAnalysis
from nlp.en_sentiment_analysis import EnSentimentAnalysis
from .utils import get_database
import os
# app.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
# app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")
celery = Celery('tasks',broker='redis://192.168.1.183:49153', backend='redis://192.168.1.183:49153',include=['consumer.tasks.task'])
# celery = Celery('tasks',broker='redis://localhost:10000', backend='redis://localhost:10000',include=['tasks.worker'])
celery.conf.update(task_track_started=True)
celery.conf.update(task_serializer='pickle')
celery.conf.update(result_serializer='pickle')
celery.conf.update(accept_content=['pickle', 'json'])
thai_sentiment_analysis = ThaiSentimentAnalysis()
en_sentiment_analysis = EnSentimentAnalysis()

db = get_database()


if __name__ == '__main__':


    # worker = worker.worker(app=app)

    # worker.run(loglevel='INFO',traceback=True,concurrency=1)


    celery.start()
    