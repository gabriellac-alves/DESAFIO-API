from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context
from src.config import settings
from src.database import metadata
from src.models.transaction import transactions  # noqa
from src.models.account import accounts  # noqa

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = metadata

def run_migrations_offline() -> None:
    url = settings.database_url.replace("+aiosqlite", "")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    sync_url = settings.database_url.replace("+aiosqlite", "")
    connectable = create_engine(sync_url)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()