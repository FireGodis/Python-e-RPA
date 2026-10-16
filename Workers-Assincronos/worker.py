import asyncio

async def process(job: str) -> None:
    await asyncio.sleep(0)
    print(f"Processado: {job}")

async def worker(queue: asyncio.Queue[str]) -> None:
    while True:
        job = await queue.get()
        try:
            if job == "STOP":
                return
            await process(job)
        finally:
            queue.task_done()

async def main() -> None:
    queue: asyncio.Queue[str] = asyncio.Queue()
    task = asyncio.create_task(worker(queue))
    for job in ("pedido-001", "pedido-002"):
        await queue.put(job)
    await queue.join()
    await queue.put("STOP")
    await task

if __name__ == "__main__":
    asyncio.run(main())
