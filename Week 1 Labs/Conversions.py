"""Write a module that provides the following conversions:

    Length - feet (') and inches ('') to meters (m)
    Mass - pounds (lbs) to kilograms (kg)
    Temperature - Kelvin (K) to Celsius (oC)
    Time - hours (h) and minutes(m) to seconds (s) """


def to_feet(meters):
    total_feet = meters * 3.28084
    feet = int(total_feet)
    inches = round((total_feet - feet) * 12, 1)
    return f"{feet}ft, {inches}in"


def to_meters(feet):
    total_inches = feet * 12
    meters = round(total_inches * 0.0254, 2)
    return f"{meters}m"


def to_kilos(pounds):
    return f"{round(pounds * 0.453, 2)}kg"


def to_pounds(kilos):
    return f"{round(kilos * 2.20462, 2)}lbs"


def celsius_to_kelvin(celsius):
    kelvin = round(celsius + 273.15, 2)
    if kelvin < 0:
        return "Error"
    return f"{kelvin}K"


def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        return "Error"
    celsius = f"{round(kelvin - 273.15, 2)}C"
    return celsius


def to_secs(mins):
    return f"{mins * 60}secs"


def to_hrsmins(secs):
    total_mins = int(secs/60)
    hrs = total_mins // 60
    mins = total_mins % 60
    sec = secs % 60
    return f"{hrs}hrs, {mins}mins, {sec}secs"
