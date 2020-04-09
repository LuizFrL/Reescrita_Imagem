# Reescrita_Imagem
Reescrever uma imagem de preferencia em Preto e Branco.

# Objetivo
Em uma posição inicial determinada por mim, lê uma imagem com openCV. Foi desenvolvido para
suprir uma necessidade minha de não conseguir desenhar bem no Gartic kkkkkk.

## Como usar
* Colocar no programa onde ira ser reescrito a imagem, a cor preta e com o tamanho da linha de
um pixel.
* Pesquisar uma imagem do Google em preto e branco de preferencia e colocar no mesmo diretório
do repositorio (Caso coloque em outro diretório, deve informar onde está a imagem a ser 
reescrita).
* Definir o inicio da imagem, colocando a posição do pixel de inicio.
* Não mexer no mouse durante a execução.

## Funcionamento
* Le a imagem como uma matriz de elementos, com linhna e os pixels com uma array de 3 elementos
(Representando o RGB).
* Ao passar por uma linha, passa por cada píxel presente e mexe o mouse 1 pixel para a direita.
* Faz uma média de cada pixel e verifica se ele é mais escuro ou mais claro (Em uma array de 3
elementos com R=255, G=255, B=255 [255, 255, 255] representa o branco, uma array com R=0, G=0, 
B=0 [0, 0, 0] representa o preto. Para identificar se é um pixel escuro ou não, ele faz a média
entre esses 3 elementos, caso seja menor que 127.5 ele é identificado como preto).
* Se o pixel for identificado como escuro, ele pressiona o botão direito do mouse fazendo ele dar um click
e colorindo o pixel com a cor escolhida.