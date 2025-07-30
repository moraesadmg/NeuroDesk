import re

def extrair_assunto(comando):
    # Expressões regulares para capturar o assunto com diferentes variações
    padroes_assunto = [
        r"assunto\s*[:=]?\s*([^\.,\n]+)",  # assunto: teste ou assunto = teste
        r"assunto\s+é\s+([^\.,\n]+)",      # assunto é teste
        r"com\s+o\s+assunto\s+([^\.,\n]+)" # com o assunto teste
    ]
    
    for padrao in padroes_assunto:
        match = re.search(padrao, comando, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    
    return "Assunto não especificado"

# Exemplo de teste
comando_exemplo = "mandeu um email assunto teste, para moraes@gg.com, mensagem ola guilherme"
assunto_extraido = extrair_assunto(comando_exemplo)
assunto_extraido

        }

    # Criar reunião
    elif "criar reunião" in command_lower or "agendar reunião" in command_lower:
        data = re.search(r'data: ([\w\s:/-]+)', command_lower)
        participantes = re.findall(r'com (\S+@\S+)', command_lower)
        response["ação"] = "criar_reuniao"
        response["parametros"] = {
            "data": data.group(1) if data else "",
            "participantes": participantes
        }

    # Enviar mensagem no Teams
    elif "mensagem no teams" in command_lower or "enviar mensagem no teams" in command_lower:
        destinatario = re.search(r'para (\S+@\S+)', command_lower)
        mensagem = re.search(r'mensagem: ([\w\s]+)', command_lower)
        response["ação"] = "enviar_mensagem_teams"
        response["parametros"] = {
            "destinatario": destinatario.group(1) if destinatario else "",
            "mensagem": mensagem.group(1) if mensagem else ""
        }

    # Comparar nota fiscal
    elif "comparar nota fiscal" in command_lower or "comparar ncm" in command_lower or "comparar icms" in command_lower or "comparar ipi" in command_lower:
        response["ação"] = "comparar_nota_fiscal"
        response["parametros"] = {
            "arquivo_nota": "nota_fiscal.pdf",
            "arquivo_pedido": "pedido.pdf"
        }

    # Atualizar planilha
    elif "atualizar planilha" in command_lower or "atualizar excel" in command_lower:
        response["ação"] = "atualizar_planilha"
        response["parametros"] = {
            "arquivo": "planilha.xlsx",
            "abas": ["dados", "resumo"]
        }

    # Gerar relatório Power BI
    elif "gerar relatório power bi" in command_lower or "gerar relatório no power bi" in command_lower:
        response["ação"] = "gerar_relatorio_powerbi"
        response["parametros"] = {
            "dashboard": "vendas",
            "filtros": ["último mês"]
        }

    # Criar PCs no Proteus
    elif "criar pcs no proteus" in command_lower or "criar pc no proteus" in command_lower:
        response["ação"] = "criar_pc_proteus"
        response["parametros"] = {
            "dados": "dados_do_pc"
        }

    # Responder perguntas consultando IA
    elif "quantos graus" in command_lower or "qual a temperatura" in command_lower or "responder pergunta" in command_lower:
        response["ação"] = "consultar_ia"
        response["parametros"] = {
            "pergunta": command
        }

    # Pesquisar coisas
    elif "pesquisar" in command_lower or "procure" in command_lower or "buscar" in command_lower:
        response["ação"] = "pesquisar_informacao"
        response["parametros"] = {
            "consulta": command
        }

    # Procurar fornecedores
    elif "procurar fornecedores" in command_lower or "buscar fornecedores" in command_lower:
        item = re.search(r'fornecedores para (.+)', command_lower)
        response["ação"] = "procurar_fornecedores"
        response["parametros"] = {
            "item": item.group(1) if item else ""
        }

    return response

