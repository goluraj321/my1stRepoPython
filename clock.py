from time import sleep, strftime

while True:
    print(strftime("%H:%M:%S"), end="\r", flush=True)
    sleep(1)
