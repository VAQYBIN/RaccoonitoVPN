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