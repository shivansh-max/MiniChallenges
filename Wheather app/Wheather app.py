# Imports
import tkinter as tk
import requests

# global
WIDTH = 700
HEIGHT = 500

# Root window
root = tk.Tk()
root.title('Wheather app @Shivansh')

# Functions
def test_function(entry):
    print('This is the entry : ', entry)


# Faranite
def format_response(weather):
    try:
        # Getting specific information
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = float(weather['main']['temp'])
        temp2 = ((temp - 32) * 5) // 9

        # giving the answer
        final_string = 'City : %s \nCondition: %s \nTempreture: (°F): %s \nTempreture: (°C): %s' % (
        name, desc, temp,temp2)
    except:
        final_string = 'There was a problem retreving that information'

    return final_string


# The function to get the weather
def get_weather(city):
    # Keys and urls
    wheather_key = 'fdebe23da7db60522fe2952ca445f7dd'
    url = 'http://api.openweathermap.org/data/2.5/weather?'

    # paramaters
    params = {'APPID': wheather_key, 'q': city, 'units': 'imperial'}

    # the response
    response = requests.get(url, params=params)
    weather = response.json()

    print(weather)


    label['text'] = format_response(weather)

# canvas
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# The image in the background
background_image = tk.PhotoImage(file='Landscape.png.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# frame which has th botton and the entry
frame = tk.Frame(root, bg='#80c1ff', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# entry that asks for the users input
entry = tk.Entry(frame, font=('Comic sans ms', 15))
entry.place(relwidth=0.65, relheight=1)

# button that gives the answer
button = tk.Button(frame, text='Get Wheather', font=('Comic sans ms', 15),
                   command=lambda: get_weather(city=entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

# Lower frame
lower_frame = tk.Frame(root, bg='#80c1ff', bd=15)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# label
label = tk.Label(lower_frame, font=('Comic sans ms', 15))
label.place(relwidth=1, relheight=1)

root.mainloop()