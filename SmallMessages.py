from tkinter import *
def input_error(error_type):
    # Create error page
    input_error = Tk()
    input_error.title(error_type + " error")
    error_message = error_type + " error"
    title = Label(input_error, text=error_message, font=("times", 16))
    title.pack()

    # Return button
    return_button = Button(input_error, text = 'OK', command = input_error.destroy)
    return_button.pack()

    # Display date error page
    input_error.mainloop()

def success_page():
    # Create error page
    success_page = Tk()
    success_page.title("Success")
    title = Label(success_page, text="Success", font=("times", 16))
    title.pack()

    # Return button
    return_button = Button(success_page, text = 'OK', command = success_page.destroy)
    return_button.pack()

    # Display date error page
    success_page.mainloop()