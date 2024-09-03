from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from numpy import double
from sqlalchemy import BIGINT

from data import config


class Database_Tavar:

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

    async def create_table_tavar(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Tavarlar (
            id SERIAL PRIMARY KEY,
            user_id varchar(255),
            t_turi varchar(255),
            t_nomer varchar(255),
            t_soni varchar(255),
            t_narxi varchar(255)
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

    async def add_Tavar(self, user_id: str = None, t_turi: str = None, t_nomer: str = None,
                       t_soni: str = None, t_narxi: str = None):
        # SQL_EXAMPLE = "INSERT INTO Tavarlar(id, t_nomer, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Tavarlar(user_id, t_turi, t_nomer,  t_soni, t_narxi) 
        VALUES($1, $2, $3, $4, $5) returning *
        """
        return await self.execute(sql, user_id, t_turi, t_nomer, t_soni, t_narxi, fetchrow=True)





    async def select_all_Tavarlar(self):
        sql = """
        SELECT * FROM Tavarlar
        """
        return await self.execute(sql, fetch=True)

    async def select_Tavar(self, **kwargs):
        sql = "SELECT * FROM Tavarlar WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetch=True)

    async def count_Tavarlar(self):
        return await self.execute("SELECT COUNT(*) FROM Tavarlar", fetchval=True)

    async def drop_Tavarlar(self):
        await self.execute("DROP TABLE Tavarlar", execute=True)

    async def delete_Tavar(self, user_id: str):
        sql = """
        DELETE FROM Tavarlar WHERE user_id = $1 returning *
        """
        return await self.execute(sql, user_id, fetch=True)
