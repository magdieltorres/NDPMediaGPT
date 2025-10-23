
# 🤖 NDP WhatsApp GPT Bot

Este proyecto permite conectar tu número de WhatsApp Business con el modelo GPT-3.5 para responder automáticamente a los mensajes que lleguen a tu número.

## ✅ ¿Qué necesitas?

1. Una cuenta en [https://developers.facebook.com/](https://developers.facebook.com/)
2. Haber creado una app y activado el producto **WhatsApp Cloud API**
3. Tu número de teléfono de prueba (ya lo tienes ✅)
4. Una cuenta en [https://platform.openai.com](https://platform.openai.com) con una clave API

## 🚀 ¿Cómo usarlo?

### 1. Sube estos archivos a un repositorio GitHub

Incluye:
- app.py
- requirements.txt

### 2. Ve a [https://render.com](https://render.com)

- Crea cuenta e inicia sesión
- Haz clic en "New Web Service"
- Conecta tu GitHub
- Selecciona el repositorio
- Build command: deja en blanco
- Start command: `gunicorn app:app`

### 3. Configura el webhook en Meta

- En tu app de Meta, ve a WhatsApp > Webhooks
- Callback URL: `https://tu-app.onrender.com/webhook`
- Verify Token: `ndpgpt123`

✅ ¡Listo! Ya tu bot estará respondiendo mensajes con GPT.

