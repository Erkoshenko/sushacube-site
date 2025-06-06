import asyncio
import aiohttp
from random import randint
from config import TOKEN
from web import start_web

peer_id = 2000000002
message = '''
 [1] Создаю проекты: 
  1. CRMP / SAMP / MTA 
  2. MINECRAFT
  3. CS
      
 [2] Создаю каналы:
  1. DISCORD 
  2. TELEGRAM - ( ПП 1K+ ) 
      
 [3] Создаю сайты:
  1. Сайт для продажи/Покупки
  2. Сайт игры
      
 [4] Создаю ботов:
  1. Вк любые задачи
  2. Тг любые задачи
  3. Вотцап любые задачи
  4. Для игры
    
 [5] °•°•°•°•°:
  1. Расскажу как заливать мод в хостинг
  2. Расскажу как создавать сервер
  3. Расскажу как зайти в игру
  
 [6] Прочие услуги:
  1. Добавление мода в хостинг
  2. Создание клиента/Лаунчера
  3. Исправление ошибок в моде/клиенте/Лаунчере

 [7] Реклама / Пиар:
  [1] Реклама Проекта
  [2] Реклама Группы
  [3] Реклама Бесед
  [4] Реклама Аккаунта

Писать ему: @qazxwyh
'''
N = 300

async def send_message(session):
    params = {
        'access_token': TOKEN,
        'peer_id': peer_id,
        'message': message,
        'random_id': randint(1, 2**31),
        'v': '5.131'
    }
    async with session.post('https://api.vk.com/method/messages.send', params=params) as response:
        result = await response.json()
        print(result)

async def main():
    asyncio.create_task(start_web())
    async with aiohttp.ClientSession() as session:
        while True:
            await send_message(session)
            await asyncio.sleep(N)

if __name__ == "__main__":
    asyncio.run(main())