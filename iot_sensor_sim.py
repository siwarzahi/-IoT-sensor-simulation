import random
import time
import matplotlib.pyplot as plt
import smtplib

def get_sensor_data():
    temp = round(random.uniform(20.0, 30.0), 2)  # Température simulée
    hum = round(random.uniform(40.0, 70.0), 2)   # Humidité simulée
    return temp, hum

while True:
    temperature, humidity = get_sensor_data()
    print(f"Temp: {temperature}°C, Humidity: {humidity}%")
    time.sleep(2)  # Met à jour toutes les 2 secondes

temps = []
temperature_data = []
humidity_data = []

plt.show()
 # Mode interactif
import matplotlib.pyplot as plt

temps = []
temperature_data = []
humidity_data = []

plt.show()  # Mode interactif

for i in range(50):
    temp, hum = get_sensor_data()
    temperature_data.append(temp)
    humidity_data.append(hum)
    temps.append(i)

    plt.clf()
    plt.plot(temps, temperature_data, label='Temp (°C)')
    plt.plot(temps, humidity_data, label='Humidity (%)')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.pause(0.1)


from email.mime.text import MIMEText

def send_email(subject, body):
    sender = 'siwarzahi10@gmail.com'
    receiver = 'zasiwar6@gmail.com'
    password = 'pelr ennj odam nmrs'  # Mot de passe application Gmail

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

# Exemple d'utilisation
send_email("Capteur IoT Alert", "Température simulée: 28°C")
