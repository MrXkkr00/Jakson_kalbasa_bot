from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from numpy import double
from sqlalchemy import BIGINT

from data import config


class Database_User:

    def __init__(self) -> None:
        self.pool: Union[Pool, None] = None

    async def create(self):
        try:
            self.pool = await asyncpg.create_pool(
                user=config.DB_USER,
                password=config.DB_PASS,
                host=config.DB_HOST,
                database=config.DB_NAME
            )
        except Exception as e:
            print(f"Error creating connection pool: {e}")

    async def disconnect(self):

        try:
            if self.pool:
                await self.pool.close()
        except Exception as e:
            print(f"Error closing connection pool: {e}")

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):

        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY,
            user_id varchar(255),
            user_name varchar(255),
            name varchar(255),
            phone_nomer varchar(255),
            date_enter varchar(255)
            );
"""
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, user_id: str = None, user_name: str = None, name: str = None,
                       phone_nomer: str = None, date_enter: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(user_id, user_name, name,  phone_nomer, date_enter) 
        VALUES($1, $2, $3, $4, $5) returning *
        """
        return await self.execute(sql, user_id, user_name, name, phone_nomer, date_enter, fetchrow=True)





    async def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        return await self.execute("SELECT COUNT(*) FROM Users", fetchval=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)
