# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>


## Grupo 67

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/vittor-augusto/">Vitor Augusto Gomes</a>
- <a href="https://www.linkedin.com/company/inova-fusca">João Vitor Lopes Beiro</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Thyego Brandão</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gabriel Alves Costa</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Ferreira Hillesheim</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona/">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi Chiovato</a>


## 📜 Descrição

### CardioIA – Fase 1: Batimentos de Dados ###
Este projeto acadêmico do curso de IA inovador tem como objetivo construir uma plataforma digital inteligente que simula o ecossistema de uma cardiologia moderna.  
Nesta primeira fase, coletamos, organizamos e preparamos **três tipos de dados fundamentais**: numéricos, textuais e visuais, que serão utilizados nas fases seguintes para alimentar algoritmos de Inteligência Artificial.

---

## Parte 1 – Dados Numéricos (IoT)

### Arquivos
- `cardioIA_fase1_dados_numericos.csv` → dados de pacientes cardíacos.
- `cardioIA_fase1_dicionario_dados.csv` → descrição e significado das variáveis.

### Fonte
Os dados foram **simulados** com base em parâmetros clínicos comuns, incluindo: idade, sexo, pressão arterial, colesterol, histórico de doenças cardíacas, frequência cardíaca, entre outros.

### Variáveis Relevantes
Algumas das variáveis mais importantes para análises de IA:
- `age_years` → idade influencia risco cardíaco.
- `systolic_bp_mmHg` e `diastolic_bp_mmHg` → pressão arterial.
- `cholesterol` e frações (`HDL`, `LDL`) → perfil lipídico.
- `heart_disease` → variável alvo para classificação.

### Link Público
Os dados numéricos estão hospedados em:  
[cardioIA_fase1_dados_numericos.csv](COLE_SEU_LINK_DO_DRIVE)  
[cardioIA_fase1_dicionario_dados.csv](COLE_SEU_LINK_DO_DRIVE)

---

## Parte 2 – Dados Textuais (NLP)

### Arquivos
- `Análise do Conceito de Risco Cardiovascular.txt`  
- `Importância da Educação Para Prevenção Cardiovascular.txt`  

### Fonte
Textos relacionados a doenças cardiovasculares, sintomas e tratamentos foram obtidos de fontes acadêmicas e literatura clássica (SciELO, BVS, Projeto Gutenberg).

### Uso em IA
- Análise de sentimentos (ex.: percepção de pacientes sobre sintomas).  
- Extração de sintomas e termos médicos para NLP.  
- Classificação de tópicos e identificação de padrões clínicos.  

### Link Público
[texto1.txt](COLE_SEU_LINK_DO_DRIVE)  
[texto2.txt](COLE_SEU_LINK_DO_DRIVE)

---

## Parte 3 – Dados Visuais (VC) – Raio-X de Tórax

### Fonte das Imagens
Para esta fase do projeto, utilizamos o **Heart Dataset** disponibilizado no [Mendeley Data](https://data.mendeley.com/datasets/czmn5ypdz5/1?utm_source=chatgpt.com), contendo exames de raio-X de tórax de pacientes. As imagens originais estão em formato `.nii.gz` (formato médico NIfTI) e foram convertidas para `.png` para facilitar o uso em análise de Visão Computacional.

### Processamento e Conversão
- Cada arquivo `.nii.gz` representa um exame volumétrico.
- Extraímos a **fatia central** de cada volume para gerar imagens 2D em escala de cinza.
- As imagens foram organizadas em:

assets/images/xray/

- Para fins do projeto, selecionamos **100 imagens** representativas do conjunto convertido, garantindo diversidade entre exames normais e patológicos.
- Renomeadas sequencialmente de `xray_001.png` até `xray_100.png`.

### Justificativa para Análise
Essas imagens serão utilizadas para:
- **Detecção de anomalias**: identificar alterações estruturais no coração e tórax.
- **Classificação visual**: separar exames normais de patológicos.
- **Treinamento de modelos de Visão Computacional**: segmentação, reconhecimento de bordas e padrões cardíacos.

### Links Públicos
As 100 imagens selecionadas estão hospedadas no Google Drive/OneDrive para acesso público:  
[Link para as imagens](COLE_AQUI_O_LINK_DO_DRIVE)


---


## Observações Finais
Esta fase do projeto tem como objetivo **construir a base de dados para o CardioIA**, garantindo relevância clínica e diversidade nos dados.  
Os datasets foram preparados considerando princípios de **Governança de Dados**, permitindo uso futuro em algoritmos de IA com consistência e qualidade.

## Organização do Repositório

CardioIA/
│
├─ assets/
│ ├─ images/xray/ # 100 imagens de raio-X
│ └─ docs/ # textos .txt
│
├─ cardioIA_fase1_dados_numericos.csv
├─ cardioIA_fase1_dicionario_dados.csv
└─ README.md


---


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).



## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


