from apscheduler.schedulers.background import BackgroundScheduler
from disaster_app.views import DisasterViewset


def start():
    scheduler = BackgroundScheduler()
    disaster = DisasterViewset()

    scheduler.add_job(disaster.save_disaster_data, "interval", seconds=240, id="fetcher 01", replace_existing=True)
    scheduler.start()
