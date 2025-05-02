import os
from pathlib import Path
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler, ContextTypes, MessageHandler, filters

# Configuração do .env
BASE_DIR = Path(__file__).parent.parent
ENV_PATH = BASE_DIR / '.env'

if not ENV_PATH.exists():
    raise FileNotFoundError(f"Arquivo .env não encontrado em: {ENV_PATH}")

load_dotenv(ENV_PATH, override=True)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
CHANNEL_LINK = os.getenv("CHANNEL_LINK")

if not TOKEN or len(TOKEN) < 30:
    raise ValueError(f"Token inválido: '{TOKEN}'. Verifique o .env")

async def handle_fan_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Processa mensagens para o chat da torcida"""
    try:
        # Verifica se é uma mensagem válida
        if not update.message or not update.message.text:
            return
        
        # Ignora mensagens muito curtas (opcional)
        if len(update.message.text) < 5:
            await update.message.reply_text("❌ Mensagem muito curta. Escreva mais!")
            return
        
        user = update.message.from_user
        message_text = update.message.text
        
        # DEBUG: Mostra no console
        print(f"Mensagem recebida de {user.first_name}: {message_text}")
        
        # Envia a mensagem para o canal
        await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=f"📢 Mensagem de {user.first_name}:\n\n{message_text}\n\n🟡⚫ #FURIA",
            disable_web_page_preview=True
        )
        
        # Confirmação para o usuário
        await update.message.reply_text(
            "✅ Sua mensagem foi enviada para o chat da torcida!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Ir para o Chat", url=CHANNEL_LINK)],
                [InlineKeyboardButton("Voltar ao Menu", callback_data="main_menu")]
            ])
        )
    except Exception as e:
        print(f"ERRO no chat da torcida: {str(e)}")
        await update.message.reply_text(
            "❌ Ocorreu um erro ao enviar sua mensagem. Tente novamente mais tarde.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Voltar ao Menu", callback_data="main_menu")]
            ])
        )



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envia o menu principal"""
    await show_main_menu(update, context)

## Mostra o menu principal com opções
async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, message: str = None):
    """Mostra o menu principal com opções"""
    keyboard = [
        [InlineKeyboardButton("Próximo Jogo 🎮", callback_data="next_match")],
        [InlineKeyboardButton("Notícias 📰", callback_data="news")],
        [InlineKeyboardButton("Elenco 👥", callback_data="team")],
        [InlineKeyboardButton("Chat da Torcida 💬", callback_data="fan_chat")],
        [InlineKeyboardButton("Sair ❌", callback_data="exit")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    text = "🟡⚫ *Menu Principal* ⚫🟡\n\nEscolha uma opção:"
    if message:
        text = message + "\n\n" + text
    
    # Edita a mensagem existente ou envia uma nova
    if update.callback_query:
        await update.callback_query.edit_message_text(
            text=text,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    else:
        await update.message.reply_text(
            text=text,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

## Manipula os botões
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manipula todos os callbacks dos botões"""
    query = update.callback_query
    await query.answer()
    

    if query.data == "next_match":
        keyboard = [
            [InlineKeyboardButton("Voltar ↩️", callback_data="main_menu")],
            [InlineKeyboardButton("Sair ❌", callback_data="exit")]
        ]
        await query.edit_message_text(
            text="⏳ *Próximo Campeonato:*\n\nFASE SUIÇA\n📅 10/05 - 18/05\n VALENDO R$425.000,00🏆\n 🟡⚫GO FURIA ⚫🟡\n Para mais informações acesse: https://draft5.gg/equipe/330-FURIA/campeonatos",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    elif query.data == "news":
        keyboard = [
            [InlineKeyboardButton("Voltar ↩️", callback_data="main_menu")],
            [InlineKeyboardButton("Sair ❌", callback_data="exit")]
        ]
        await query.edit_message_text(
            text="📢 *Últimas Notícias:*\n\n- FURIA apresenta ex-Falcons como novo auxiliar técnico\n- FalleN divulga primeiro PUG da nova FURIA na Europa\n FURIA pode reforçar comissão técnica com cazaque ex-AVANGAR, sugere rumor",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    elif query.data == "team":
        keyboard = [
            [InlineKeyboardButton("Voltar ↩️", callback_data="main_menu")],
            [InlineKeyboardButton("Sair ❌", callback_data="exit")]
    ]
    
    # Texto formatado com o nome do time e instagram
        team_text = (
            "👥 *Elenco Principal FURIA CS:GO* ⚫🟡\n\n"
            "• [MOLODOY](https://www.instagram.com/danil.molodoy_/)\n"
            "• [YEKINDAR](https://www.instagram.com/yek1ndar/)\n"
            "• [FalleN](https://www.instagram.com/fallen/)\n"
            "• [KSCERATO](https://www.instagram.com/kscerato/)\n"
            "• [yuurih](https://www.instagram.com/yuurihfps/)\n\n"
            "[Ver estatísticas completas](https://draft5.gg/equipe/330-FURIA)"
    )
    
        await query.edit_message_text(
            text=team_text,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown',
            disable_web_page_preview=True  # Evita pré-visualização de links
    )
    elif query.data == "fan_chat":
        keyboard = [
            [InlineKeyboardButton("Voltar ↩️", callback_data="main_menu")],
            [InlineKeyboardButton("Ir para o Chat", url=CHANNEL_LINK)]
        ]
        await query.edit_message_text(
            text="💬 *Chat da Torcida*\n\nDigite sua mensagem abaixo e ela será enviada para o chat oficial da torcida FURIA!",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )
    
    elif query.data == "main_menu":
        await show_main_menu(update, context)
    
    elif query.data == "exit":
        await query.edit_message_text(
            text="🟡⚫ *Obrigado por usar o FURIA Bot!* ⚫🟡\n\nUse /start para iniciar novamente.",
            parse_mode='Markdown'
        )

def main():
    app = Application.builder().token(TOKEN).build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND & ~filters.FORWARDED,
        handle_fan_chat
    ))
    
    print("🤖 Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
