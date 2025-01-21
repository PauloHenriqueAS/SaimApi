# SAIM - API

<p align="center">
<img src="https://img.shields.io/badge/STATUS-EM DESENVOLVIMENTO-green"/>
</p>


## ⚙️ Tecnologias Utilizadas

<div align="center">
    <div style="display: inline_block"><br>
        <img align="center" alt="FastAPI" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original.svg">
        <img align="center" alt="Postgres" height="30" width="40"  src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg">
        <img align="center" alt="OpenCV" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/opencv/opencv-original.svg">
         <img align="center" alt="SqlAlchemy" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original.svg">
          <img align="center" alt="Swagger" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/swagger/swagger-original.svg">
    </div>
</div>

## 🗒️ Descrição do Portal 

1. CRUD de Usuários.
   1. Gerenciamento de usuários com operações de criação, leitura, atualização e exclusão, incluindo autenticação segura 
2. HealthCheck da API.
   1. Endpoint para monitoramento da integridade da API e seus serviços críticos, garantindo a disponibilidade do sistema
3. CRUD de Informações de Pessoa.
   1. Gestão de dados pessoais, permitindo operações de CRUD com validação de informações e busca avançada.
4. CRUD de Imagens.
   1. Gerenciamento de imagens com suporte a upload, atualização, listagem e exclusão, otimizando armazenamento e formato.
5. Métodos de Processamento de Imagem.
   1. Funcionalidades para redimensionamento, filtros, e reconhecimento de padrões em imagens.
6. Métodos de Dashboard.
   1. Visualização de dados em dashboards com gráficos dinâmicos e relatórios em tempo real.

## ⚠️ Comandos Importantes
- Antes de executar o projeto é necessário realizar o download de todas as bibliotecas utilizadas, para isso basta executar o comando
  ```
   pip install requirements.txt
  ```

- Executar a API usando Uvicorn:
- Para iniciar a API localmente com Uvicorn, utilize o seguinte comando no terminal:
- Isso ativará o modo de recarregamento automático, ideal para desenvolvimento, onde a aplicação será recarregada sempre que houver mudanças no código.
```
    uvicorn main:app --reload
```

  
- Acessar a documentação Swagger:
- A documentação interativa da API estará disponível automaticamente via Swagger. Para acessá-la, basta adicionar /docs ao final da URL padrão do Uvicorn:
```
    http://127.0.0.1:8000/docs
```

- Execução da API em modo de depuração no [Visual Studio Code](https://code.visualstudio.com/)
- Para rodar a API em modo de depuração (debug) no Visual Studio Code, utilize o seguinte comando no terminal do VSCode. Esse comando conecta o debugger ao Uvicorn, facilitando o rastreamento de erros durante o desenvolvimento:
  
```
 c:; cd 'c:\Users\Paulo H\Desktop\TCC2024\SaimApi'; & 'c:\Python311\python.exe' 'c:\Users\Paulo H\.vscode\extensions\ms-python.debugpy-2024.10.0-win32-x64\bundled\libs\debugpy\adapter/../..\debugpy\launcher' '58635' '--' '-m' 'uvicorn' 'main:app' '--reload' 
```

<div align="center">
    <h1> 🏗️ Padrões de Commits </h1>

| Tag | Descrição |
| --- | --- |
| FIX | Correções de bug localizados sendo  Hotfix ou Bugfix |
| FEAT | Inicio de implementação de funcionalidade/task |
| CHORE | Desenvolvimento de funcionalidade/task  |
| DONE | Finalização do desenvolvimento de funcionalidade/task |
| REFACTOR | Refatoração do código ou formatação |
| MERGE | Realização de merge e correções de conflitos do mesmo  |
| TEST | Implementação/Execução de testes |
| BUILD | Correções/ajustes/criação de build ou projeto base |
| RELEASE | Liberação de fontes |
| SYNC | Sincronização de modificações liberadas |

</div>

<hr>