from apscheduler.schedulers.background import BackgroundScheduler

from jobs.jobs import send_messages


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_messages, 'interval', seconds=10)
    scheduler.start()