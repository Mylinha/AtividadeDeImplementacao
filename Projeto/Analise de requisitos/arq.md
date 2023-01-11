	[UC01] Autenticar Usuário Identificação: [UC01]
Descrição: Validar os dados de usuário e senha para que o funcionário tenha acesso ao sistema.
 Atores: coordenadores, professores, técnicos e bolsitas.
Prioridade: Essencial 
Pré-condições: O ator deve possuir cadastro no sistema
 Pós-condições: O ator estará logado no sistema

Fluxo de Eventos 
1. O ator deve entrar no sistema
 2. O ator deve escrever o seu usuário e senha nos devidos campos 
3. O sistema realizará a validação dos dados do usuário 
4. O ator será direcionado para a pagina de menu do sistema
 Fluxo Secundário 
1. O ator deve entrar no sistema 
2. O ator deve escrever o seu usuário e senha nos devidos campos 
3. O sistema emitirá uma mensagem informando que os dados não são de um usuário válido e que o ator deve digitar valores corretos de usuário e senha





	[UC02] Cadastrar o funcionário no sistema: [UC02]

Descrição:  Permitindo com que seus dados sejam armazenados e fique listado na lista de funcionários da empresa, suas funções dentro dela.

Atores: coordenadores e bolsitas.
Prioridade: Essencial 
Pré-condições: O ator deve ser funcionário da empresa.
Pós-condições: O ator estará registrado no sistema.

Fluxo de Eventos 
1. O ator deve entrar no sistema
 2. O ator deve escrever o seu usuário e senha nos devidos campos 
3. O sistema realizará a validação dos dados do usuário 
4. O ator será direcionado para a página de menu do sistema
5. Entrará na área de cadastro.
6. Cadastrará as informações do funcionário, que será salvo no sistema.
 
Fluxo Secundário 
1. O ator deve entrar no sistema 
2. O ator deve escrever o seu usuário e senha nos devidos campos 
3. Entrará no menu e logo em seguida na área de cadastros.
4. Caso este funcionário já esteja cadastrado o sistema emitirá uma mensagem informando que os dados são de um usuário válido já existente no sistema.



	[UC03]Marcar os horários de visitas: [UC03]

Descrição:  Para que o funcionário que é permitido acessar esta função, possa conseguir editar esta lista, e marcar os horários de visitas.
 Atores: coordenadores e bolsitas.
Prioridade: Essencial 
Pré-condições: O ator deve ser funcionário da empresa.
 Pós-condições:  Horário de visita marcado.

Fluxo de Eventos 
1. O ator deve entrar no sistema
2. O ator deve escrever o seu usuário e senha nos devidos campos 
3. O sistema realizará a validação dos dados do usuário 
4. O ator será direcionado para a página de menu do sistema
5. Entrará na área de agenda de visitas
6.Colocará as informações da data e hora da visita na agenda, que será salvo no sistema.
 
Fluxo Secundário 
1. O ator deve entrar no sistema 
2. O ator deve escrever o seu usuário e senha nos devidos campos 
3. Entrará no menu e logo em seguida na área de agenda de visitas.
4. Caso o horário que a mesma já esteja preenchida o sistema emitirá uma mensagem informando que o horário já está preenchido.


	[UC04] Efetuar logoff [UC04]

Descrição:  O ator sairá do sistema.
 Atores: coordenadores, professores, técnicos e bolsitas.
Prioridade: Importante 
Pré-condições: O ator deve ser funcionário da empresa.
 Pós-condições: O ator não estará mais logado no sistema.

Fluxo de Eventos 
1.	A qualquer momento o ator pode clicar em “Sair” e dessa forma ele não estará mais logado no sistema.



	[UC05] Gerar listas de funcionamento [UC05]

Descrição:  Gerar listas de todos os funcionários da empresa e dos horários de visitas registrados.
 Atores: coordenadores e bolsitas.
Prioridade: Importante 
Pré-condições: O ator deve ser funcionário da empresa.
 Pós-condições: Imprimiu as informações precisas.

Fluxo de Eventos 
1. O ator deve entrar no sistema
2. O ator deve escrever o seu usuário e senha nos devidos campos 
3. O sistema realizará a validação dos dados do usuário 
4. O ator será direcionado para a página de menu do sistema
5. Entrará na área de informações da empresa
6. Escolherá quais informações quer que seja imprimida
7. Terá acesso as informações e poderá imprimi -las caso necessário.
