# 🏨 Guia de Integração com Banco de Dados

## ✅ O que foi implementado

O sistema agora possui **persistência de dados** usando SQLite. Todos os dados são salvos automaticamente no arquivo `hotel.db`.

### Estrutura do Banco de Dados

#### Tabela `clientes`
- `id` - ID único (chave primária, autoincremento)
- `nome` - Nome do cliente
- `telefone` - Telefone do cliente
- `email` - E-mail do cliente

#### Tabela `quartos`
- `id` - ID único (chave primária, autoincremento)
- `numero` - Número do quarto (único)
- `tipo` - Tipo do quarto (ex: simples, duplo, suíte)
- `diaria` - Valor da diária
- `status` - Status do quarto (disponível/ocupado)

#### Tabela `reservas`
- `id` - ID único (chave primária, autoincremento)
- `cliente_id` - ID do cliente (chave estrangeira)
- `quarto_id` - ID do quarto (chave estrangeira)
- `checkin` - Data de check-in
- `checkout` - Data de check-out
- `status` - Status da reserva (ativa/cancelada/concluída)

## 🔄 Como funciona

### Operações automáticas

Todas as operações CRUD agora salvam dados no banco automaticamente:

#### Cadastrar
- **Cliente**: Ao cadastrar, os dados são inseridos na tabela `clientes`
- **Quarto**: Ao cadastrar, os dados são inseridos na tabela `quartos`
- **Reserva**: Ao criar, os dados são inseridos na tabela `reservas`

#### Editar
- **Cliente**: Alterações são atualizadas na tabela `clientes`
- **Quarto**: Alterações são atualizadas na tabela `quartos`
- **Reserva**: Alterações são atualizadas na tabela `reservas`

#### Excluir
- **Cliente**: Remove o registro da tabela `clientes`
- **Quarto**: Remove o registro da tabela `quartos`
- **Reserva**: Remove o registro da tabela `reservas`

## 🧪 Como testar

### 1. Execute o sistema normalmente
```bash
python main.py
```

### 2. Cadastre alguns dados
- Cadastre clientes no menu 1
- Cadastre quartos no menu 2
- Crie reservas no menu 3

### 3. Verifique os dados no banco
```bash
python teste_banco.py
```

Este script exibe todos os dados salvos no banco de dados.

### 4. Consulte o banco diretamente (opcional)
```bash
sqlite3 hotel.db
```

Comandos úteis no SQLite:
```sql
-- Listar todas as tabelas
.tables

-- Ver estrutura de uma tabela
.schema clientes

-- Consultar dados
SELECT * FROM clientes;
SELECT * FROM quartos;
SELECT * FROM reservas;

-- Sair
.quit
```

## 📁 Arquivos modificados

- ✅ `database.py` - Funções CRUD completas para todas as tabelas
- ✅ `hotel.py` - Integração com banco nas operações de clientes e quartos
- ✅ `gerenciador.py` - Integração com banco nas operações de reservas
- ✅ `teste_banco.py` - Script para visualizar dados do banco

## 🎯 Benefícios

1. **Persistência**: Dados não são perdidos ao fechar o sistema
2. **Integridade**: Chaves estrangeiras garantem relacionamentos corretos
3. **Backup**: Arquivo `hotel.db` pode ser copiado/restaurado
4. **Consultas**: Dados podem ser analisados com SQL
5. **Escalabilidade**: Fácil migrar para banco mais robusto (PostgreSQL, MySQL)

## ⚠️ Observações importantes

- O arquivo `hotel.db` é criado automaticamente na primeira execução
- As tabelas são criadas automaticamente se não existirem
- Os dados em memória (listas) e no banco devem estar sincronizados
- Em caso de erro, verifique se o arquivo `hotel.db` tem permissões de escrita

## 🔮 Próximos passos (opcional)

Para melhorar ainda mais o sistema, você pode:

1. **Carregar dados do banco ao iniciar** - Carregar clientes, quartos e reservas existentes
2. **Validações adicionais** - Verificar duplicatas antes de inserir
3. **Histórico de alterações** - Criar tabela de logs
4. **Backup automático** - Criar cópias periódicas do banco
5. **Interface gráfica** - Usar Tkinter ou PyQt para visualizar dados
