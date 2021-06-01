import datetime

def getTimeRemaining():
    current_time = datetime.datetime.now()
    
    # August 20, Rachel's vest date
    # TODO: Make extensible
    end_time = datetime.datetime(year = 2021, month=8, day=20)
    time_remaining = (end_time - current_time)

    days_remaining = time_remaining.days
    return days_remaining
