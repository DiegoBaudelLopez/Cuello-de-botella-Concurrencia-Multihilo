import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 8000

def manejar_cliente(conn, addr, id_cliente):
    """
    Esta funcion corre en su propio hilo.
    El hilo principal NO se bloquea aqui, sigue aceptando conexiones.
    """
    print(f"[Hilo-{id_cliente}] Atendiendo a {addr[0]}:{addr[1]}")

    conn.sendall(f"Cliente {id_cliente} aceptado. Iniciando procesamiento...\r\n".encode())

    for i in range(10, 0, -1):
        mensaje = f"   [Cliente {id_cliente}] Procesando... {i} segundos restantes\r\n".encode()
        conn.sendall(mensaje)
        print(f"    [Hilo-{id_cliente}] {i}s restantes")
        time.sleep(1)

    conn.sendall(f"[Cliente {id_cliente}] Procesamiento completado. Respuesta confirmada.\r\n".encode())
    print(f"[Hilo-{id_cliente}] Respuesta enviada. Cerrando conexion.")

    conn.close()


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind((HOST, PORT))
servidor.listen(5)

print(f"[*] Servidor CONCURRENTE escuchando en {HOST}:{PORT}")
print(f"[*] Cada cliente sera atendido en su propio hilo\n")

id_cliente = 0

while True:
    print("[*] Esperando nueva conexion...")
    conn, addr = servidor.accept()
    id_cliente += 1

    # Crear un hilo nuevo para este cliente
    hilo = threading.Thread(target=manejar_cliente, args=(conn, addr, id_cliente))
    hilo.daemon = True
    hilo.start()

    print(f"[+] Hilo-{id_cliente} iniciado. Hilos activos: {threading.active_count() - 1}")