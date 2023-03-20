import time
import asyncio
from main_exec import execution
import datetime as dt

# function for normal output. it checks the websites every 10 minutes
async def main(times):
	counter = 1
	while True:
		print(f'Check #{counter} at {str(dt.datetime.now())}')
		print('\n'.join(['=' * 80 for _ in range(3)]))
		print()
		execution()
		print()
		print('\n'.join(['=' * 80 for _ in range(3)]))		
		await asyncio.sleep(times)

# asynch process
async def runner():
    data1 = []
    data1.append(asyncio.create_task(main(600)))
    await asyncio.gather(*data1)

# executing the func
if __name__ == '__main__':
	asyncio.run(runner())