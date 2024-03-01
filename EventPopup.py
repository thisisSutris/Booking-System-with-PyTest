from tkinter import *
from tkinter import ttk
from SmallMessages import *
from Attendee import *
from Reminder import *
from MyEventManager import *

def event_popup(event = None):
    def add_attendee_popup():
        if len(attendees)>20:
            input_error("too many attendee")
            return
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
        try:
            reminder_time = int(reminder_time)
        except:
            input_error("reminder time")
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
        try:
            reminder_time = int(reminder_time)
        except:
            input_error("reminder time")
            return
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
    
    # If an event was provided, there is already an existing event and this will be used to update it
    if event:
        updating_event = TRUE
    else:
        updating_event = FALSE
    # Initialise variables
    name = ""
    date = ""
    organiser = ""
    online_link = ""
    address = ""
    suburb = ""
    postcode = ""
    state = ""
    country = ""
    attendees = [] 
    reminders = []

    # If updating event, there will be value in fields
    if updating_event:
        name = event.get_summary()
        date_imported = event.get_starting_time()
        date = str(date_imported.get_year()) + "-" + str(date_imported.get_month()) + "-" + str(date_imported.get_day())
        if event.get_organiser():
            organiser = event.get_organiser()

        location = event.get_location()
        if location.get_link():
            online_link = location.get_link()
        else:
            address = str(location.get_street_number()) + " " + str(location.get_street_name())
            suburb = location.get_suburb()
            postcode = location.get_postcode()
            state = location.get_state()
            country = location.get_country()

        if event.get_attendees():
            attendees = event.get_attendees()
        if event.get_reminders():
            reminders = event.get_reminders()
    
    # Display event information
    view_event = Tk()
    view_event.title("View Event")
    view_event.geometry("640x420")
    title = Label(view_event, text="View Event",font=("times", 30, "bold"))
    title.place(relx=0.5, rely=0.1, anchor=CENTER)

    y_ = 90
    event_name_label = Label(view_event, text="Event Name:",font=("times", 12))
    event_name_label.place(x=30, y=y_)
    event_name = Entry(view_event)
    event_name.insert(0,name)
    event_name.place(x=140, y=y_)
    y_ += 40

    print(organiser)
    event_organiser_label = Label(view_event, text="Event Organiser:",font=("times", 12))
    event_organiser_label.place(x=30, y=y_)
    event_organiser = Entry(view_event)
    event_organiser.insert(0,organiser)
    event_organiser.place(x=140, y=y_)
    y_ += 40

    event_date_label = Label(view_event, text="Event Date:",font=("times", 12))
    event_date_label.place(x=30, y=y_)
    event_location_online_label = Label(view_event, text="Use formats yyyy-mm-dd or dd-MON-yy",font=("times", 10))
    event_location_online_label.place(x=30, y=y_ + 20)
    event_date = Entry(view_event)
    event_date.insert(0,date)
    event_date.place(x=140, y=y_)
    y_ += 50

    event_online_label = Label(view_event, text="Online Link:",font=("times", 12))
    event_online_label.place(x=30, y=y_)
    event_location_online_label = Label(view_event, text="If event is online, don't fill the fields below",font=("times", 10))
    event_location_online_label.place(x=30, y=y_ + 20)
    event_online = Entry(view_event)
    event_online.insert(0, online_link)
    event_online.place(x=140, y=y_)
    y_ += 40

    event_address_label = Label(view_event, text="Address:",font=("times", 12))
    event_address_label.place(x=30, y=y_)
    event_address = Entry(view_event)
    event_address.insert(0, address)
    event_address.place(x=140, y=y_)
    y_ += 40

    event_suburb_label = Label(view_event, text="Suburb:",font=("times", 12))
    event_suburb_label.place(x=30, y=y_)
    event_suburb = Entry(view_event)
    event_suburb.insert(0, suburb)
    event_suburb.place(x=140, y=y_)
    y_ += 40

    event_postcode_label = Label(view_event, text="Postcode:",font=("times", 12))
    event_postcode_label.place(x=30, y=y_)
    event_postcode = Entry(view_event)
    event_postcode.insert(0, postcode)
    event_postcode.place(x=140, y=y_)
    y_ += 40

    event_state_label = Label(view_event, text="State:",font=("times", 12))
    event_state_label.place(x=30, y=y_)
    event_state = Entry(view_event)
    event_state.insert(0, state)
    event_state.place(x=140, y=y_)
    y_ += 40

    event_country_label = Label(view_event, text="Country:",font=("times", 12))
    event_country_label.place(x=30, y=y_)
    event_country = Entry(view_event)
    event_country.insert(0, country)
    event_country.place(x=140, y=y_)

    # Attendees Table
    attendees_table = ttk.Treeview(view_event, columns = (1), show="headings", height=4)
    attendees_table.place(x=370, y=90)
    attendees_table.heading(1, text = "Attendees")
    attendees_table.column(1, width = 200)

    # Put attendees from API into table
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

    if updating_event:
        delete_event_button = Button(view_event, text = 'Delete Event', command = lambda: [event_delete(event), view_event.destroy()])
        delete_event_button.place(x=300, y=370)

        if event.cancelled:
            cancel_event_button = Button(view_event, text = 'Uncancel Event', command = lambda: [event.uncancel_event(), view_event.destroy()])
            cancel_event_button.place(x=380, y=370)
        else:
            cancel_event_button = Button(view_event, text = 'Cancel Event', command = lambda: [event.cancel_event(), view_event.destroy()])
            cancel_event_button.place(x=380, y=370)

    cancel_button = Button(view_event, text = 'Cancel', command = view_event.destroy)
    cancel_button.place(x=460, y=370)

    save_event_button = Button(view_event, text = 'Save Event', command = lambda: [event_update(updating_event, event, event_name.get(), event_organiser.get(), event_date.get(), event_online.get(), event_address.get(), event_suburb.get(), event_postcode.get(), event_state.get(), event_country.get(), attendees, reminders), view_event.destroy()])
    save_event_button.place(x=510, y=370)
    
    # Display new event page
    view_event.mainloop()

def event_delete(event):
    api = get_calendar_api()
    events = get_events(api)
    delete_event(api, events, event.get_event_id())
    success_page()

def event_cancel():
    print("event cancelled")
    success_page()

def event_update(updating_event, event, name, organiser, date, online_link, address, suburb, postcode, state, country, attendees, reminders):
    # Only owner can update event
    if updating_event:
        if not check_self_organiser(event):
            input_error("Owner")
            return
    
    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    # Setup date object
    try:
        date = date.split("-")
    except:
        input_error("date")
        return
    year, month, day = None, None, None
    if (len(date[0]) == 4 and len(date) == 3):
        # yyyy-mm-dd format is used
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
    elif (len(date[0])) == 2  and len(date) == 3:
        # dd-MON-yy format is used
        year = 2000 + int(date[2])
        print(year)
        
        if date[1] in months:
            month = months.index(date[1]) + 1
        else:
            input_error("date")
        day = int(date[0])
    else:
        # Error
        input_error("date")
        return
    month28 = 2
    month30 = [4,6,9,11]
    if year>2050 or month<1 or month>12 or day<1 or (month == month28 and day>28) or (month in month30 and day>31) or day>31 or day<1:
        # Error
        input_error("date")
        return
    else:
        start_event_date = Time(year, month, day, 0, 0)
        end_event_date = Time(year, month, day, 23, 59)
    
    if str(start_event_date) < str(get_time_now()):
        input_error("time")
        return

    # Setup location object
    location = Location()
    # If both location options are filled
    if online_link and (address or suburb or postcode or country):
        input_error("location")
        return
    # If no location is given
    elif not online_link and not (address and suburb and postcode and country):
        input_error("location")
        return
    # Online link is given
    elif online_link:
        location.init_link(online_link)
    # Address is given
    else:
        street_number = address.split(" ", 1)[0]
        street_name = address.split(" ", 1)[1]

        location.init_address(street_number, street_name, suburb, state, postcode, country)

    # Setup Organiser
    organiser = Organiser(organiser)

    # create event
    api = get_calendar_api()
    events = get_events(api)
    if updating_event:
        update_event_(api, events, start_event_date, end_event_date, attendees, name, organiser, location, reminders, event)
    else:
        new_event = create_event(api, events, start_event_date, end_event_date, attendees, name, "", location, reminders)
        transfer_organiser(api, new_event, organiser)
    success_page()
        
def update_event_(api, events, start_event_date, end_event_date, attendees, name, organiser, location, reminders, event):
    event.set_starting_time(start_event_date)
    event.set_ending_time(end_event_date)
    event.set_attendees(attendees)
    event.set_summary(name)
    event.set_organiser(organiser)
    event.set_location(location)
    event.set_reminders(reminders)
    update_event(api, events, event.get_event_id(), event)
    transfer_organiser(api, event, organiser)
