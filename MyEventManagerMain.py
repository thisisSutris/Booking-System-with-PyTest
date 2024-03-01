from re import search
from tkinter import *
from SmallMessages import *
from MyEventManager import *
from SearchedEvent import *

global api
api = get_calendar_api()

def my_event_manager():
    # Date variables
    days_list = [None] + list(range(1,32))
    months_list = [None, "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    years_list = list(range(2017, 2027))

    # Main page displays
    y_ = 110
    main = Tk()
    main.title("My Event Manager")
    main.geometry("640x350")
    title = Label(main, text="My Event Manager",font=("times", 45, "bold"))
    title.place(relx=0.5, rely=0.15, anchor=CENTER)
    text = Label(main, text=" Day         Month       Year",font=("times", 15,))
    text.place(x=150, y=y_)
    y_ += 30

    # Days dropdown box
    days_variable = StringVar(main)
    days_variable.set(days_list[0])
    days = OptionMenu(main, days_variable, *days_list)
    days.place(x=150, y=y_)

    # Months dropdown box
    months_variable = StringVar(main)
    months_variable.set(months_list[0])
    months = OptionMenu(main, months_variable, *months_list)
    months.place(x=230, y=y_)

    # Years dropdown box
    years_variable = StringVar(main)
    years_variable.set(2022)
    years = OptionMenu(main, years_variable, *years_list)
    years.place(x=310, y=y_)

    # Select date button
    select_date_button = Button(main, text = 'Select Date', command = lambda: date_check(days_variable.get(), months_variable.get(), years_variable.get()))
    select_date_button.place(x=400, y=y_)
    y_ += 40

    # Search for event
    search_event_label = Label(main, text="Event Search:",font=("times", 12))
    search_event_label.place(x=150, y=y_)
    search_event = Entry(main)
    search_event.place(x=260, y=y_)

    # Search for event button
    search_event_button = Button(main, text = 'Search', command = lambda: search_event_check(search_event.get()))
    search_event_button.place(x=400, y=y_)
    y_ += 40

    # Create new event button
    new_event_button = Button(main, text = 'Create New Event', command = event_popup)
    new_event_button.place(x=250, y=y_)
    y_ += 40

     # Search for event
    filename_label = Label(main, text="File Name:",font=("times", 12))
    filename_label.place(x=150, y=y_)
    filename = Entry(main)
    filename.place(x=230, y=y_)

    # Import events button
    import_events = Button(main, text = 'Import Event', command = lambda: [import_event(filename.get())])
    import_events.place(x=370, y=y_-4)

    # Export events button
    export_events = Button(main, text = 'Export Events', command = lambda: [export_event(filename.get())])
    export_events.place(x=460, y=y_-4)


    # Display main page
    main.mainloop()

def date_check(day, month, year):
    # day and month is given as string
    if day == "None":
        day = None
    else:
        day = int(day)
    if month == "None":
        month = None
    else:
        months = [None, "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month = months.index(month)
    
    # Seperate months depending on how many days they have
    months28 = [2]
    months30 = [4, 6, 9, 11]
    # If days is filled, months will also have to be filled
    # There will only be problems on months with 30 or 28 days (31 is max and will work with all 31 day months)
    if (month == None and day != None) or (month in months28 and int(day) > 28) or (month in months30 and int(day) > 30):
        input_error("date")
    else:
        # Get required events and make new window
        events = get_events(api)
        events = get_events_date(events, int(year), month, day)
        search_field = ""
        if day != None:
            search_field = search_field + str(day) + " "
        if month != None:
            search_field = search_field + months[month] + " "
        search_field = search_field + str(year) + " "
        display_searched_events(events, search_field)

def search_event_check(search_field):
    events = get_events(api)
    events = search_phrase(events, search_field)
    search_field = search_field + " "
    display_searched_events(events, search_field)

def export_event(filename):
    try:
        export_events(get_events(api), filename)
    except:
        input_error("file name")
        return
    success_page()
    

def import_event(filename):
    try:
        import_events(filename)
    except:
        input_error("file name")
        return
    success_page()

if __name__=='__main__':
    my_event_manager()