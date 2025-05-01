# server.py
from mcp.server.fastmcp import FastMCP
from typing import Dict, Any, Optional, Callable
import logging
import requests

# Create an MCP server
mcp = FastMCP("Trabalho Doutorado", "v1.0.0")

# --- Configuração de Logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_SEND_TEXT_URL = "http://localhost:3000/api/sendText"
API_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}
DEFAULT_SESSION = "default"
REQUEST_TIMEOUT = 15  # Segundos

CONTATOS_PRECARREGADOS = {
    "sandro": "5564992770830@c.us",
    "alison": "5564992422171@c.us",
    "joão": "5511999990001@c.us",
    "maria": "5521988880002@c.us",
}


# criando tools
@mcp.tool()
def tool_enviar_mensagem_whatsapp(destinatario: str, mensagem: str) -> Dict[str, Any]:
    """
    Ferramenta para enviar uma mensagem de texto via WhatsApp API.
    Busca o chatId e faz a chamada POST.
    """
    logger.info(f"Executando tool_enviar_mensagem_whatsapp para '{destinatario}' com texto: '{mensagem}'")

    chat_id = buscar_contato_whatsapp(destinatario)

    data = {
        "chatId": chat_id,
        "text": mensagem,
        "session": DEFAULT_SESSION
    }

    try:
        response = requests.post(
            API_SEND_TEXT_URL,
            json=data,
            headers=API_HEADERS,
            timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()
        try:
            return {"status": "sucesso", "resposta_api": response.json()}
        except requests.exceptions.JSONDecodeError:
            return {"status": "sucesso", "resposta_api_raw": response.text}

    except requests.exceptions.Timeout:
        return {"status": "erro", "detalhe": "A API externa demorou muito para responder."}
    except requests.exceptions.RequestException as e:
        return {"status": "erro", "detalhe": f"Erro na comunicação com a API: {e}"}
    except Exception as e:
        return {"status": "erro", "detalhe": f"Erro inesperado na ferramenta: {e}"}


# adicionando recursos
@mcp.resource("buscar://{nome}")
def buscar_contato_whatsapp(nome: str) -> Dict[str, Any]:
    """
    Função auxiliar para obter o chatId a partir de um nome ou número.
    """
    logger.info(f"Executando buscar_contato_whatsapp para '{nome}'")

    nome_lower = nome.lower()

    if nome_lower in CONTATOS_PRECARREGADOS:
        numero = CONTATOS_PRECARREGADOS[nome_lower]
        return numero
    else:
        return "nao_encontrado"