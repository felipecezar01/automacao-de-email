# Sistema de Envio de E-mails

Este projeto é uma ferramenta simples de envio de e-mails utilizando Python. Ele permite que os usuários enviem e-mails personalizados em formato HTML para uma lista de destinatários especificada.

## Funcionalidades

- Envio de e-mails em formato HTML.
- Configuração simples do servidor SMTP.
- Suporte a múltiplos destinatários.

## Tecnologias Utilizadas

- Python
- Bibliotecas: `smtplib`, `email.message`

## Como Usar

1. **Configurar Credenciais do SMTP**: Para usar este script, você precisa fornecer suas credenciais SMTP no lugar dos espaços reservados no código. Isso inclui o seu endereço de e-mail e uma senha de aplicativo, que pode ser gerada nas configurações da sua conta do Google.

2. **Editar o Conteúdo do E-mail**: O corpo do e-mail está em formato HTML e pode ser editado para atender às suas necessidades. Basta modificar o conteúdo dentro das tags `<body>` do template HTML fornecido no código.

3. **Adicionar Destinatários**: Adicione os e-mails dos destinatários à lista `destinatarios` no script para começar a enviar e-mails.

4. **Executar o Script**: Execute o script para enviar os e-mails. Cada destinatário receberá o e-mail personalizado conforme definido no corpo do e-mail.

## Segurança

Este script utiliza TLS para garantir uma conexão segura com o servidor SMTP. É altamente recomendável não compartilhar ou expor suas credenciais de e-mail em repositórios públicos.

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou novas funcionalidades, fique à vontade para criar um pull request ou abrir um issue.

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
