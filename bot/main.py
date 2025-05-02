import os
from pathlib import Path
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler, ContextTypes

# Configuração do .env
BASE_DIR = Path(__file__).parent.parent
ENV_PATH = BASE_DIR / '.env'

if not ENV_PATH.exists():
    raise FileNotFoundError(f"Arquivo .env não encontrado em: {ENV_PATH}")

load_dotenv(ENV_PATH, override=True)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN or len(TOKEN) < 30:
    raise ValueError(f"Token inválido: '{TOKEN}'. Verifique o .env")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler do comando /start com menu interativo"""
    keyboard = [
        [InlineKeyboardButton("Próximo Jogo 🎮", callback_data="next_match")],
        [InlineKeyboardButton("Notícias 📰", callback_data="news")],
        [InlineKeyboardButton("Torcida Ao Vivo 🔊", callback_data="live_chat")],
        [InlineKeyboardButton("Elenco 👥", callback_data="team")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        text="🟡⚫ *Bem-vindo ao Bot Oficial da Torcida FURIA!* ⚫🟡\n\nEscolha uma opção:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para os botões inline"""
    query = update.callback_query
    await query.answer()
    
    if query.data == "next_match":
        await query.edit_message_text(
            text="⏳ *Próximo Jogo:*\nFURIA vs NAVI\n📅 15/05 - 19h\n🏆 IEM Katowice\n\n🔗 https://www.furia.gg/agenda", 
            parse_mode='Markdown'
        )
    elif query.data == "news":
        await query.edit_message_text(
            text="📢 *Últimas Notícias:*\n\n- FURIA anuncia novo patrocinador\n- KSCERATO eleito MVP do mês\n\n🔗 https://www.furia.gg/noticias",
            parse_mode='Markdown'
        )
    elif query.data == "live_chat":
        await query.edit_message_text(
            text="💬 *Chat da Torcida Ativado!*\n\nEnvie mensagens e elas aparecerão aqui para outros fãs!\n\nDigite /sair para voltar ao menu",
            parse_mode='Markdown'
        )
    elif query.data == "team":
        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=open("assets/furia_team.jpg", "rb"),
            caption="👥 *Elenco Principal FURIA CS:GO:*\n\n• arT (IGL)\n• KSCERATO\n• yuurih\n• chelo\n• FalleN\n\n🔗 https://www.furia.gg/elenco",
            parse_mode='Markdown'
        )

if __name__ == "__main__":
    print(f"🔍 .env carregado de: {ENV_PATH}")
    print(f"🔑 Token usado: {TOKEN[:10]}...{TOKEN[-6:]}")
    
    app = Application.builder().token(TOKEN).build()
    
    # Registra os handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("🤖 Bot iniciado com menu interativo. Pressione CTRL+C para parar")
    app.run_polling()