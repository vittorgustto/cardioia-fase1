# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="./assets/logo-fiap (1).png" alt="FIAP - Faculdade de Informática e Administração Paulista" style="border:0; width:40%; height:40%;">
  </a>
</p>

<br>


## Grupo 67

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/vittor-augusto/">Vitor Augusto Gomes</a>
- <a href="https://www.linkedin.com/in/jo%C3%A3o-vitor-lopes-beiro-59a007248/">João Vitor Lopes Beiro</a>

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
Os dados foram **simulados** com base em parâmetros clínicos comuns e realistas refletindo medidas comuns em exames e avaliações médicas de rotina, incluindo: idade, sexo, pressão arterial, colesterol, histórico de doenças cardíacas, frequência cardíaca, entre outros. O dataset é composto por variáveis demográficas, laboratoriais e clínicas que podem auxiliar na análise de risco cardiovascular.

### Variáveis Relevantes
As variáveis a seguir foram destacadas por sua importância no contexto de projetos de Inteligência Artificial aplicada à saúde:
- Idade (anos) → fator de risco fundamental, pois a probabilidade de doenças cardiovasculares aumenta com o envelhecimento.
- Pressão Arterial Sistólica e Diastólica (mmHg) → essenciais para identificar hipertensão, uma das principais causas de complicações cardíacas.
- Colesterol Total, HDL e LDL (mg/dL) → indicadores diretos do perfil lipídico, amplamente utilizados para avaliar risco de aterosclerose.
- Glicemia em Jejum (mg/dL) → importante para identificar diabetes ou pré-diabetes, condições fortemente associadas a problemas cardiovasculares.
- Histórico Familiar (0/1) → representa predisposição genética, que aumenta significativamente o risco de eventos cardíacos.
- Tabagismo (0/1) → hábito de alto impacto no risco de infarto e outras doenças do coração.

### Justificativa
Essas variáveis foram escolhidas por combinarem fatores de risco modificáveis (como colesterol, pressão arterial e tabagismo) e não modificáveis (como idade e histórico familiar). Essa integração é essencial para modelos de Machine Learning capazes de prever riscos e apoiar decisões médicas preventivas.

### Link
Os dados numéricos estão na seguinte pasta:  
- [cardioIA_fase1_dados_numericos.csv](data/cardioIA_fase1_dados_numericos.csv)
- [cardioIA_fase1_dicionario_dados.csv](data/cardioIA_fase1_dicionario_dados.csv)
- [data_dictionary.md](data/data_dictionary.md)

---

## Parte 2 – Dados Textuais (NLP)

### Arquivos
- `Análise do Conceito de Risco Cardiovascular.txt`  
- `Importância da Educação Para Prevenção Cardiovascular.txt`  

### Fonte
Textos relacionados a doenças cardiovasculares, sintomas e tratamentos foram obtidos de fontes acadêmicas e literatura clássica (SciELO, BVS, Projeto Gutenberg).

### Possibilidades de Exploração com NLP
Os textos podem ser utilizados em diferentes aplicações:
- Análise de Sentimentos: identificar percepções positivas, negativas ou neutras em narrativas sobre prevenção e tratamento cardiovascular.
- Extração de Sintomas: localizar automaticamente menções a sintomas ou condições clínicas relevantes para suporte ao diagnóstico.
- Classificação de Tópicos: organizar os documentos em categorias como “prevenção”, “tratamento”, “educação em saúde” e “risco cardiovascular”.
- Resumo Automático: gerar resumos curtos de artigos e relatórios para facilitar o acesso rápido a informações importantes.

### Relevância para a Saúde
Explorar textos médicos e científicos com NLP é fundamental porque:
- Permite mineração de conhecimento em larga escala, aproveitando documentos que seriam inviáveis de analisar manualmente.
- Contribui para sistemas de apoio à decisão clínica, fornecendo insights adicionais a partir de literatura e registros de pacientes.
- Facilita educação em saúde, ao estruturar informações de forma clara para profissionais e pacientes.

### Uso em IA
- Análise de sentimentos (ex.: percepção de pacientes sobre sintomas).  
- Extração de sintomas e termos médicos para NLP.  
- Classificação de tópicos e identificação de padrões clínicos.  

### Link
- [Análise do Conceito de Risco Cardiovascular.txt](docs/texts/Análise_do_Conceito_de_Risco_Cardiovascular.txt)
- [Importância da Educação Para Prevenção Cardiovascular.txt](docs/texts/Importância_da_Educação_Para_Prevenção_Cardiovascular.txt)

---

## Parte 3 – Dados Visuais (VC) – Raio-X de Tórax

### Fonte das Imagens
Para esta fase do projeto, utilizamos o **Heart Dataset** disponibilizado no [Mendeley Data](https://data.mendeley.com/datasets/czmn5ypdz5/1?utm_source=chatgpt.com), contendo exames de raio-X de tórax de pacientes. As imagens originais estão em formato `.nii.gz` (formato médico NIfTI) e foram convertidas para `.png` para facilitar o uso em análise de Visão Computacional.

### Processamento e Conversão
- Cada arquivo `.nii.gz` representa um exame volumétrico.
- Extraímos a **fatia central** de cada volume para gerar imagens 2D em escala de cinza.
- Para fins do projeto, selecionamos **100 imagens** representativas do conjunto convertido, garantindo diversidade entre exames normais e patológicos.
- Renomeadas sequencialmente de `xray_001.png` até `xray_100.png`.

### Relevância para a Saúde
A análise de exames de imagem por meio de algoritmos de Visão Computacional é fundamental porque:
- Oferece **apoio ao diagnóstico precoce**, aumentando a precisão e reduzindo erros humanos.
- Auxilia médicos no **monitoramento da evolução clínica** de pacientes.
- Contribui para a **agilidade no atendimento**, especialmente em ambientes de alta demanda hospitalar.
- Permite a construção de **sistemas de triagem automatizados**, ampliando o alcance da medicina preventiva.

### Justificativa para Análise e Possibilidades de Exploração com Visão Computacional
As imagens podem ser utilizadas em diferentes aplicações de Visão Computacional, como:
- **Detecção de anomalias e padrões**: identificar alterações estruturais no coração e tórax.
- **Classificação visual**: separar exames normais de patológicos.
- **Treinamento de modelos de Visão Computacional**: segmentação, reconhecimento de bordas e padrões cardíacos.
- **Identificação de Bordas e Segmentação**: separar regiões de interesse, como área cardíaca e vasos sanguíneos.
- **Reconhecimento de Anomalias**: localizar possíveis sinais de doenças como cardiomegalia ou insuficiência cardíaca.
- **Classificação Automática**: treinar modelos de IA para distinguir entre exames normais e exames com indícios de patologias.

### Link Público
As 100 imagens selecionadas estão hospedadas no OneDrive para acesso público:  
[Link para as imagens](https://1drv.ms/f/c/4140def327662c57/Eo1w_440ba9Ji5yxbjA3OaMBcHYAXzinhSodTjx_KdMNvg?e=zqdb3A)

---

## Observações Finais
Esta fase do projeto tem como objetivo **construir a base de dados para o CardioIA**, garantindo relevância clínica e diversidade nos dados.  
Os datasets foram preparados considerando princípios de **Governança de Dados**, permitindo uso futuro em algoritmos de IA com consistência e qualidade.

## Organização do Repositório

```
cardioia-fase1/
├─ README.md
├─ data/
│ ├─ cardioIA_fase1_dados_numericos.csv
│ ├─ cardioIA_fase1_dicionario_dados.csv
│ └─ data_dictionary.md
├─ docs/
│ ├─ texts/
│ │ ├─ Análise_do_Conceito_de_Risco_Cardiovascular.txt
│ │ └─ Importância_da_Educação_Para_Prevenção_Cardiovascular.txt
├─ scripts/
│ ├─ generate_numeric_dataset.py
│ └─ validate_dataset.py
└─ assets/
│ └─ logo-fiap (1).png
```
---


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>docs</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).



## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


