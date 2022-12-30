Fala galera!!

Hoje estou trazendo um jogo da forca feito através de funções em Python

Para começar o jogo digite preparacao() e insira a palavra e a dica.
Depois digite jogar() e boa diversão!!


Processo de criação do código

Primeiro eu defini 5 variáveis(palavra,resposta,erros,palpites e dica)

A primeira função eu chamei de preparação, nela eu peço que seja digitada a palavra a ser adivinhada, transformo essa palavra toda em letra maiúscula para evitar problemas, depois peço que entre com uma dica e para finalizar faço um for para inserir _ na variável resposta, de acordo com a quantidade de letras da palavra.

A segunda função eu chamei de jogar, primeiro eu faço um if para saber se a variável resposta é igual a variável palavra(explico o motivo mais a frente), depois faço 2 prints, um dizendo as letras que já foram palpitadas e outro dizendo a dica e mostrando a quantidade de letras da palavra, através do _ que inserimos em resposta com a primeira função.
Em seguida faço um esquema com if e for, onde peço que seja inserida uma letra, insiro essa letra na variável palpites, verifico se essa letra corresponde a alguma letra da palavra, se sim, insiro ela na variável resposta na posição certa, faço um print e chamo a função novamente para reiniciar todo o ciclo, caso o palpite seja errado, eu diminuo 1 de erros, faço um print e chamo a função e reinicio todo o ciclo.
Assim que todas as letras forem advinhadas, o primeiro if irá encerrar a função dizendo que a palavra foi descoberta.
Também coloquei uma opção de chute caso a pessoa queira tentar adivinhar. Basta escrever a palavra chutar ao invés de digitar uma letra.

A terceira função é o boneco que representa os erros na forca, essa função é chamada automaticamente dentro da função jogar().
________
|      |
|      O
|     /|\
|     / \
A função termina quando se acerta todos as letras(que é verificada no primeiro if), acertando ou errando o chute ou quando terminam as tentativas(que são definidas na variável erros).
