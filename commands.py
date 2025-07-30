def process_command(command):
    # Aqui você pode usar NLP, regex ou chamadas para modelos de linguagem
    if "enviar email" in command.lower():
        return {"action": "send_email", "status": "pending", "details": "Preparando envio de e-mail"}
    elif "criar reunião" in command.lower():
        return {"action": "create_meeting", "status": "pending", "details": "Criando evento no Outlook"}
    else:
        return {"action": "unknown", "status": "error", "details": "Comando não reconhecido"}
