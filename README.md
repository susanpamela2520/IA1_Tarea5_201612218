# 🤖 IA1_Tarea5 — Bot de Telegram

**Curso:** Inteligencia Artificial 1  
**Universidad:** Universidad de San Carlos de Guatemala  
**Facultad de Ingeniería — Escuela de Ciencias y Sistemas**

---

| Nombre | Carnet | Actividad realizada |
|--------|--------|---------------------|
| Susan Pamela Herrera Monzon | 201612218 | Configuración del repositorio, creación del bot, implementación de los 4 comandos (`/hola`, `/hora`, `/contacto`, `/proyecto`), manejo de variables de entorno, documentación completa en README |

---

**MediLogic Assistant Bot** es un mini asistente de Telegram desarrollado en Python para el proyecto de Inteligencia Artificial 1. El bot provee información instantánea sobre el proyecto MediLogic, el integrante del grupo y la hora actual en Guatemala.

Está construido con la librería `python-telegram-bot` v21 (arquitectura asíncrona) y utiliza `python-dotenv` para la gestión segura del token.

---

## Lista de comandos

| Comando | Descripción |
|---------|-------------|
| `/hola` | Saluda al usuario por su nombre y muestra los comandos disponibles |
| `/hora` | Muestra la fecha y hora actual en zona horaria de Guatemala (UTC-6) |
| `/contacto` | Muestra los datos del integrante del grupo (nombre, carnet, facultad, GitHub) |
| `/proyecto` | Describe el proyecto MediLogic: tecnologías, funcionalidades y repositorio |

---

## Instrucciones de instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/<tu-usuario>/IA1_Tarea5_Grupo#.git
cd IA1_Tarea5_Grupo#
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Configurar el token

```bash
cp .env.example .env
```

Edita el archivo `.env` y reemplaza el valor con tu token real de BotFather:

```
TELEGRAM_BOT_TOKEN=TU_TOKEN_AQUI
```

> ⚠️ **IMPORTANTE:** Nunca subas el archivo `.env` a GitHub. Está incluido en `.gitignore`.

### 4. Ejecutar el bot

```bash
python bot.py
```

---

## 🛠️ Tecnologías utilizadas

- **Python 3.10+**
- **python-telegram-bot 21.6** — Framework asíncrono para bots de Telegram
- **python-dotenv 1.0.1** — Gestión de variables de entorno
- **pytz 2024.1** — Manejo de zonas horarias

---

## 📁 Estructura del repositorio

```
IA1_Tarea5_Grupo#/
├── bot.py            # Código fuente del bot
├── requirements.txt  # Dependencias Python
├── .env.example      # Plantilla de configuración (sin token real)
├── .gitignore        # Archivos excluidos del repositorio
└── README.md         # Este archivo
```

---

## 🔗 Link del grupo de Telegram

> _[Enlace al grupo de Telegram donde el bot está activo]_

---

*Tarea 05 — Inteligencia Artificial 1 — 2026*
