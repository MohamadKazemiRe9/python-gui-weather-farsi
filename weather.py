import tkinter as tk
import requests
from translate import Translator
import datetime
from tkinter.messagebox import showerror

window = tk.Tk()
window.title("وضعیت آب و هوا")
window.minsize(200, 500)


city_name = tk.StringVar()
wheather_type = tk.StringVar()
city_label = tk.StringVar()
temp = tk.StringVar()
wind = tk. StringVar()
sunset = tk.StringVar()

def widgets():
    label = tk.Label(window, text="وضعیت آب و هوا", width=25, height=2)
    label.config(font=("Titr",22,"bold"), fg="#000", bg="lightblue")
    label.grid(row=0, columnspan=2)

    labe_name = tk.Label(window, text="نام شهر")
    labe_name.config(font=("Lalezar",18,"bold"), fg="red")
    labe_name.grid(row=1, column=0, pady=10)

    input_name = tk.Entry(window, textvariable=city_name)
    input_name.grid(row=1, column=1, pady=10)

    search_btn = tk.Button(text="جستجو", width=10, height=2, background="green", fg="white", font=("None",15), command=search)
    search_btn.grid(row=2, columnspan=2, pady=10)

    label_city_name = tk.Label(text="نام شهر", font=("Aviny",16,"bold"), fg="blue")
    label_city_name.grid(row=3, column=0, pady=10)

    label_city = tk.Label(text="----",font=("Aviny",14), textvariable=city_label)
    label_city.grid(row=3, column=1,pady=10)

    label_wheather_type = tk.Label(text="وضعیت", font=("Aviny",16,"bold"), fg="blue")
    label_wheather_type.grid(row=4, column=0, pady=5)

    label_wheather = tk.Label(text="----",font=("Aviny",14), textvariable=wheather_type)
    label_wheather.grid(row=4, column=1, pady=5)

    label_temp = tk.Label(text="دما", font=("Aviny",16,"bold"), fg="blue")
    label_temp.grid(row=5, column=0, pady=5)

    label_temp_show = tk.Label(text="----",font=("Aviny",14), textvariable=temp)
    label_temp_show.grid(row=5, column=1, pady=5)

    label_wind = tk.Label(text="سرعت باد", font=("Aviny",16,"bold"), fg="blue")
    label_wind.grid(row=6, column=0, pady=5)

    label_wind_show = tk.Label(text="----",font=("Aviny",14), textvariable=wind)
    label_wind_show.grid(row=6, column=1, pady=5)

    label_sunset = tk.Label(text="غروب خورشید", font=("Aviny",16,"bold"), fg="blue")
    label_sunset.grid(row=7, column=0, pady=5)

    label_sunset_show = tk.Label(text="----",font=("Aviny",14), textvariable=sunset)
    label_sunset_show.grid(row=7, column=1, pady=5)

def second_to_clock(seconds):
        m , s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return h, m, s

def time_calculate(seconds):
    sunsetdate = datetime.datetime.fromtimestamp(seconds)
    now = datetime.datetime.now()
    if now >  sunsetdate:
        result = now - sunsetdate
        second = result.seconds
        h,m,s = second_to_clock(second)
        sunset.set(str(h)+"ساعت و"+str(m)+ "دقیقه و"+str(s)+" ثانیه پیش")
        
    else:
        result = sunsetdate - now
        second = result.seconds
        h,m,s = second_to_clock(second)
        sunset.set(str(h)+"ساعت و"+str(m)+ "دقیقه و"+str(s)+" ثانیه دیگر")



def search():
    city = city_name.get()
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    app_id = "109d424b54ae460e540bad9953047757"
    try:
        result = requests.get(url.format(city, app_id)).json()
        translator= Translator(to_lang="Persian")
        status = translator.translate(result['weather'][0]['main'])
        city = translator.translate(result['name'])
        wheather_type.set(status)
        city_label.set(city)
        temp.set(str(round(result['main']['temp']-273.15,2) )+'درجه سانتی گراد')
        wind.set(str(result['wind']['speed'])+"متر بر ثانیه")
        time_calculate(result['sys']['sunset'])
    except:
        showerror("خطا!","نام شهر صحیح نمی باشد")
        city_name.set("")
widgets()

window.mainloop()





