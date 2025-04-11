# 📘 Documentação do Projeto: **carros**

## 📄 Visão Geral

**Nome do Projeto:** carros  
**Descrição:** Aplicação web para cadastro e venda de automóveis. Usuários registrados podem cadastrar veículos com informações completas, incluindo imagens.  
**Objetivo:** Facilitar o gerenciamento de vendas de veículos entre usuários registrados.  
**Tecnologia Base:** Django (Python)  
**IDE Utilizada:** Visual Studio Code (VSCode)  
**Banco de Dados:** Postgresql

---

## 🛠️ Tecnologias Utilizadas

- **Framework Backend:** Django
- **ORM:** Django ORM
- **Autenticação:** Sistema de usuários do Django + superusuário
- **Frontend:** Templates Django
- **Ambiente:** Desenvolvimento local com VSCode

---

## 🧱 Modelagem de Dados

### 📦 Modelo de Veículo (`Car`)
- **modelo** (char)
- **marca** (char)
- **ano_fabricacao** (int)
- **ano_modelo** (int)
- **placa** (char, única)
- **valor** (decimal)
- **imagem** (upload de imagem)

### 👤 Usuário
- Utiliza o sistema de autenticação padrão do Django.
- Cada veículo é associado a um usuário.

---

## 🔗 Rotas da Aplicação

| Rota | Método | Descrição |
|------|--------|-----------|
| `/cars` | GET | Lista todos os carros cadastrados |
| `/car/<int:pk>/` | GET | Visualiza detalhes de um veículo específico |
| `/car/<int:pk>/update` | POST/GET | Atualiza dados de um veículo |
| `/car/<int:pk>/delete` | POST/GET | Deleta um veículo |
| `/new_car` | POST/GET | Formulário para cadastrar um novo carro |
| `/register` | POST/GET | Registro de novo usuário |
| `/login` | POST/GET | Login do usuário |
| `/logout` | GET | Logout do usuário |
| `/admin` | GET | Área administrativa do Django (superusuário) |

---

## 🔐 Acesso e Autenticação

- **Login e Registro:** Feitos via rotas `/login` e `/register`
- **Área administrativa:** Acessível apenas por superusuário via `/admin`
- **Permissões:** Apenas o dono do carro ou o superusuário pode editar/deletar informações referentes ao veículo

---

## 🚀 Instruções de Execução

1. **Clone o repositório**  
   ```bash
   git clone https://github.com/marcellacg/carros.git
   cd carros
   ```

2. **Crie o ambiente virtual**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   ```

3. **Instale as dependências**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Rode as migrações**  
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário (admin)**  
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento**  
   ```bash
   python manage.py runserver
   ```

---

## 🧪 Testes

> Por enquanto, o projeto não possui uma suíte de testes automatizados. Sugere-se o uso do `pytest` ou `unittest` para futuros testes.

---

## 👥 Desenvolvedores

- Projeto desenvolvido por Marcella Costa
- IDE utilizada: **Visual Studio Code**
