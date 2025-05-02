# 🟡⚫ FURIA FanBot ⚫🟡

Bot oficial da torcida FURIA CS:GO no Telegram, criado para conectar fãs e fornecer informações atualizadas sobre o time.

## 📌 Recursos Principais

- ✅ Menu interativo com opções
- 🎮 Próximos jogos e campeonatos
- 📰 Últimas notícias do time  
- 👥 Elenco completo com redes sociais
- 💬 Chat integrado com a torcida
- 🔔 Notificações (em desenvolvimento)

## 🚀 Como Executar

### Pré-requisitos
- Python 3.11+
- Conta no Telegram
- Token do Bot (@BotFather)
- Canal do Telegram (para o chat da torcida)

### Instalação
```bash
# Clone o repositório
git clone https://github.com/Pedr00ga/Telegram-Furia-Bot.git

# Acesse a pasta
cd Telegram-Furia-Bot

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

Para rodar o programa é necessario de 3 informações:
TOKEN = Criar um bot no telegram utilizando @BotFather
CHANNEL_ID = Verificar o ID do seu canal utilizando o bot @Get my ID
CHANNEL_LINK = Link para acessar o seu canal

Colocar todas essas informações do .env na pasta raiz com os seguintes nomes:
TELEGRAM_BOT_TOKEN=SEU TOKEN
CHANNEL_ID="SUA ID"
CHANNEL_LINK="SEU LINK"

Após criado, basta rodar o arquivo start.bat na pasta raiz e interagir com o bot com /start no telegram para abrir o menu principal de interações
