import re

def process_command(command):
    # Inicializa os dados extraídos
    acao = "unknown"
    parametros = {}
    
    # Expressões regulares para extrair destinatário e assunto
    email_match = re.search(r'para\s+([\w\.-]+@[\w\.-]+)', command, re.IGNORECASE)
    assunto_match = re.search(r'assunto:\s*(.+)', command, re.IGNORECASE)

    # Verifica se é um comando de envio de e-mail
    if "email" in command.lower():
        acao = "enviar_email"
        if email_match:
            parametros["destinatario"] = email_match.group(1)
        else:
            parametros["destinatario"] = "não identificado"
        if assunto_match:
            parametros["assunto"] = assunto_match.group(1).strip()
        else:
            parametros["assunto"] = "não identificado"

    # Retorna o JSON completo
    return {
        "ação": acao,
        "parametros": parametros,
        "comando_original": command
    }

# Exemplo de teste
comando_exemplo = "neuro, mande um email para moraesguilherme844@gmail.com com o assunto: teste"
print(process_command(comando_exemplo))

