1.	Requisitos funcionais (Casos de uso)

1.1.	Requisitos comuns ao usuário 

1.1.1.	[RF001] Autenticar funcionário.

Prioridade:  Essencial

Validar os dados do usuário e permitir que o funcionário tenha acesso ao sistema. Para isso, o funcionário vai informar o seu CPF. A única forma do mesmo ter acesso ao sistema.

1.1.2.	 [RF002] Efetuar Logoff.

Prioridade: Importante

Permite que o funcionário saia do sistema.

1.2.	Outros requisitos

1.2.1.	  [RF003] Cadastrar o funcionário no sistema.

Prioridade: Essencial

Permitindo com que seus dados sejam armazenados e fique listado na lista de funcionários da empresa, suas funções dentro dela.


1.2.2.	  [RF005]  O sistema deve permitir a geração da lista de todos os funcionários e suas funções.

Prioridade: Importante

Para que a empresa tenha o controle dos funcionários que nela trabalham.


1.2.3.	   [RF006] O sistema deve permitir o acesso a os horários de visita 

  Prioridade: Essencial

Para que o funcionário que é permitido acessar esta função, possa conseguir editar esta lista, e marcar os horários de visitas.


1.2.4.	 [RF008]  O sistema deve permitir a geração da agenda de visitas

  Prioridade: Importante

Para que o funcionário tenha o controle dos horários.



2.	Requisitos não funcionais

2.1.	[NFR001]  Armazenar todos os dados dos funcionários em uma base de MySQL

Prioridade: Desejavel

Para que tudo esteja bem armazenado e não seja perdido com facilidade.

2.2.	[NFR002]  Armazenar toda a agenda de visitas em uma base de MySQL .

Prioridade: Essencial

Para que tudo esteja bem armazenado e não seja perdido com facilidade.

2.3.	[NFR003]  Os dados dos horários de funcionalidade de cada funcionário estejam coligados com o BD das visitas.

Prioridade: Essencial

Para que ao atualizar os horários dos funcionários, a agenda de visitas tenha os dias e horários corretos, para que não haja interferência nas funcionalidades da empresa, garantindo uma melhor organização e funcionamento da mesma.

2.4.	[NFR004]  Interface intuitiva

Prioridade: Essencial

Tanto funcionários com habilidades com computador quanto funcionários com dificuldade, usarão o sistema. Portanto a interface deve ser clara e objetiva.

2.5.	[NFR005]  Backup 

Prioridade: Essencial

Deve haver algumas cópias dos dados em servidores diferentes para evitar a perda de dados. O backup deve ser feito uma vez ao dia


2.6.	[NFR006]  Restrição de acesso

Prioridade: Essencial

Cada tipo de usuário deve ter acesso apenas às funções designadas para ele.

2.7.	[NFR007]  Mensagens de erro

Prioridade: Essencial

O sistema deve apresentar mensagem de erro, quando for o caso, de forma clara o objetiva.


