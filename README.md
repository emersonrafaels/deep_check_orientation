
<h1 align="center">
    <img alt="Deep Check Orientation" title="#DeepCheckOrientation" src="./assets/banner.png" />
</h1>

<h4 align="center"> 
	🚧 Deep Check Orientation 1.0 🚀 em desenvolvimento... 🚧
</h4>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/tgmarinho/nlw1?color=%2304D361">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/emersonrafaels/deep_check_orientation">

  	
  <a href="https://www.linkedin.com/in/emerson-rafael/">
    <img alt="Siga no Linkedin" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
  </a>
	
  
  <a href="https://github.com/emersonrafaels/deep_check_orientation/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/emersonrafaels/deep_check_orientation">
  </a>

  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
   <a href="https://github.com/emersonrafaels/deep_check_orientation/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/emersonrafaels/deep_check_orientation?style=social">
  </a>
</p>


## 💻 Sobre o projeto

📷 Deep Check Orientation é um projeto que utiliza aprendizado profundo (deep learning) para verificação da orientação de uma imagem e rotação adequada da mesma. ao ser enviada uma imagem (em qualquer formato), retorna-se o número de rotações necesárias e a imagem rotacionada corretamente.

Os passos realizados são:
1) Leitura da imagem em rgb
2) Pipeline de aumento de imagem usando albumentations (classe: compose)
3) Realização da predição usando uma rede neural do tipo resnet
4) Obtenção das predições de orientação da imagem
5) Cálculo do número de rotações necessárias para orientação correta da imagem.

Projeto desenvolvido durante utilizando a rede **swsl_resnext50_32x4d** oferecida pelo [Ternaus].

## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python]

## 🚀 Como executar o projeto

1. pip install requirements.txt
2. Abrir a linha de comando (cmd) e digitar: python main.py <imagem_para_rotacionar>. 
Ex: python main.py "..\allPd.jpg".

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas (O download pode ser realizado pela própria página do Python ou Anaconda):
[Python](https://www.anaconda.com/products/individual).

## 📝 Licença

Este projeto esta sobe a licença MIT.

Feito com ❤️ por Emerson Rafael 👋🏽 [Entre em contato!](https://www.linkedin.com/in/emerson-rafael/)

[Ternaus]: https://github.com/ternaus/check_orientation
[Python]: https://www.python.org/downloads/