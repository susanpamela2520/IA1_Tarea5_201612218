import logging
import os
from datetime import datetime
import pytz
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# ──────────────────────────────────────────
# Configuración de logs
# ──────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ──────────────────────────────────────────
# Cargar variables de entorno
# ──────────────────────────────────────────
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# ══════════════════════════════════════════
# HANDLERS DE COMANDOS
# ══════════════════════════════════════════

async def cmd_hola(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /hola — Saluda al usuario por su nombre de Telegram.
    """
    user = update.effective_user
    nombre = user.first_name if user.first_name else "usuario"
    mensaje = (
        f"👋 ¡Hola, {nombre}!\n\n"
        "Soy el asistente del proyecto de Inteligencia Artificial 1.\n"
        "Estoy aquí para brindarte información sobre el grupo y el proyecto.\n\n"
        "📋 *Comandos disponibles:*\n"
        "  /hola      — Saludo de bienvenida\n"
        "  /hora      — Hora actual (Guatemala)\n"
        "  /contacto  — Información del integrante\n"
        "  /proyecto  — Descripción del proyecto\n"
    )
    await update.message.reply_text(mensaje, parse_mode="Markdown")
    logger.info("Comando /hola ejecutado por %s", user.username)


async def cmd_hora(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /hora — Devuelve la fecha y hora actual en zona horaria de Guatemala.
    """
    zona = pytz.timezone("America/Guatemala")
    ahora = datetime.now(zona)
    fecha_str = ahora.strftime("%A, %d de %B de %Y")
    hora_str  = ahora.strftime("%H:%M:%S")

    mensaje = (
        "🕐 *Hora actual (Guatemala)*\n\n"
        f"📅 Fecha : {fecha_str}\n"
        f"⏰ Hora  : {hora_str}\n"
        f"🌎 Zona  : America/Guatemala (UTC-6)"
    )
    await update.message.reply_text(mensaje, parse_mode="Markdown")
    logger.info("Comando /hora ejecutado por %s", update.effective_user.username)


async def cmd_contacto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /contacto — Muestra los datos del integrante del grupo.
    """
    mensaje = (
        "👤 *Integrante del Grupo*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📛 *Nombre:* Susan Daniela Ajú Carrillo\n"
        "🎓 *Carnet:* 201612218\n"
        "🏫 *Universidad:* Universidad de San Carlos de Guatemala\n"
        "📐 *Facultad:* Ingeniería\n"
        "💻 *Escuela:* Ingeniería en Ciencias y Sistemas\n"
        "📚 *Curso:* Inteligencia Artificial 1\n\n"
        "📬 *GitHub:* github.com/201612218\n"
    )
    await update.message.reply_text(mensaje, parse_mode="Markdown")
    logger.info("Comando /contacto ejecutado por %s", update.effective_user.username)


async def cmd_proyecto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /proyecto — Describe el proyecto del grupo.
    """
    mensaje = (
        "🤖 *Proyecto: MediLogic*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📌 *Descripción:*\n"
        "MediLogic es un sistema experto de diagnóstico médico desarrollado "
        "con Python, Prolog y Tkinter. Utiliza una base de conocimiento en "
        "Prolog para inferir posibles diagnósticos a partir de síntomas "
        "ingresados por el usuario.\n\n"
        "🛠️ *Tecnologías utilizadas:*\n"
        "  • Python 3\n"
        "  • SWI-Prolog + pyswip\n"
        "  • Tkinter (interfaz gráfica)\n"
        "  • Lógica de primer orden y cláusulas Horn\n\n"
        "🎯 *Funcionalidades principales:*\n"
        "  • Registro de síntomas por módulo Admin\n"
        "  • Diagnóstico automático por inferencia\n"
        "  • Base de conocimiento editable\n"
        "  • Interfaz gráfica intuitiva\n\n"
        "📁 *Repositorio:* IA1\\_1S2026\\_Carnet\n"
        "👤 *Integrante:* Susan Daniela Ajú Carrillo — 201612218\n"
    )
    await update.message.reply_text(mensaje, parse_mode="Markdown")
    logger.info("Comando /proyecto ejecutado por %s", update.effective_user.username)


# ══════════════════════════════════════════
# PUNTO DE ENTRADA
# ══════════════════════════════════════════

def main() -> None:
    if not TOKEN:
        raise ValueError(
            "No se encontró TELEGRAM_BOT_TOKEN. "
            "Asegúrate de definirlo en el archivo .env"
        )

    app = ApplicationBuilder().token(TOKEN).build()

    # Registrar handlers
    app.add_handler(CommandHandler("hola",     cmd_hola))
    app.add_handler(CommandHandler("hora",     cmd_hora))
    app.add_handler(CommandHandler("contacto", cmd_contacto))
    app.add_handler(CommandHandler("proyecto", cmd_proyecto))

    logger.info("Bot iniciado. Esperando comandos...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
