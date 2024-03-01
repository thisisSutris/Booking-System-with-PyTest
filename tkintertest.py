from tkinter import *
from tkinter import ttk
from MyEventManager import *
from Time import *
from Reminder import *

""" ---------------------------------------- Main Page ---------------------------------------- """
def my_event_manager():
    # Date variables
    days_list = [" "] + list(range(1,32))
    months_list = [" ", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    years_list = list(range(2017, 2027))

    # Main page displays
    main = Tk()
    main.title("My Event Manager")
    main.geometry("640x350")
    title = Label(main, text="My Event Manager",font=("times", 45, "bold"))
    title.place(relx=0.5, rely=0.15, anchor=CENTER)
    text = Label(main, text=" Day         Month       Year",font=("times", 15,))
    text.place(x=150, y=110)

    # Days dropdown box
    days_variable = StringVar(main)
    days_variable.set(days_list[0])
    days = OptionMenu(main, days_variable, *days_list)
    days.place(x=150, y=140)

    # Months dropdown box
    months_variable = StringVar(main)
    months_variable.set(months_list[0])
    months = OptionMenu(main, months_variable, *months_list)
    months.place(x=230, y=140)

    # Years dropdown box
    years_variable = StringVar(main)
    years_variable.set(years_list[0])
    years = OptionMenu(main, years_variable, *years_list)
    years.place(x=310, y=140)

    # Select date button
    select_date = Button(main, text = 'Select Date', command = lambda: date_check(days_variable.get(), months_variable.get(), years_variable.get()))
    select_date.place(x=400, y=142)

    # Create new event button
    new_event_button = Button(main, text = 'Create New Event', command = new_event)
    new_event_button.place(x=250, y=200)

    # Export events button
    export_events = Button(main, text = 'Export Events', command = export_event)
    export_events.place(x=210, y=260)

    # Import events button
    import_events = Button(main, text = 'Import Event', command = import_event)
    import_events.place(x=310, y=260)

    # Display main page
    main.mainloop()

""" ---------------------------------------- View Events on a Certain Day Page ---------------------------------------- """
def date_check(day, month, year):
    # Seperate months depending on how many days they have
    months28 = ["Feb"]
    months30 = ["Apr", "Jun", "Sep", "Nov"]
    # If days is filled, months will also have to be filled
    # There will only be problems on months with 30 or 28 days (31 is max and will work with all 31 day months)
    if (month == " " and day != " ") or (month in months28 and int(day) > 28) or (month in months30 and int(day) > 30):
        date_error()
    else:
        date_events(day, month, year)

def date_error():
    # Date error displays
    date_error = Tk()
    date_error.title("Date error")
    title = Label(date_error, text="Date error, please select a valid date",font=("times", 16))
    title.pack()

    return_button = Button(date_error, text = 'OK', command = date_error.destroy)
    return_button.pack()

    # Display date error page
    date_error.mainloop()

def date_events(day, month, year):
    def view_event():
        selected_item = events_table.selection()
        selected_event = events[int(selected_item[0][1:4], base=16)-1]
        view_event_popup(selected_event)

    # Date event displays
    date_events = Tk()
    title_text = day + " " + month + " " + year + " Events"
    date_events.title(title_text)
    date_events.geometry("640x400")
    title = Label(date_events, text=title_text,font=("times", 30, "bold"))
    title.place(relx=0.5, rely=0.15, anchor=CENTER)

    # Events Table
    events_table = ttk.Treeview(date_events, columns = (1), show="headings", height=10)
    events_table.place(x=70, y=100)
    events_table.heading(1, text = "Events")
    events_table.column(1, width = 500)

    # Attendee table buttons
    view_event_button = Button(date_events, text = 'View', command = view_event)
    view_event_button.place(x=310, y=330)

    # Put events from API into table
    months = [" ", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month = months.index(month)
    if month == 0:
        month = None
    if day == " ":
        day = None
    else: 
        day = int(day)
    events = get_events_date(get_calendar_api(), int(year), month, day)
    for event in events:
        events_table.insert(parent='',index='end', values=event.get_summary())

    # Display date event page
    date_events.mainloop()

def view_event_popup(event):
    # Retrieve variables from event
    date_imported = event.get_starting_time()
    event_date_imported = str(date_imported.get_year()) + "-" + str(date_imported.get_month()) + "-" + str(date_imported.get_day())

    attendees = []
    if event.get_attendees():
        attendees = event.get_attendees()

    reminders = []
    if event.get_reminders():
        reminders = event.get_reminders()

    name_imported = event.get_summary()
    
    location_imported = event.get_location()
    online_link = ""
    if location_imported.get_link():
        online_link = location_imported.get_link()

    address_imported = ""
    if location_imported.get_street_number() or location_imported.get_street_name():
        address_imported = str(location_imported.get_street_number()) + " " + str(location_imported.get_street_name())

    suburb_imported = ""
    if location_imported.get_suburb():
        suburb_imported = location_imported.get_suburb()

    state_imported = ""
    if location_imported.get_state():
        state_imported = location_imported.get_state() 

    postcode_imported = ""
    if location_imported.get_postcode():
        postcode_imported = location_imported.get_postcode()

    country_imported = ""
    if location_imported.get_country():
        country_imported = location_imported.get_country()

    def add_attendee_popup():
        if len(attendees)>20:
            # Too many attendees error
            attendee_error = Tk()
            attendee_error.title("Too many attendees")
            title = Label(attendee_error, text="Maximum of 20 attendees",font=("times", 16))
            title.pack()

            return_button = Button(attendee_error, text = 'OK', command = attendee_error.destroy)
            return_button.pack()

            # Display date error page
            attendee_error.mainloop()
        else:
            # Display attendee popup page
            add_attendee_popup = Tk()
            add_attendee_popup.title("Add Attendee")
            add_attendee_popup.geometry("320x100")

            attendee_email_label = Label(add_attendee_popup, text="Attendee Email:",font=("times", 12))
            attendee_email_label.place(x=30, y=30)
            attendee_email = Entry(add_attendee_popup)
            attendee_email.place(x=140, y=30)

            cancel_button = Button(add_attendee_popup, text = 'Cancel', command = add_attendee_popup.destroy)
            cancel_button.place(x=160, y=60)

            add_button = Button(add_attendee_popup, text = 'Add', command = lambda: [add_attendee(attendee_email.get()), add_attendee_popup.destroy()])
            add_button.place(x=220, y=60)

            add_attendee_popup.mainloop()

    def add_attendee(attendee_email):
        # Add attendee to array and table
        attendee = Attendee(attendee_email)
        attendees.append(attendee)
        attendees_table.insert(parent='',index='end', values=attendee.get_email())

    def edit_attendee_popup():
        # Get the selected attendee
        selected_item = int(attendees_table.selection()[0][1:4], base=16)-1
        edit_attendee_popup = Tk()
        edit_attendee_popup.title("Add Attendee")
        edit_attendee_popup.geometry("320x100")

        attendee_email_label = Label(edit_attendee_popup, text="Attendee Email:",font=("times", 12))
        attendee_email_label.place(x=30, y=30)
        attendee_email = Entry(edit_attendee_popup)
        attendee_email.insert(0,attendees[selected_item].get_email())
        attendee_email.place(x=140, y=30)

        cancel_button = Button(edit_attendee_popup, text = 'Cancel', command = edit_attendee_popup.destroy)
        cancel_button.place(x=160, y=60)

        edit_button = Button(edit_attendee_popup, text = 'Update', command = lambda: [edit_attendee(attendee_email.get(), selected_item), edit_attendee_popup.destroy()])
        edit_button.place(x=220, y=60)

        edit_attendee_popup.mainloop()

    def edit_attendee(attendee_email, index):
        # Update the array and table
        attendees[index].set_email(attendee_email)
        selected_item = attendees_table.selection()
        attendees_table.item(selected_item, values=attendees[index].get_email())


    def delete_attendee():
        # Remove selected attendee from table and array
        selected_item = attendees_table.selection()
        attendees_table.delete(selected_item)
        del attendees[int(selected_item[0][1:4], base=16)-1]
    
    # Reminders
    def add_reminder_popup():
        # Display reminder popup page
        add_reminder_popup = Tk()
        add_reminder_popup.title("Add Reminder")
        add_reminder_popup.geometry("320x130")

        reminder_time_label = Label(add_reminder_popup, text="Reminder Time:",font=("times", 12))
        reminder_time_label.place(x=30, y=30)
        reminder_time = Entry(add_reminder_popup)
        reminder_time.place(x=140, y=30)

        reminder_method_label = Label(add_reminder_popup, text="Reminder Method:",font=("times", 12))
        reminder_method_label.place(x=30, y=50)
        reminder_methods = ["email", "popup"]
        method_variable = StringVar(add_reminder_popup)
        method_variable.set(reminder_methods[0])
        method = OptionMenu(add_reminder_popup, method_variable, *reminder_methods)
        method.place(x=170, y=50)

        cancel_button = Button(add_reminder_popup, text = 'Cancel', command = add_reminder_popup.destroy)
        cancel_button.place(x=160, y=100)

        add_button = Button(add_reminder_popup, text = 'Add', command = lambda: [add_reminder(reminder_time.get(), method_variable.get()), add_reminder_popup.destroy()])
        add_button.place(x=220, y=100)

        add_reminder_popup.mainloop()

    def add_reminder(reminder_time, reminder_method):
        # Add reminder to array and table
        reminder_time = int(reminder_time)
        try:
            reminder_time = int(reminder_time)
        except:
            time_error = Tk()
            time_error.title("Time error")
            title = Label(date_error, text="Time error",font=("times", 16))
            title.pack()
            return_button = Button(time_error, text = 'OK', command = time_error.destroy)
            return_button.pack()
            time_error.mainloop()
            return
        reminder = Reminder(reminder_method, int(reminder_time))
        reminders.append(reminder)
        reminders_table.insert(parent='',index='end', values=[reminder_time, reminder_method])

    def edit_reminder_popup():
        # Get the selected reminder
        selected_item = int(reminders_table.selection()[0][1:4], base=16)-1
        edit_reminder_popup = Tk()
        edit_reminder_popup.title("Add Reminder")
        edit_reminder_popup.geometry("320x130")

        reminder_time_label = Label(edit_reminder_popup, text="Reminder Time:",font=("times", 12))
        reminder_time_label.place(x=30, y=30)
        reminder_time = Entry(edit_reminder_popup)
        reminder_time.insert(0,reminders[selected_item].get_minutes())
        reminder_time.place(x=140, y=30)

        reminder_method_label = Label(edit_reminder_popup, text="Reminder Method:",font=("times", 12))
        reminder_method_label.place(x=30, y=50)
        reminder_methods = ["email", "popup"]
        method_variable = StringVar(edit_reminder_popup)
        method_variable.set(reminder_methods[0])
        method = OptionMenu(edit_reminder_popup, method_variable, *reminder_methods)
        method.place(x=170, y=50)

        cancel_button = Button(edit_reminder_popup, text = 'Cancel', command = edit_reminder_popup.destroy)
        cancel_button.place(x=160, y=100)

        add_button = Button(edit_reminder_popup, text = 'Update', command = lambda: [edit_reminder(reminder_time.get(), method_variable.get(), selected_item), edit_reminder_popup.destroy()])
        add_button.place(x=220, y=100)

        edit_reminder_popup.mainloop()

    def edit_reminder(reminder_time, reminder_method, index):
        # Update the array and table
        updated_reminder = Reminder(reminder_method, int(reminder_time))
        reminders[index] = updated_reminder
        selected_item = reminders_table.selection()
        reminders_table.item(selected_item, values=[reminder_time, reminder_method])


    def delete_reminder():
        # Remove selected reminder from table and array
        selected_item = reminders_table.selection()
        reminders_table.delete(selected_item)
        del reminders[int(selected_item[0][1:4], base=16)-1]


    # New event displays
    view_event = Tk()
    view_event.title("View Event")
    view_event.geometry("640x420")
    title = Label(view_event, text="View Event",font=("times", 30, "bold"))
    title.place(relx=0.5, rely=0.12, anchor=CENTER)

    # Required entry boxes
    _y = 90
    event_name_label = Label(view_event, text="Event Name:",font=("times", 12))
    event_name_label.place(x=30, y=_y)
    event_name = Entry(view_event)
    event_name.insert(0,name_imported)
    event_name.place(x=140, y=_y)
    _y += 40

    event_date_label = Label(view_event, text="Event Date:",font=("times", 12))
    event_date_label.place(x=30, y=_y)
    event_location_online_label = Label(view_event, text="Use formats yyyy-mm-dd or dd-MON-yy",font=("times", 10))
    event_location_online_label.place(x=30, y=_y + 20)
    event_date = Entry(view_event)
    event_date.insert(0,event_date_imported)
    event_date.place(x=140, y=_y)
    _y += 50

    event_online_label = Label(view_event, text="Online Link:",font=("times", 12))
    event_online_label.place(x=30, y=_y)
    event_location_online_label = Label(view_event, text="If event is online, don't fill the fields below",font=("times", 10))
    event_location_online_label.place(x=30, y=_y + 20)
    event_online = Entry(view_event)
    event_online.insert(0, online_link)
    event_online.place(x=140, y=_y)
    _y += 40

    event_address_label = Label(view_event, text="Address:",font=("times", 12))
    event_address_label.place(x=30, y=_y)
    event_address = Entry(view_event)
    event_address.insert(0, address_imported)
    event_address.place(x=140, y=_y)
    _y += 40

    event_suburb_label = Label(view_event, text="Suburb:",font=("times", 12))
    event_suburb_label.place(x=30, y=_y)
    event_suburb = Entry(view_event)
    event_suburb.insert(0, suburb_imported)
    event_suburb.place(x=140, y=_y)
    _y += 40

    event_postcode_label = Label(view_event, text="Postcode:",font=("times", 12))
    event_postcode_label.place(x=30, y=_y)
    event_postcode = Entry(view_event)
    event_postcode.insert(0, postcode_imported)
    event_postcode.place(x=140, y=_y)
    _y += 40

    event_state_label = Label(view_event, text="State:",font=("times", 12))
    event_state_label.place(x=30, y=_y)
    event_state = Entry(view_event)
    event_state.insert(0, state_imported)
    event_state.place(x=140, y=_y)
    _y += 40

    event_country_label = Label(view_event, text="Country:",font=("times", 12))
    event_country_label.place(x=30, y=_y)
    event_country = Entry(view_event)
    event_country.insert(0, country_imported)
    event_country.place(x=140, y=_y)
    
    # Attendees Table
    attendees_table = ttk.Treeview(view_event, columns = (1), show="headings", height=4)
    attendees_table.place(x=370, y=90)
    attendees_table.heading(1, text = "Attendees")
    attendees_table.column(1, width = 200)

    # Put attendees from API into table
    if attendees:
        for attendee in attendees:
            attendees_table.insert(parent='',index='end', values=attendee.get_email())
    
    # Attendee table buttons
    add_attendee_popup_button = Button(view_event, text = 'Add', command = add_attendee_popup)
    add_attendee_popup_button.place(x=540, y=200)
    
    edit_attendee_popup_button = Button(view_event, text = 'Edit', command = edit_attendee_popup)
    edit_attendee_popup_button.place(x=500, y=200)

    delete_attendee_button = Button(view_event, text = 'Delete', command = delete_attendee)
    delete_attendee_button.place(x=450, y=200)

    # Reminders Table
    reminders_table = ttk.Treeview(view_event, columns = (1,2), show="headings", height=4)
    reminders_table.place(x=370, y=230)
    reminders_table.heading(1, text = "Reminder Time")
    reminders_table.column(1, width = 100)
    reminders_table.heading(2, text = "Method")
    reminders_table.column(2, width = 100)

    # Put reminders from API into table
    if reminders:
        for reminder in reminders:
            reminders_table.insert(parent='',index='end', values=[reminder.get_minutes(),reminder.get_method()])
    """"""
    # Reminders table buttons
    add_reminder_popup_button = Button(view_event, text = 'Add', command = add_reminder_popup)
    add_reminder_popup_button.place(x=540, y=340)
    
    edit_reminder_popup_button = Button(view_event, text = 'Edit', command = edit_reminder_popup)
    edit_reminder_popup_button.place(x=500, y=340)

    delete_reminder_button = Button(view_event, text = 'Delete', command = delete_reminder)
    delete_reminder_button.place(x=450, y=340)

    cancel_event_button = Button(view_event, text = 'Cancel Event', command = view_event.destroy)
    cancel_event_button.place(x=400, y=370)
    cancel_event_button = Button(view_event, text = 'Cancel Event', command = view_event.destroy)
    cancel_event_button.place(x=400, y=370)

    save_event_button = Button(view_event, text = 'Save Event', command = lambda: [event_update(view_event, event_date.get(), attendees, event_name.get(), event_online.get(), event_address.get(), event_suburb.get(), event_postcode.get(), event_state.get(), event_country.get(), event, reminders)])
    save_event_button.place(x=510, y=370)
    
    # Display new event page
    view_event.mainloop()

def event_update(new_event_tk, date, attendees, name, online_link, address, suburb, postcode, state, country, event, reminders):
    # Only owner can update event
    if not check_self_organiser(event):
        save_event_error("Owner")
        return
    # Setup date object
    date = date.split("-")
    year, month, day = None, None, None
    if (len(date[0]) == 4 and len(date) == 3):
        # yyyy-mm-dd format is used
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
    elif (len(date[0])) == 2  and len(date) == 3:
        # yy-MON-dd format is used
        year = 2000 + int(date[0])
        months = [" ", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month = months.index(date[1])
        day = int(date[2])
    else:
        # Error
        save_event_error("date")
        return
    month28 = 2
    month30 = [4,6,9,11]
    if year>2050 or month<1 or month>12 or day<1 or (month == month28 and day>28) or (month in month30 and day>31) or day>31:
        # Error
        save_event_error("date")
        return
    else:
        start_event_date = Time(year, month, day, 0, 0)
        end_event_date = Time(year, month, day, 23, 59)

    # Setup location object
    location = Location()
    # If both location options are filled
    if online_link and (address or suburb or postcode or country):
        save_event_error("location")
        return
    # If no location is given
    elif not online_link and not (address and suburb and postcode and country):
        save_event_error("location")
        return
    # Online link is given
    elif online_link:
        location.init_link(online_link)
    # Address is given
    else:
        street_number = address.split(" ", 1)[0]
        street_name = address.split(" ", 1)[1]

        location.init_address(street_number, street_name, suburb, state, postcode, country)

    # create event
    """ ---------------------------------------- API ---------------------------------------- """
    updated_event = create_event(get_calendar_api(), get_events(get_calendar_api()), start_event_date, end_event_date, attendees, name, "", location, reminders)
    update_event(get_calendar_api(), get_events(get_calendar_api()), event.get_event_id(), updated_event)
    delete_event(get_calendar_api(), get_events(get_calendar_api()), updated_event.get_event_id())
    new_event_tk.destroy()

def save_event_error(error):
    save_event_error = Tk()
    save_event_error.title(error + " error")
    error_message = error + " error"
    title = Label(save_event_error, text=error_message, font=("times", 16))
    title.pack()

    return_button = Button(save_event_error, text = 'OK', command = save_event_error.destroy)
    return_button.pack()

    # Display date error page
    save_event_error.mainloop()

""" ---------------------------------------- New Event Page ---------------------------------------- """
def new_event():
    attendees = []
    reminders = []

    def add_attendee_popup():
        if len(attendees)>20:
            # Too many attendees error
            attendee_error = Tk()
            attendee_error.title("Too many attendees")
            title = Label(attendee_error, text="Maximum of 20 attendees",font=("times", 16))
            title.pack()

            return_button = Button(attendee_error, text = 'OK', command = attendee_error.destroy)
            return_button.pack()

            # Display date error page
            attendee_error.mainloop()
        else:
            # Display attendee popup page
            add_attendee_popup = Tk()
            add_attendee_popup.title("Add Attendee")
            add_attendee_popup.geometry("320x100")

            attendee_email_label = Label(add_attendee_popup, text="Attendee Email:",font=("times", 12))
            attendee_email_label.place(x=30, y=30)
            attendee_email = Entry(add_attendee_popup)
            attendee_email.place(x=140, y=30)

            cancel_button = Button(add_attendee_popup, text = 'Cancel', command = add_attendee_popup.destroy)
            cancel_button.place(x=160, y=60)

            add_button = Button(add_attendee_popup, text = 'Add', command = lambda: [add_attendee(attendee_email.get()), add_attendee_popup.destroy()])
            add_button.place(x=220, y=60)

            add_attendee_popup.mainloop()

    def add_attendee(attendee_email):
        # Add attendee to array and table
        attendee = Attendee(attendee_email)
        attendees.append(attendee)
        attendees_table.insert(parent='',index='end', values=attendee.get_email())

    def edit_attendee_popup():
        # Get the selected attendee
        selected_item = int(attendees_table.selection()[0][1:4], base=16)-1
        edit_attendee_popup = Tk()
        edit_attendee_popup.title("Add Attendee")
        edit_attendee_popup.geometry("320x100")

        attendee_email_label = Label(edit_attendee_popup, text="Attendee Email:",font=("times", 12))
        attendee_email_label.place(x=30, y=30)
        attendee_email = Entry(edit_attendee_popup)
        attendee_email.insert(0,attendees[selected_item].get_email())
        attendee_email.place(x=140, y=30)

        cancel_button = Button(edit_attendee_popup, text = 'Cancel', command = edit_attendee_popup.destroy)
        cancel_button.place(x=160, y=60)

        edit_button = Button(edit_attendee_popup, text = 'Update', command = lambda: [edit_attendee(attendee_email.get(), selected_item), edit_attendee_popup.destroy()])
        edit_button.place(x=220, y=60)

        edit_attendee_popup.mainloop()

    def edit_attendee(attendee_email, index):
        # Update the array and table
        attendees[index].set_email(attendee_email)
        selected_item = attendees_table.selection()
        attendees_table.item(selected_item, values=attendees[index].get_email())


    def delete_attendee():
        # Remove selected attendee from table and array
        selected_item = attendees_table.selection()
        attendees_table.delete(selected_item)
        del attendees[int(selected_item[0][1:4], base=16)-1]
    
    # Reminders
    def add_reminder_popup():
        # Display reminder popup page
        add_reminder_popup = Tk()
        add_reminder_popup.title("Add Reminder")
        add_reminder_popup.geometry("320x130")

        reminder_time_label = Label(add_reminder_popup, text="Reminder Time:",font=("times", 12))
        reminder_time_label.place(x=30, y=30)
        reminder_time = Entry(add_reminder_popup)
        reminder_time.place(x=140, y=30)

        reminder_method_label = Label(add_reminder_popup, text="Reminder Method:",font=("times", 12))
        reminder_method_label.place(x=30, y=50)
        reminder_methods = ["email", "popup"]
        method_variable = StringVar(add_reminder_popup)
        method_variable.set(reminder_methods[0])
        method = OptionMenu(add_reminder_popup, method_variable, *reminder_methods)
        method.place(x=170, y=50)

        cancel_button = Button(add_reminder_popup, text = 'Cancel', command = add_reminder_popup.destroy)
        cancel_button.place(x=160, y=100)

        add_button = Button(add_reminder_popup, text = 'Add', command = lambda: [add_reminder(reminder_time.get(), method_variable.get()), add_reminder_popup.destroy()])
        add_button.place(x=220, y=100)

        add_reminder_popup.mainloop()

    def add_reminder(reminder_time, reminder_method):
        # Add reminder to array and table
        reminder_time = int(reminder_time)
        try:
            reminder_time = int(reminder_time)
        except:
            time_error = Tk()
            time_error.title("Time error")
            title = Label(date_error, text="Time error",font=("times", 16))
            title.pack()
            return_button = Button(time_error, text = 'OK', command = time_error.destroy)
            return_button.pack()
            time_error.mainloop()
            return
        reminder = Reminder(reminder_method, int(reminder_time))
        reminders.append(reminder)
        reminders_table.insert(parent='',index='end', values=[reminder_time, reminder_method])

    def edit_reminder_popup():
        # Get the selected reminder
        selected_item = int(reminders_table.selection()[0][1:4], base=16)-1
        edit_reminder_popup = Tk()
        edit_reminder_popup.title("Add Reminder")
        edit_reminder_popup.geometry("320x130")

        reminder_time_label = Label(edit_reminder_popup, text="Reminder Time:",font=("times", 12))
        reminder_time_label.place(x=30, y=30)
        reminder_time = Entry(edit_reminder_popup)
        reminder_time.insert(0,reminders[selected_item].get_minutes())
        reminder_time.place(x=140, y=30)

        reminder_method_label = Label(edit_reminder_popup, text="Reminder Method:",font=("times", 12))
        reminder_method_label.place(x=30, y=50)
        reminder_methods = ["email", "popup"]
        method_variable = StringVar(edit_reminder_popup)
        method_variable.set(reminder_methods[0])
        method = OptionMenu(edit_reminder_popup, method_variable, *reminder_methods)
        method.place(x=170, y=50)

        cancel_button = Button(edit_reminder_popup, text = 'Cancel', command = edit_reminder_popup.destroy)
        cancel_button.place(x=160, y=100)

        add_button = Button(edit_reminder_popup, text = 'Update', command = lambda: [edit_reminder(reminder_time.get(), method_variable.get(), selected_item), edit_reminder_popup.destroy()])
        add_button.place(x=220, y=100)

        edit_reminder_popup.mainloop()

    def edit_reminder(reminder_time, reminder_method, index):
        # Update the array and table
        updated_reminder = Reminder(reminder_method, int(reminder_time))
        reminders[index] = updated_reminder
        selected_item = reminders_table.selection()
        reminders_table.item(selected_item, values=[reminder_time, reminder_method])


    def delete_reminder():
        # Remove selected reminder from table and array
        selected_item = reminders_table.selection()
        reminders_table.delete(selected_item)
        del reminders[int(selected_item[0][1:4], base=16)-1]

    """"""

    # New event displays
    new_event = Tk()
    new_event.title("New Event")
    new_event.geometry("640x420")
    title = Label(new_event, text="New Event",font=("times", 30, "bold"))
    title.place(relx=0.5, rely=0.12, anchor=CENTER)

    # Required entry boxes
    _y = 90
    event_name_label = Label(new_event, text="Event Name:",font=("times", 12))
    event_name_label.place(x=30, y=_y)
    event_name = Entry(new_event)
    event_name.place(x=140, y=_y)
    _y += 40

    event_date_label = Label(new_event, text="Event Date:",font=("times", 12))
    event_date_label.place(x=30, y=_y)
    event_location_online_label = Label(new_event, text="Use formats yyyy-mm-dd or dd-MON-yy",font=("times", 10))
    event_location_online_label.place(x=30, y=_y + 20)
    event_date = Entry(new_event)
    event_date.place(x=140, y=_y)
    _y += 50

    event_online_label = Label(new_event, text="Online Link:",font=("times", 12))
    event_online_label.place(x=30, y=_y)
    event_location_online_label = Label(new_event, text="If event is online, don't fill the fields below",font=("times", 10))
    event_location_online_label.place(x=30, y=_y + 20)
    event_online = Entry(new_event)
    event_online.place(x=140, y=_y)
    _y += 40

    event_address_label = Label(new_event, text="Address:",font=("times", 12))
    event_address_label.place(x=30, y=_y)
    event_address = Entry(new_event)
    event_address.place(x=140, y=_y)
    _y += 40

    event_suburb_label = Label(new_event, text="Suburb:",font=("times", 12))
    event_suburb_label.place(x=30, y=_y)
    event_suburb = Entry(new_event)
    event_suburb.place(x=140, y=_y)
    _y += 40

    event_postcode_label = Label(new_event, text="Postcode:",font=("times", 12))
    event_postcode_label.place(x=30, y=_y)
    event_postcode = Entry(new_event)
    event_postcode.place(x=140, y=_y)
    _y += 40

    event_state_label = Label(new_event, text="State:",font=("times", 12))
    event_state_label.place(x=30, y=_y)
    event_state = Entry(new_event)
    event_state.place(x=140, y=_y)
    _y += 40

    event_country_label = Label(new_event, text="Country:",font=("times", 12))
    event_country_label.place(x=30, y=_y)
    event_country = Entry(new_event)
    event_country.place(x=140, y=_y)
    
    # Attendees Table
    attendees_table = ttk.Treeview(new_event, columns = (1), show="headings", height=4)
    attendees_table.place(x=370, y=90)
    attendees_table.heading(1, text = "Attendees")
    attendees_table.column(1, width = 200)
    
    # Attendee table buttons
    add_attendee_popup_button = Button(new_event, text = 'Add', command = add_attendee_popup)
    add_attendee_popup_button.place(x=540, y=200)
    
    edit_attendee_popup_button = Button(new_event, text = 'Edit', command = edit_attendee_popup)
    edit_attendee_popup_button.place(x=500, y=200)

    delete_attendee_button = Button(new_event, text = 'Delete', command = delete_attendee)
    delete_attendee_button.place(x=450, y=200)

    # Reminders Table
    reminders_table = ttk.Treeview(new_event, columns = (1,2), show="headings", height=4)
    reminders_table.place(x=370, y=230)
    reminders_table.heading(1, text = "Reminder Time")
    reminders_table.column(1, width = 100)
    reminders_table.heading(2, text = "Method")
    reminders_table.column(2, width = 100)
    """"""
    # Reminders table buttons
    add_reminder_popup_button = Button(new_event, text = 'Add', command = add_reminder_popup)
    add_reminder_popup_button.place(x=540, y=340)
    
    edit_reminder_popup_button = Button(new_event, text = 'Edit', command = edit_reminder_popup)
    edit_reminder_popup_button.place(x=500, y=340)

    delete_reminder_button = Button(new_event, text = 'Delete', command = delete_reminder)
    delete_reminder_button.place(x=450, y=340)

    cancel_event_button = Button(new_event, text = 'Cancel Event', command = new_event.destroy)
    cancel_event_button.place(x=400, y=370)

    save_event_button = Button(new_event, text = 'Save Event', command = lambda: [save_event(new_event, event_date.get(), attendees, event_name.get(), event_online.get(), event_address.get(), event_suburb.get(), event_postcode.get(), event_state.get(), event_country.get(), reminders)])
    save_event_button.place(x=510, y=370)
    
    # Display new event page
    new_event.mainloop()

def save_event(new_event_tk, date, attendees, name, online_link, address, suburb, postcode, state, country, reminders):
    # Setup date object
    date = date.split("-")
    year, month, day = None, None, None
    if (len(date[0]) == 4 and len(date) == 3):
        # yyyy-mm-dd format is used
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
    elif (len(date[0])) == 2  and len(date) == 3:
        # dd-MON-yy format is used
        year = 2000 + int(date[2])
        months = [" ", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month = months.index(date[1])
        day = int(date[1])
    else:
        # Error
        save_event_error("date")
        return
    month28 = 2
    month30 = [4,6,9,11]
    if year>2050 or month<1 or month>12 or day<1 or (month == month28 and day>28) or (month in month30 and day>31) or day>31:
        # Error
        save_event_error("date")
        return
    else:
        start_event_date = Time(year, month, day, 0, 0)
        end_event_date = Time(year, month, day, 23, 59)

    # Setup location object
    location = Location()
    # If both location options are filled
    if online_link and (address or suburb or postcode or country):
        save_event_error("location")
        return
    # If no location is given
    elif not online_link and not (address and suburb and postcode and country):
        save_event_error("location")
        return
    # Online link is given
    elif online_link:
        location.init_link(online_link)
    # Address is given
    else:
        street_number = address.split(" ", 1)[0]
        street_name = address.split(" ", 1)[1]

        location.init_address(street_number, street_name, suburb, state, postcode, country)

    # create event
    """ ---------------------------------------- API ---------------------------------------- """
    create_event(get_calendar_api(), get_events(get_calendar_api()), start_event_date, end_event_date, attendees, name, "", location, reminders)
    new_event_tk.destroy()

def save_event_error(error):
    save_event_error = Tk()
    save_event_error.title(error + " error")
    error_message = error + " error"
    title = Label(save_event_error, text=error_message, font=("times", 16))
    title.pack()

    return_button = Button(save_event_error, text = 'OK', command = save_event_error.destroy)
    return_button.pack()

    # Display date error page
    save_event_error.mainloop()


""" ---------------------------------------- Export and Import Events ---------------------------------------- """

def export_event():
    print("event exported")

def import_event():
    print("events imported")


if __name__=='__main__':
    my_event_manager()