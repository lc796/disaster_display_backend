import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from disaster_app.views import DisasterViewset


def start():
    HOURS_BETWEEN_JOBS = 24

    scheduler = BackgroundScheduler()
    disaster = DisasterViewset()

    # Schedule tasks to run with an interval, and to start the first job after 3 seconds
    scheduler.add_job(disaster.save_disaster_data, "interval", hours=HOURS_BETWEEN_JOBS,
                      next_run_time=(datetime.datetime.now() + datetime.timedelta(seconds=3)),
                      id="fetcher 01", replace_existing=True)
    scheduler.start()
