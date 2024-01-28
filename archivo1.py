import datetime as dt

ahora = dt.datetime.now()

print(f"Estamos {ahora.day} del mes {ahora.month} del año {ahora.year}")
print(f"Hora: {ahora.hour} --- Minutos: {ahora.minute} --- Segundos: {ahora.second}")