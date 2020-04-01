from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import atexit
import time
from database.fetch import getUser

import pandas as pd

def print_time():
  field,data = getUser()
  df = pd.DataFrame(data,columns= field )
  print(df)
  df.to_csv('new.csv')
  return 0

# create schedule for printing time

def cron_job():
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(
        func=print_time,
        trigger=IntervalTrigger(seconds=15),
        id='printing_time_job',
        name='Print time every 2 seconds',
        replace_existing=True)
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())