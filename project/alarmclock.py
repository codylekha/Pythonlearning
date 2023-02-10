from datetime import datetime
#from playsound import playsound
alarm_time = input("Enter the time of alarm HH:MM:SS \n")

alarm_hour =  alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper() #AM PM

now = datetime.now()

current_hour = now.strftime("%I")
current_min = now.strftime("%M")
current_sec = now.strftime("%S")
current_period = now.strftime("%p")

while True:
    if(alarm_period==current_period):
        if (alarm_hour == current_hour):
            if(alarm_min==current_min):
                if(alarm_sec==current_sec):
                
                    print("Wakeup!!!!!!!!!!")
                    break
                    
'''
0   1    2    3    4    5     6     7    8    9 10      s11
h   h    :    m     m    :     s    s     :  A  M    backslash n    '''
