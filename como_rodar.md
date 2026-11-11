# Como operar:
 Hospede o Worker: Coloque o worker.py em uma pasta e rode `python -m http.server 8000` para que os containers consigam baixá-lo.


Configure o IP: `No main.py`, altere http://seu-ip:8000/worker.py para o IP da sua máquina.

Execute o Controlador: Rode `python main.py.`

Mecânica de Funcionamento:

**Distribuição**: O controlador usa a API do Docker para instanciar imagens Ubuntu limpas.

**Injeção**: O comando sh -c transforma o container em um agente de ataque no momento do boot, instalando as dependências necessárias em tempo real.

**Escalabilidade**: Cada container roda 500 threads de sockets TCP. Se você subir 10 containers, terá 5.000 conexões simultâneas tentando saturar o alvo.

**Painel**: O loop de monitoramento usa o método .reload() do objeto container para verificar se o processo ainda está em execução no daemon do Docker.