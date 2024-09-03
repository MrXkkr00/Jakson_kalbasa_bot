import asyncio

from utils.db_api.tavar_sql import Database_Tavar


async def test():
    db = Database_Tavar()
    await db.create()
    await db.create_table_tavar()

    # users = await db.select_all_Tavarlar()
    # print(users)
    # await db.add_Tavar(user_id="23131", t_turi="330", t_soni="2", t_nomer="4", t_narxi="40000")
    # await db.add_Tavar(user_id="23131", t_turi="800", t_soni="2", t_nomer="4", t_narxi="80000")
    # users = await db.select_all_Tavarlar()
    user1 = await db.select_Tavar(user_id="7010118152")
    print(user1)
    await db.delete_Tavar(user_id="7010118152")
    user1 = await db.select_Tavar(user_id="7010118152")
    print(user1)

    # await db.delete_Tavar(user_id="23131")
    # users = await db.select_all_Tavarlar()
    # print(users)


asyncio.run(test())

#
# soat = "10-11"
# print(soat[:2])
# print(soat[2])
# print(soat[3:5])
