import time

from win11toast import toast, notify, update_progress

def start():
    
    res = toast("Start 30min Timer?", buttons=['Yes',"No"], audio={"silent": "true"})
    res_str = res["arguments"].replace("http:","")

    if res_str=="Yes":
        time.sleep(2)       #Technically not needed, seems to me to give it a smoother transition
        timer()
    else:
        print("Stopped")


def timer():

    mins = 30


    notify(title="Warming up", body=None,progress={
    'title': 'Booting up Human',
    'status': 'Booting....',
    'value': '0',
    'valueStringOverride': f'{mins} Mins left'
    }, audio={"silent": "true"})

    for i in range(30, 0, -1):
        time.sleep(60)
        update_progress({'value': i/mins, 'valueStringOverride': f'{i} Mins left'})

    update_progress({'status': 'Completed!'})

    alarm()
    

def alarm():
    toast("Booted Up", audio="ms-winsoundevent:Notification.Looping.Default")


if __name__ == '__main__':
    start()