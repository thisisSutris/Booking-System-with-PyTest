from tkinter import *
from tkinter import ttk
from MyEventManager import *
from EventPopup import *

def display_searched_events(events, search_field):
    def view_event():
        selected_item = events_table.selection()
        selected_event = events[int(selected_item[0][1:4], base=16)-1]
        event_popup(selected_event)

    # Display searched events
    display_searched_events = Tk()
    display_searched_events.title(search_field + "Events")
    display_searched_events.geometry("640x400")
    title = Label(display_searched_events, text=(search_field + "Events"),font=("times", 30, "bold"))
    title.place(relx=0.5, rely=0.15, anchor=CENTER)

    # Events Table
    events_table = ttk.Treeview(display_searched_events, columns = (1), show="headings", height=10)
    events_table.place(x=70, y=100)
    events_table.heading(1, text = "Events")
    events_table.column(1, width = 500)

    # View event button
    view_event_button = Button(display_searched_events, text = 'View', command = view_event)
    view_event_button.place(x=310, y=330)

     # Put events from API into table
    for event in events:
        events_table.insert(parent='',index='end', values=event.get_summary())

    display_searched_events.mainloop()
