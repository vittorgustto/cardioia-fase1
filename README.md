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
Este repositório reúne **dados numéricos, textuais e visuais** que serão usados nas próximas fases do projeto **CardioIA** (triagem, diagnóstico, monitoramento e previsão). O foco é garantir **qualidade**, **governança** e **relevância clínica** desde o início.


## 2) Estrutura dos Dados
- **Numéricos (IoT/Clínicos simulados)**: `data/cardio_numeric_dataset.csv` e `.xlsx`
- **Cópia pública**: [link público Drive/OneDrive]
- **Dicionário de dados**: `data/data_dictionary.md`
- **Origem**: dados **simulados** por script com distribuição realista e correlações clínicas plausíveis.
- **Variáveis-chave (exemplos)**: idade, sexo, PA sistólica/diastólica, colesterol total, glicemia jejum, FC, IMC, tabagismo, histórico familiar, tipo de dor torácica, ECG de repouso, angina induzida por exercício, ST (oldpeak), inclinação do segmento ST, alvo (prob. doença cardíaca), etc.
- **Justificativa clínica**: variáveis amplamente associadas a **risco cardiovascular** e **estratificação clínica**; úteis para modelos de IA (classificação/regressão, explicabilidade, score de risco).


- **Textuais (NLP)**: `docs/texts/`
- **Arquivos**: pelo menos 2 `.txt` (ex.: material sobre doenças cardíacas, sintomas, diretrizes de saúde pública, trechos literários pertinentes).
- **Cópia pública**: [link público Drive/OneDrive]
- **Como explorar (NLP)**: análise de tópicos, extração de sintomas, normalização terminológica, sumarização, detecção de vieses linguísticos (ex.: cobertura desigual entre populações).


- **Visuais (VC)**: **hospedadas externamente** (Drive/OneDrive) – **≥ 100 imagens do mesmo tipo** (ex.: ECGs)
- **Link público**: [link público Drive/OneDrive]
- **Como explorar (VC)**: detecção de padrões, anomalias, segmentação/realce de bordas, classificação supervisionada, autoencoders para detecção de outliers.


## 3) Governança de Dados, Viés e Ética
- **Origem e licenças**: declarar claramente as fontes. Usar somente dados com **licenças permissivas** (ou gerados por nós).
- **Privacidade**: nenhum dado pessoal identificável; dados numéricos são **sintéticos**.
- **Viés**: monitorar distribuição (idade, sexo etc.), evitar representações desbalanceadas que prejudiquem performance/justiça de modelos.
- **Rastreabilidade**: scripts versionados em `scripts/`; outputs versionados em `data/`.


## 4) Reprodutibilidade
- Python 3.10+
- Gerar dataset: `python scripts/generate_numeric_dataset.py`
- Validar dataset: `python scripts/validate_dataset.py`


## 5) Contato
- Equipe: [Nomes]
- Responsáveis: [Você / Colega]



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


