Atividade implementada na disciplina de Tópicos Avançados em IA Generativa do programa de Doutorado em Ciência da Computação do INF/UFG, sob orientação do professor Dr. Anderson Soares.

O servidor deverá ter a tool: send_message que recebe como parâmetros o número no formato internacional (+5511..) e a mensagem a ser enviada. 
A tool deverá se comunicar com um servidor local de WaHa onde deve fazer uma chamada post na rota de envio de mensagens. 
Para instanciar o servidor de WaHa você deve seguir os passos do video: https://www.youtube.com/watch?v=RFerMyAUPRg https://waha.devlike.pro/docs/overview/quick-start/ 
Com o servidor autenticado, a tool deve fazer uma chamada POST na rota /api/sendText, passando como parâmetros o número recebido e a mensagem. 
Implemente também um resource no servidor que tenha 3 números de telefone e nome ja pré carregados para que o client de MCP utilize ele ao ser chamado com: "Envie uma mensagem de bom dia para o João". 
