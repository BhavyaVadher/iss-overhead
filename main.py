import requests
from datetime import datetime
# import smtplib
# import time


MY_LAT = 22.257933 # My latitude
MY_LONG = 70.808052 # My longitude
time_now = 0

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print=(f"sunrise hour is {sunrise}")
    print=(f"sunset hour is {sunset}")

    time_now = datetime.now().hour
    # print(f"Current time is {time_now}")
    
    if time_now >= sunset or time_now <= sunrise:
        return True

is_iss_overhead()
is_night()


if is_iss_overhead() and is_night():
    print('''Subject:Look Up👆
          The ISS is above you in the sky.''')
else:
    print(f"Wait for {is_night()-time_now} hours")  
    
# while True:
#     time.sleep(60)
#     if is_iss_overhead() and is_night():
#         connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=MY_EMAIL,
#             msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
#         )


