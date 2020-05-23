from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler
from main import send_marks

account_sid = '*******************************'
auth_token = '********************************'
client = Client(account_sid, auth_token)

def job_function():
    send_marks()


sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(job_function, 'interval', hours=10)

sched.start()