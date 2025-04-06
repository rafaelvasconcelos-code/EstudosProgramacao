import asyncio

async def print_sum(a,b):
    print(a+b)

async def sum(a,b):
    await print_sum(a,b)
    return a+b

resultado = sum(2,3)


#Event Loop -> Quem orquestra as tarefas

event_loop = asyncio.new_event_loop()
result = event_loop.run_until_complete(resultado)