import xlwings as xw
import pyautogui
from appJar import gui
from win32com.client import Dispatch
import re
import xlrd
import clipboard
from datetime import timedelta
from datetime import datetime
from dateutil import  parser

wb = xw.Book('EricssonBSS V7.7.xlsm')
wblte = xw.Book('LTE Outage Handler V2.5.xlsm')
sht = wb.sheets['Ericsson']
shtlte = wblte.sheets('LTE Outage')
workbook = xlrd.open_workbook("warid.xlsx")
worksheet = workbook.sheet_by_index(0)

#########################################

reason = []
down_time = []
BSC = []
Site_id = []
city = []
rbu = []
sites = []


##################################################

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
wsh = Dispatch("WScript.Shell")

#############################################################################

for x in range(1, 16480):
    rbu.append(worksheet.cell(x, 17).value)
    city.append(worksheet.cell(x, 5).value)
    sites.append(worksheet.cell(x, 0).value)

for y in range(0, 16479):
    temp = sites[y]
    sites[y] = temp[-6:]

############################################################################



def press2G(btn):
    count = 5
    check = True
    total_tts = int(app.getTextArea(title="Number of TTS"))
    if total_tts > 0:
        total_tts = int(app.getTextArea(title="Number of TTS"))
    else:
        total_tts = 1
    trout_start = True
    while (check == True and total_tts >=1):
        c = str(count)
        if (sht.range('P' + c).value == None):
            reason = sht.range('O' + c).value
            down_time = sht.range('Q' + c).value
            Site_id = sht.range('S' + c).value
            if isinstance(Site_id,float):
                Site_id = int(Site_id)
                Site_id = str(Site_id)
                Site_id = unicode(Site_id)

            start_time = parser.parse(down_time)
            esc_time = start_time + timedelta(minutes=5)
            start_time = datetime.strftime(start_time, '%d/%H:%M')
            esc_time = datetime.strftime(esc_time, '%d/%H:%M')
            start_time_hrs, start_time_min = start_time.split(':')
            start_time_day, start_time_hrs = start_time_hrs.split('/')
            esc_time_hrs, esc_time_min = esc_time.split(':')
            esc_time_day, esc_time_hrs = esc_time_hrs.split('/')

            for z in range(0, 16479):
                if Site_id == sites[z]:
                    city_name = city[z]
                else:
                    temp1 = 0

            if trout_start == True:
                ###################click on task_bar################################

                pyautogui.click(x=int(app.getTextArea(title='Task bar x')), y=int(app.getTextArea(title='Task bar y')),
                                button='left')

                trout_start = False


            ###################click on close###############################

            pyautogui.click(x=496, y=279, button='left')

            ###################click on find################################

            pyautogui.click(x=438, y=280, button='left')

            ###################click on open################################

            pyautogui.click(x=495, y=235, button='left')

            ###################click on BTS################################

            pyautogui.click(x=581, y=231, button='left')

            ###################click on BTS_okay################################

            pyautogui.click(x=754, y=536, button='left', interval=0.3)

            ###################click on medium################################

            pyautogui.click(x=650, y=279, button='left')

            ###################click on start_time day################################

            pyautogui.click(x=804, y=237, button='left')
            pyautogui.typewrite(message=start_time_day)

            ###################click on start_time hours################################

            pyautogui.click(x=898, y=238, button='left')
            pyautogui.typewrite(message=start_time_hrs)

            ###################click on start_time minutes################################

            pyautogui.click(x=916, y=237, button='left')
            pyautogui.typewrite(message=start_time_min)

            ###################click on esc_time day################################

            pyautogui.click(x=803, y=292, button='left')
            pyautogui.typewrite(message=esc_time_day)

            ###################click on esc_time hours################################

            pyautogui.click(x=899, y=292, button='left')
            pyautogui.typewrite(message=esc_time_hrs)

            ###################click on esc_time minutes################################

            pyautogui.click(x=915, y=293, button='left')
            pyautogui.typewrite(message=esc_time_min)

            ###################click on node################################

            pyautogui.click(x=693, y=347, button='left')
            wsh.Sendkeys("+{HOME}")
            pyautogui.press('delete')
            pyautogui.typewrite(message=Site_id)
            pyautogui.doubleClick(x=693, y=347, button='left')

            ###################click on city name################################

            pyautogui.click(x=467, y=347, button='left')
            wsh.Sendkeys("+{HOME}")
            pyautogui.press('delete')
            pyautogui.typewrite(message=city_name)

            ###################click on site is down################################

            pyautogui.click(x=769, y=472, button='left')
            wsh.Sendkeys("^+{HOME}")
            pyautogui.press('delete')
            z = Site_id + " is up now"
            pyautogui.typewrite(message=z)
            ###################click on alarms################################

            pyautogui.click(x=772, y=528, button='left')
            wsh.Sendkeys("^+{HOME}")
            pyautogui.press('delete')
            pyautogui.typewrite(message=reason)

            ###################click on escalation################################

            pyautogui.click(x=773, y=585, button='left')
            wsh.Sendkeys("^+{HOME}")
            pyautogui.press('delete')
            pyautogui.typewrite(message="Escalated to FME and NOSS")

            ###################click on RCA will be shared################################

            pyautogui.click(x=773, y=696, button='left')
            wsh.Sendkeys("^+{HOME}")
            pyautogui.press('delete')
            pyautogui.typewrite(message="RCA will be shared later by NOSS")

            ###################click on okay################################

            pyautogui.click(x=919, y=390, button='left')

            ###################click on close################################

            pyautogui.click(x=496, y=279, button='left')

            ###################click on TT################################

            pyautogui.click(x=467, y=251, button='left')
            wsh.Sendkeys("^+{HOME}")
            pyautogui.hotkey('ctrlleft', 'c')
            ################################################################
            sht.range('P' + c).value = clipboard.paste()

            total_tts = total_tts -1

        elif (sht.range('P' + c).value != None):
            count = count + 1
            check = True



###################################################

def press4G(btn):
    count = 5
    check = True
    total_tts = int(app.getTextArea(title="Number of TTS"))
    if total_tts > 0:
        total_tts = int(app.getTextArea(title="Number of TTS"))
    else:
        total_tts = 1
    trout_start = True
    while (check == True and total_tts >= 1):
        c = str(count)
        if (shtlte.range('T' + c).value == None):
            reason = shtlte.range('S' + c).value
            down_time = shtlte.range('V' + c).value
            Site_id = shtlte.range('W' + c).value
            if isinstance(Site_id, float):
                Site_id = int(Site_id)
                Site_id = str(Site_id)
                Site_id = unicode(Site_id)

            start_time = parser.parse(down_time)
            esc_time = start_time + timedelta(minutes=5)
            start_time = datetime.strftime(start_time, '%d/%H:%M')
            esc_time = datetime.strftime(esc_time, '%d/%H:%M')
            start_time_hrs, start_time_min = start_time.split(':')
            start_time_day, start_time_hrs = start_time_hrs.split('/')
            esc_time_hrs, esc_time_min = esc_time.split(':')
            esc_time_day, esc_time_hrs = esc_time_hrs.split('/')

            for z in range(0, 16479):
                if Site_id == sites[z]:
                    city_name = city[z]
                else:
                    temp1 = 0

            if trout_start == True:
                ###################click on task_bar################################

                pyautogui.click(x=int(app.getTextArea(title='Task bar x')), y=int(app.getTextArea(title='Task bar y')),
                                button='left')

                trout_start = False

            ###################click on close###############################

            pyautogui.click(x=496, y=279, button='left')

            ###################click on find################################

            pyautogui.click(x=438, y=280, button='left')

            ###################click on open################################

            pyautogui.click(x=495, y=235, button='left')

            ###################click on BTS################################

            pyautogui.click(x=581, y=231, button='left')

            ###################click on BTS_okay################################

            pyautogui.click(x=754, y=536, button='left', interval=0.3)

            ###################click on medium################################

            pyautogui.click(x=650, y=256, button='left')

            ###################click on start_time day################################

            pyautogui.click(x=804, y=237, button='left')
            pyautogui.typewrite(message=start_time_day)

            ###################click on start_time hours################################

            pyautogui.click(x=898, y=238, button='left')
            pyautogui.typewrite(message=start_time_hrs)

            ###################click on start_time minutes################################

            pyautogui.click(x=916, y=237, button='left')
            pyautogui.typewrite(message=start_time_min)

            ###################click on esc_time day################################

            pyautogui.click(x=803, y=292, button='left')
            pyautogui.typewrite(message=esc_time_day)

            ###################click on esc_time hours################################

            pyautogui.click(x=899, y=292, button='left')
            pyautogui.typewrite(message=esc_time_hrs)

            ###################click on esc_time minutes################################

            pyautogui.click(x=915, y=293, button='left')
            pyautogui.typewrite(message=esc_time_min)

            ###################click on node################################

            pyautogui.click(x=693, y=347, button='left')
            wsh.Sendkeys("+{HOME}")
            pyautogui.press('delete')
            pyautogui.typewrite(message=Site_id)
            pyautogui.doubleClick(x=693, y=347, button='left')

            ###################click on city name################################

            pyautogui.click(x=467, y=347, button='left')
            wsh.Sendkeys("+{HOME}")
            pyautogui.press('delete')
            pyautogui.typewrite(message=city_name)

            ###################click on site is down################################

            pyautogui.click(x=769, y=472, button='left')
            wsh.Sendkeys("^+{HOME}")
            pyautogui.press('delete')
            z = Site_id + " (4G/LTE) is up now"
            pyautogui.typewrite(message=z)
            ###################click on alarms################################

            pyautogui.click(x=772, y=528, button='left')
            wsh.Sendkeys("^+{HOME}")
            pyautogui.press('delete')
            pyautogui.typewrite(message=reason)

            ###################click on escalation################################

            pyautogui.click(x=773, y=585, button='left')
            wsh.Sendkeys("^+{HOME}")
            pyautogui.press('delete')
            pyautogui.typewrite(message="Escalated to FME and NOSS")

            ###################click on RCA will be shared################################

            pyautogui.click(x=773, y=696, button='left')
            wsh.Sendkeys("^+{HOME}")
            pyautogui.press('delete')
            pyautogui.typewrite(message="RCA will be shared later by NOSS")

            ###################click on okay################################

            pyautogui.click(x=919, y=390, button='left')

            ###################click on close################################

            pyautogui.click(x=496, y=279, button='left')

            ###################click on TT################################

            pyautogui.click(x=467, y=251, button='left')
            wsh.Sendkeys("^+{HOME}")
            pyautogui.hotkey('ctrlleft', 'c')
            ################################################################
            shtlte.range('T' + c).value = clipboard.paste()

            total_tts = total_tts - 1

        elif (shtlte.range('T' + c).value != None):
            count = count + 1
            check = True


###################################################



def press2GCP(btn):
    x = clipboard.paste()
    x = re.split(r'\t+', x)
    temp = x[3]
    temp = temp[:-2]
    x[3] = temp
    temp = temp[-6:]
    start_time = parser.parse(x[1])
    esc_time = start_time + timedelta(minutes=5)
    start_time = datetime.strftime(start_time, '%d/%H:%M')
    esc_time = datetime.strftime(esc_time, '%d/%H:%M')
    start_time_hrs, start_time_min = start_time.split(':')
    start_time_day, start_time_hrs = start_time_hrs.split('/')
    esc_time_hrs, esc_time_min = esc_time.split(':')
    esc_time_day, esc_time_hrs = esc_time_hrs.split('/')


    for z in range(0, 16479):
        if temp == sites[z]:
            x.append(city[z])
        else:
            temp1 = 0

    ###################click on task_bar################################

    pyautogui.click(x=int(app.getTextArea(title='Task bar x')), y=int(app.getTextArea(title='Task bar y')), button='left')


    ###################click on close###############################

    pyautogui.click(x=496,y=279,button='left')

    ###################click on find################################

    pyautogui.click(x=438, y=280, button='left')

    ###################click on open################################

    pyautogui.click(x=495, y=235, button='left')

    ###################click on BTS################################

    pyautogui.click(x=581, y=231, button='left')

    ###################click on BTS_okay################################

    pyautogui.click(x=754, y=536, button='left')

    ###################click on medium################################

    pyautogui.click(x=650, y=279, button='left')

    ###################click on start_time day################################

    pyautogui.click(x=804, y=237, button='left')
    pyautogui.typewrite(message=start_time_day)

    ###################click on start_time hours################################

    pyautogui.click(x=898, y=238, button='left')
    pyautogui.typewrite(message=start_time_hrs)

    ###################click on start_time minutes################################

    pyautogui.click(x=916, y=237, button='left')
    pyautogui.typewrite(message=start_time_min)

    ###################click on esc_time day################################

    pyautogui.click(x=803, y=292, button='left')
    pyautogui.typewrite(message=esc_time_day)

    ###################click on esc_time hours################################

    pyautogui.click(x=899, y=292, button='left')
    pyautogui.typewrite(message=esc_time_hrs)

    ###################click on esc_time minutes################################

    pyautogui.click(x=915, y=293, button='left')
    pyautogui.typewrite(message=esc_time_min)

    ###################click on node################################

    pyautogui.click(x=693, y=347, button='left')
    wsh.Sendkeys("+{HOME}")
    pyautogui.press('delete')
    pyautogui.typewrite(message=x[3])

    ###################click on city name################################

    pyautogui.click(x=467, y=347, button='left')
    wsh.Sendkeys("+{HOME}")
    pyautogui.press('delete')
    pyautogui.typewrite(message=x[4])

    ###################click on site is down################################

    pyautogui.click(x=769, y=472, button='left')
    wsh.Sendkeys("^+{HOME}")
    pyautogui.press('delete')
    z = x[3] + " is up now"
    pyautogui.typewrite(message = z)
    ###################click on alarms################################

    pyautogui.click(x=772, y=528, button='left')
    wsh.Sendkeys("^+{HOME}")
    pyautogui.press('delete')
    pyautogui.typewrite(message=x[0])

    ###################click on escalation################################

    pyautogui.click(x=773, y=585, button='left')
    wsh.Sendkeys("^+{HOME}")
    pyautogui.press('delete')
    pyautogui.typewrite(message= "Escalated to FME and NOSS")


    ###################click on RCA will be shared################################

    pyautogui.click(x=773, y=696, button='left')
    wsh.Sendkeys("^+{HOME}")
    pyautogui.press('delete')
    pyautogui.typewrite(message="RCA will be shared later by NOSS")

    ###################click on okay################################

    pyautogui.click(x=919, y=390, button='left')


    ###################click on close################################

    pyautogui.click(x=496, y=279, button='left')

    ###################click on TT################################

    pyautogui.click(x=467, y=251, button='left')
    wsh.Sendkeys("^+{HOME}")
    pyautogui.hotkey('ctrlleft', 'c')
    ################################################################

###################################################



def press4GCP(btn):
    x = clipboard.paste()
    x = re.split(r'\t+', x)
    temp = x[3]
    temp = temp[:-2]
    x[3] = temp
    temp = temp[-6:]
    start_time = parser.parse(x[2])
    esc_time = start_time + timedelta(minutes=5)
    start_time = datetime.strftime(start_time, '%d/%H:%M')
    esc_time = datetime.strftime(esc_time, '%d/%H:%M')
    start_time_hrs,start_time_min = start_time.split(':')
    start_time_day,start_time_hrs = start_time_hrs.split('/')
    esc_time_hrs, esc_time_min = esc_time.split(':')
    esc_time_day,esc_time_hrs = esc_time_hrs.split('/')


    for z in range(0, 16479):
        if temp == sites[z]:
            x.append(city[z])
        else:
            temp1 = 0

    ###################click on task_bar################################

    pyautogui.click(x=int(app.getTextArea(title='Task bar x')), y=int(app.getTextArea(title='Task bar y')), button='left')


    ###################click on close###############################

    pyautogui.click(x=496,y=279,button='left')

    ###################click on find################################

    pyautogui.click(x=438, y=280, button='left')

    ###################click on open################################

    pyautogui.click(x=495, y=235, button='left')

    ###################click on BTS################################

    pyautogui.click(x=581, y=231, button='left')

    ###################click on BTS_okay################################

    pyautogui.click(x=754, y=536, button='left')

    ###################click on high################################

    pyautogui.click(x=650, y=256, button='left')

    ###################click on start_time day################################

    pyautogui.click(x=804, y=237, button='left')
    pyautogui.typewrite(message=start_time_day)


    ###################click on start_time hours################################

    pyautogui.click(x=898, y=238, button='left')
    pyautogui.typewrite(message=start_time_hrs)

    ###################click on start_time minutes################################

    pyautogui.click(x=916, y=237, button='left')
    pyautogui.typewrite(message=start_time_min)

    ###################click on esc_time day################################

    pyautogui.click(x=803, y=292, button='left')
    pyautogui.typewrite(message=esc_time_day)

    ###################click on esc_time hours################################

    pyautogui.click(x=899, y=292, button='left')
    pyautogui.typewrite(message=esc_time_hrs)

    ###################click on esc_time minutes################################

    pyautogui.click(x=915, y=293, button='left')
    pyautogui.typewrite(message=esc_time_min)

    ###################click on node################################

    pyautogui.click(x=693, y=347, button='left')
    wsh.Sendkeys("+{HOME}")
    pyautogui.press('delete')
    pyautogui.typewrite(message=x[3])

    ###################click on city name################################

    pyautogui.click(x=467, y=347, button='left')
    wsh.Sendkeys("+{HOME}")
    pyautogui.press('delete')
    pyautogui.typewrite(message=x[4])

    ###################click on site is down################################

    pyautogui.click(x=769, y=472, button='left')
    wsh.Sendkeys("^+{HOME}")
    pyautogui.press('delete')
    z = x[3] + "  (4G/LTE) is up now"
    pyautogui.typewrite(message = z)
    ###################click on alarms################################

    pyautogui.click(x=772, y=528, button='left')
    wsh.Sendkeys("^+{HOME}")
    pyautogui.press('delete')
    pyautogui.typewrite(message=x[0])

    ###################click on escalation################################

    pyautogui.click(x=773, y=585, button='left')
    wsh.Sendkeys("^+{HOME}")
    pyautogui.press('delete')
    pyautogui.typewrite(message= "Escalated to FME and NOSS")


    ###################click on RCA will be shared################################

    pyautogui.click(x=773, y=696, button='left')
    wsh.Sendkeys("^+{HOME}")
    pyautogui.press('delete')
    pyautogui.typewrite(message="RCA will be shared later by NOSS")

    ###################click on okay################################

    pyautogui.click(x=919, y=390, button='left')


    ###################click on close################################

    pyautogui.click(x=496, y=279, button='left')

    ###################click on TT################################

    pyautogui.click(x=467, y=251, button='left')
    wsh.Sendkeys("^+{HOME}")
    pyautogui.hotkey('ctrlleft', 'c')
    ################################################################

def Impact(btn):
    x = clipboard.paste()
    x = str(x)
    x = x.replace("\r\n", ",").strip()
    x = "*"+ x
    clipboard.copy(x)

###################################################

###################################################
app = gui("AUTO-TT-Trout")
app.addButton("Create 2G TT", press2G,0,1)
app.setButtonWidhts("Create 2G TT",2)

app.addButton("Create 4G TT", press4G,3,1)
app.setButtonWidhts("Create 4G TT",2)

app.addButton("Create 2G TT CP", press2GCP,0,2)
app.setButtonWidhts("Create 2G TT CP",2)

app.addButton("Create 4G TT CP", press4GCP,3,2)
app.setButtonWidhts("Create 4G TT CP",2)

app.addButton("Impact of Sites", Impact,0,0)
app.setButtonWidhts("Impact of Sites",1)

app.enableEnter(press2G)

############################################
app.addLabel("l1", "Task bar x",1,0)
app.addTextArea("Task bar x",2,0)

############################################
app.addLabel("l2", "Task bar y",1,3)
app.addTextArea("Task bar y",2,3)

###########################################
app.addLabel("l3", "Number of TTS",5,0)
app.addTextArea("Number of TTS",5,1)


app.setAllTextAreaHeights(1)

app.go()