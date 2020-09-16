import aiohttp
import asyncio
import aiojobs
import motor.motor_asyncio
from pymongo import InsertOne, DeleteOne, ReplaceOne


async def do_upsert_bulk(data):
    requests = []

    for item in data:
        requests.append(ReplaceOne({'id':item['id']}, {'id':item['id'], 'name': item['name'] }, upsert=True))

    result = await db.test_collection.bulk_write(requests)

    return result.modified_count


async def fetch(session, url):
    async with session.get(url, params={"key1":"value","key2":"value"}) as response:
        return await response.json()


async def task(i):
    async with aiohttp.ClientSession(headers={ 'X-Auth-Token': "hoge" }) as session:
        json = await fetch(session, 'http://localhost:7001/api/user')
        return await do_upsert_bulk(json['results'])


async def main():
    while True:
        scheduler = await aiojobs.create_scheduler()
        response_buffer = []
        for i in range(100):
            # spawn jobs
            response = await scheduler.spawn(task(i))
            response_buffer.append(response)

        await asyncio.sleep(2.0)
        # close all jobs exists more than 5.0sec

        # gracefully close spawned jobs
        await scheduler.close()

        print(f'# of response: {len(response_buffer)}/100')


client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
db = client.test_database
collection = db.test_collection
asyncio.get_event_loop().run_until_complete(main())
