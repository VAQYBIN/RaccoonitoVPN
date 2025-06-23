# RaccoonitoVPN
Telegram bot for selling VPN subscriptions

## Database configuration

Set the `DATABASE_URL` environment variable to your PostgreSQL connection
string.  For example:

```bash
export DATABASE_URL="postgresql+psycopg2://user:password@host:5432/dbname"
```

Alembic migrations also rely on this variable when `db/alembic.ini` uses
`driver://` as the placeholder URL.

## Загрузка конфигураций серверов

Файлы с описанием серверов размещаются в каталоге `servers`. Формат файла
может быть `*.yaml` или `*.json`. Пример содержимого:

```yaml
domain: vpn.example.com
port: 51820
web_path: /wireguard
sub_port: 80
sub_web_path: /subscribe
```

Чтобы добавить сервера в базу данных, запустите:

```bash
python scripts/load_servers.py
```

Перед запуском убедитесь, что переменная `DATABASE_URL` указывает на удалённый
сервер PostgreSQL, например:

```bash
export DATABASE_URL="postgresql+psycopg2://user:password@remote-host:5432/dbname"
```