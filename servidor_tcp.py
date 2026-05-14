import socket
import time

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 8000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind((HOST, PORT))
servidor.listen(5)
 
print(f"[*] Servidor escuchando en {HOST}:{PORT}")
 
while True:
    print("[*] Esperando conexión...")
    conn, addr = servidor.accept()
    print(f"[+] Cliente conectado desde {addr[0]}:{addr[1]}")
 
    conn.sendall(b"Conexion aceptada. Procesando datos...\r\n")
 
    print("[~] Simulando procesamiento pesado (10 segundos)...")
    time.sleep(10)
 
    conn.sendall(b"Procesamiento completado. Respuesta confirmada.\r\n")
    print(f"[+] Respuesta enviada a {addr[0]}:{addr[1]}")
 
    conn.close()
    print("[*] Conexion cerrada.\n")
 