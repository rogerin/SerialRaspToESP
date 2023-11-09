# Comunicação serial Raspberry PI com ESP32

<p aling="center">
  <img src="/assets/imgs/rasp.png" width="200" />
  <img src="/assets/imgs/esp.png" width="200" /> 
</p>


## Codigo Python Raspberry

Um exemplo de código que você pode executar em seu ambiente local para enviar um '1' através da porta serial a cada 5 segundos, mas apenas se um dispositivo ESP32 estiver conectado. O código a seguir faz uso da biblioteca `pyserial` para comunicação serial e `serial.tools.list_ports` para listar e verificar os dispositivos conectados.

```python
import serial
import serial.tools.list_ports
import time

# Nome da porta serial que você deseja verificar (altere conforme necessário)
PORT_NAME = "COM3"

def is_esp32_connected(port_name):
    """Verifica se um ESP32 está conectado na porta especificada."""
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        # Aqui você pode adicionar condições adicionais para verificar se é um ESP32
        if port_name in port.device:
            print(f"Dispositivo encontrado na porta: {port.device}")
            return True
    return False

def send_data_to_esp32(port_name):
    """Envia um '1' para o ESP32 conectado a cada 5 segundos."""
    try:
        with serial.Serial(port_name, 9600, timeout=1) as ser:
            while True:
                ser.write(b'1')  # Envia um '1' como um byte
                print("Dados enviados: 1")
                time.sleep(5)  # Espera por 5 segundos antes de enviar o próximo '1'
    except serial.SerialException as e:
        print(f"Erro ao abrir a porta serial: {e}")

# Verificar se o ESP32 está conectado antes de começar a enviar dados
if is_esp32_connected(PORT_NAME):
    send_data_to_esp32(PORT_NAME)
else:
    print("ESP32 não está conectado.")
```

Para executar este código:

1. Certifique-se de que você tem a biblioteca `pyserial` instalada. Se não, você pode instalá-la usando pip:

```sh
pip install pyserial
```

2. Substitua `COM3` pelo nome correto da sua porta serial onde o ESP32 está conectado.

3. Execute o script em seu ambiente local. Ele tentará localizar um dispositivo na porta especificada e, se encontrado, começará a enviar '1' a cada 5 segundos.

Lembre-se de que para confirmar se um dispositivo conectado é realmente um ESP32, você pode precisar verificar mais informações do que apenas a porta. Isso pode incluir verificar o identificador do hardware ou o nome do produto, se disponível através da listagem de portas seriais.


## Código MicroPython ESP32

Um exemplo de código que você pode usar em um ESP32 rodando MicroPython. Este script irá escutar a porta serial do ESP32 por dados recebidos. Se ele receber o caractere '1', ele acenderá um LED conectado a um dos GPIOs do ESP32. Se receber um '0', ele desligará o LED.

```python
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
```