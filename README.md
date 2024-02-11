
Preparação do Ambiente:
    Este repositorio foi criado com a finalidade de implementar uma simulação de um sistema de transações bancaerias.
    Para testar o código, baixe o arquivo compactado e descompacte no seu computador ou faça um clone do projeto.
    Para testar o sistema é necessário ter o Python e o MySQL instalados no seu computador.
    Além disso as seguintes bibliotecas python são necessárias: requests,mysql-connector,tkinter e flask. Para instala-las utilizando pip, digite os seguintes comando no terminal:
        pip install requests
        pip install mysql-connector-python
        pip install tkinter
        pip install flask

Preparação do banco de dados
    Para criar e configurar o banco de dados, foi criado um script. Para executa-lo, porém, é necessário criar um susuario "daniel" com a senha "daniel".
    Para fazer isso, você pode abrir o terminal e logar com um usuario ja existente em uma sessão MySQL e digitar o comando:
    CREATE USER 'daniel'@'localhost' IDENTIFIED BY 'daniel'
    Após criado o usuario, entre na pasta DB e execute o arquivo 'create_db.py':
        python create_db.py

Preparação dos servidores:
    Para o exemplo foram criados 4 servidores: AmericanExpress, Visa, CreditMutuel, CreditAgricole
    Para rodar os servidores, abra 4 terminais e rode:
        python AmericanExpressServer.py
        python VisaServer.py
        python CreditAgricoleServer.py
        python CreditMutuelServer.py

Execução do programa:
    Para ver o funcionamento do sistema, é necessário executar o arquivo main_terminal.py:
        python main_terminal.py
    Este arquivo abrira uma tela de login referente a conta que receberam os pagamentos feitos no terminal. Para facilitar, o teste, dois botoes foram colocados: pattern1 e pattern2, que foram duas contas criadas, uma em cada banco.
    Ao logar, irá aparecer uma tela para que as informações de pagamento seham inseridas. O mesmo sistema de botoes de pattern foi adicionado para facilitar o teste.

    Além disso, é possível executar o arquivo main_account.py:
        python main_account.py
    Este arquivo abrira uma interface visual onde é possível acompanhar o saldo das contas a medida que as transações são feitas.