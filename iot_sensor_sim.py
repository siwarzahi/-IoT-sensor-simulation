import random
import time
import matplotlib.pyplot as plt
import smtplib
from email.mime.text import MIMEText

# Fonction pour simuler le capteur
def get_sensor_data():
    temp = round(random.uniform(20.0, 35.0), 2)
    hum = round(random.uniform(40.0, 70.0), 2)
    return temp, hum

# Fonction pour envoyer l'email
def send_email(subject, body):
    sender = 'siwarzahi10@gmail.com'
    receiver = 'zasiwar6@gmail.com'
    password = 'pelr ennj odam nmrs'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

# Listes pour le graphe
temps = []
temperature_data = []
humidity_data = []

plt.ion()  # Mode interactif

# Boucle principale
for i in range(50):  # 50 mesures pour l'exemple
    temp, hum = get_sensor_data()
    
    # Ajouter les valeurs aux listes
    temperature_data.append(temp)
    humidity_data.append(hum)
    temps.append(i)
    
    # Afficher le graphe
    plt.clf()
    plt.plot(temps, temperature_data, label='Température (°C)')
    plt.plot(temps, humidity_data, label='Humidité (%)')
    plt.xlabel('Mesure')
    plt.ylabel('Valeur')
    plt.legend()
    plt.pause(0.1)
    
    print(f"Température: {temp}°C, Humidité: {hum}%")
    
    # Vérifier seuil pour envoyer email
    if temp > 30:
        send_email("Alerte Température", f"La température a dépassé 30°C: {temp}°C")
    
    time.sleep(1)
