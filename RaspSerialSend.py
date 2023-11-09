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
