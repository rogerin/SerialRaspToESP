from machine import Pin
import time
import sys

# Configura o GPIO do LED (altere o número do pino conforme necessário)
led = Pin(2, Pin.OUT)

while True:
    if sys.stdin.any():
        # Lê um byte da entrada padrão (serial)
        received = sys.stdin.read(1)
        if received == '1':
            led.value(1)  # Acende o LED
            print("LED ligado")
        elif received == '0':
            led.value(0)  # Desliga o LED
            print("LED desligado")
    time.sleep(0.1)  # Pequena pausa para não sobrecarregar o loop
