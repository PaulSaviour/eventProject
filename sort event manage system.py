import pickle
import os
import pathlib
import json
########################### ORGANIZER ####################
class Event:
    # event_id = ''
    name = ''
    eventname = ''
    startdate = ''
    enddate = ''
    starttime = ''
    endtime = ''
    eventTotalcapacity = 10
    edetails = ''

    def __init__(self):
        self.Eevent={}
        self.event_id=len(self.Eevent)+1

    def createEvent(self):
        self.name = input("enter your name?")
        self.code = input("enter event code ?")
        self.eventname = input("what is your event name?")
        self.startdate = input("what is start date of your event ?")
        self.enddate = input("what is end date of your event ?")
        self.starttime = input("what is start time of your event ?")
        self.endtime = input("what is end time of your event ?")
        self.eventTotalcapacity = input("Enter Event Total capacity: ")
        


        self.edetails = self.Eevent
        self.details = {"Event name":self.eventname,"Event code":self.code,"organizer":self.name,"Start Date":self.startdate,"Start Time":self.starttime,
                       "End Date":self.enddate,"End Time":self.endtime,"Capacity":self.eventTotalcapacity}
        self.event_id=len(self.Eevent)+1
        self.Eevent[self.event_id] = self.details

        with open("event_data.json","w") as f:
            json.dump(self.Eevent,f)

        print("\n\n ------> Event Created!",self.Eevent)

    
    def update_details(self):
        e_id=int(input("Enter the event id you want to update : "))
        for i in self.Eevent[e_id]:
            self.Eevent[e_id][i]=input(f"enter the {i} you want to update : ")
        print("event details updated successfully \n ",self.Eevent)

    def delete_details(self):
        x = int(input("enter the event id which you want to delete : "))
        del self.Eevent[x] 
        print("remaining details available",self.Eevent)

    def detail_using_id(self):
        y = int(input("enter the event id which you want to view : "))
        print(self.Eevent[y])

    
class eventmember():
    name = ''
    email = ''
    event = ''
    reference = 200000
    
    
    def mail(self):
        self.email = input("What is your email address? ")
        while "@" not in self.email:
            self.email= input("Your email address must have '@' in it\nPlease write your email address again: ")
        if len(self.email) <= 6 :
            self.email = input("Your email address is too short\nPlease write your email address again: ")
        if "." not in self.email:
            self.email = input("Your email address must have '.' in it\nPlease write your email address again: ")
        while "." not in self.email:
            self.email = input("Your email address must have '.' in it\nPlease write your email address again: ")
        if len(self.email) <= 6 :
            self.email = input("Your email address is too short\nPlease write your email address again: ")
        if "@" not in self.email:
            self.email = input("Your email address must have '@' in it\nPlease write your email address again: ")
        else:
            print("Emil verified successfully")
        self.password = input("enter your new password : ")
    def update_pass(self):
        self.password = input("enter your new password : ")
        print("password updated successfully \n ",self.password)
    
    def register(self):
        self.name= input("Enter Customer Name: ")
        # self.email = input("Enter Customer Email: ")
        file = pathlib.Path("events.data")
        if file.exists():
            infile = open('events.data', 'rb')
            eventdetails = pickle.load(infile)

            self.reference = input("Enter Reference Code(10000 - 50000) : ")
            while True:
                if int(self.reference) <= 10000:
                    print("Warning: Please Enter Valid Reference Code")
                    self.reference = input("Enter Reference Code(10000 - 50000) : ")
                else:
                    break

        for event in eventdetails:
            print("Available Events : " + event.code + " Event Name : " + event.eventname)
        infile.close()
        self.event = input("Enter Event Code: ")


    def check(self):
        file = pathlib.Path("register.data")
        if file.exists():
            infile = open('register.data', 'rb')
            registerdetails = pickle.load(infile)
            for register in registerdetails:
                if register.email == self.email and register.event == self.event:
                    return True
            infile.close()


    def gettotalregister(self):
        file = pathlib.Path("events.data")
        if file.exists():
            infile = open('events.data', 'rb')
            eventdetails = pickle.load(infile)
            for event in eventdetails:
                if event.eventcode == self.event:
                    return int(event.eventTotalcapacity)
            infile.close
        else:
            return 0

    def registeredevents(self):
        file = pathlib.Path("tickets.data")
        counter= 0
        if file.exists():
            infile = open('tickets.data', 'rb')
            registerdetails = pickle.load(infile)
            for register in registerdetails:
                if register.event == self.event:
                    counter = counter + 1
            return int(counter)
        return 0





########organizer#####

def createEvent():
    event = Event()
    event.createEvent()
    event.createEvent()
    event.createEvent()
    event.createEvent()

    event.update_details()

    event.delete_details()

    event.detail_using_id()

    saveEventDetails(event)


# Save Event Details to File

def saveEventDetails(event):
    file = pathlib.Path("events.data")
    if file.exists():
        infile = open('events.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(event)
        infile.close()
        os.remove('events.data')
    else:
        oldlist = [event]
    outfile = open('tempevents.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('tempevents.data', 'events.data')

def getEventslists():
    file = pathlib.Path("events.data")
    if file.exists ():
        infile = open('events.data','rb')
        eventdetails = pickle.load(infile)
        print("---------------EVENT LISTS---------------------")
        for event in eventdetails :
            print({"Name":event.name,"Event Name":event.eventname,"Start Date": event.startdate, "End Date":event.enddate,
            "Start Time": event.starttime, "End Time":event.endtime,"Capacity":event.eventTotalcapacity})
            
        infile.close()
        print("--------------------------------------------------")
        input('Press Enter To Main Menu')
    else :
        print("NO EVENTS RECORDS FOUND")

def getEventsdetails():
    file = pathlib.Path("events.data")
    if file.exists ():
        infile = open('events.data','rb')
        eventdetails = pickle.load(infile)
        print("---------------EVENT DETAILS---------------------")

        for event in eventdetails :
            print(event.edetails)
            
        infile.close()
        print("--------------------------------------------------")
        input('Press Enter To Main Menu')
    else :
        print("NO EVENTS RECORDS FOUND")

########################### MEMBER ####################

def mail():
    events=eventmember()
    events.mail()
    events.update_pass()

def registerevent():
    regist = eventmember()
    regist.register()
    if regist.check():
        print("Warning : You Already Book A Seat")

    elif regist.registeredevents() >= regist.gettotalregister():
        print("Warning : All Ticket Sold Out")

    else:
        print("Sucess : event Booked!")
        saveregisterDetiails(regist)

# Save Ticket Detials to File

def saveregisterDetiails(regist):
    file = pathlib.Path("register.data")
    if file.exists():
        infile = open('register.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(regist)
        infile.close()
        os.remove('register.data')
    else:
        oldlist = [regist]
    outfile = open('tempregister.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('tempregister.data', 'register.data')


# Display Saved Ticket Details

def getregisterDetails():
    file = pathlib.Path("register.data")
    if file.exists ():
        infile = open('register.data','rb')
        registerdetails = pickle.load(infile)
        print("---------------REGISTERED DETAILS---------------------")
        print("T-Ref    C-Name    C-Email    E-Code")
        for regist in registerdetails :
            print(regist.reference,"\t",regist.name,"\t", regist.email, "\t",regist.event)
        infile.close()
        print("--------------------------------------------------")
        input('Press Enter To Main Menu')
    else :
        print("NO event RECORDS FOUND")

    

###################################################### Start Program



ch=''
num=0
while ch != 8:
    print("\t\t---REGISTRATION---")
    print("\tEnter 1 to register as ORGANIZER")
    print("\tEnter 2 to register as MEMBER")
    ch = input()
    if ch == '1':
        print("\t\t\t\t---------------------")
        print("\t\t\t\tREGISTER AS ORGANIZER")
        print("\t\t\t\t---------------------")
        email = input("enter email")
        password = input("enter password")
        print("\t\t\t\t------------------")
        print("\t\t\t\tLOGIN AS ORGANIZER")
        print("\t\t\t\t------------------")
        print("\tMAIN MENU")
        print("\t1. CREATE EVENTS , UPDATE , DELETE , VIEW WITH ID")
        print("\t2. VIEW EVENTS LIST")
        print("\t3. VIEW EVENTS DETAILS")
        print("\t4. LOGOUT")
        print("\tSelect Your Option (1-4) ")



        chi = input()
        if chi == '1':
            createEvent()
        elif chi == '2':
            getEventslists()
        elif chi == '3':
            getEventsdetails()
        elif chi == '4':
            print("ORGANIZER has Logging out")
    elif ch == '2':
        print("\t\t\t\t------------------")
        print("\t\t\t\tREGISTER AS MEMBER")
        print("\t\t\t\t------------------")
        mail()
        print("\t\t\t\t---------------")
        print("\t\t\t\tLOGIN AS MEMBER")
        print("\t\t\t\t---------------")
        print("\tMAIN MENU")
        print("\t1. REGISTER FOR EVENTS")
        print("\t2. VIEW REGISTERED EVENTS")
        print("\t3. LOGOUT")
        print("\tSelect Your Option (1-4) ")



        gh = input()
        if gh == '1':
            registerevent()
        elif gh == '2':
            getregisterDetails()
        elif chi == '3':
            print("MEMBER has Logging out")