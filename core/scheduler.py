import asyncio
import logging

from sqlalchemy import text

from db.session import AsyncSessionLocal

logger = logging.getLogger(__name__)

KEEP_ALIVE_INTERVAL = 600  # 10 minutes


async def _keep_alive_loop() -> None:
    while True:
        await asyncio.sleep(KEEP_ALIVE_INTERVAL)
        try:
            async with AsyncSessionLocal() as session:
                await session.execute(text("SELECT 1"))
            logger.info("DB keep-alive ping sent")
        except Exception as e:
            logger.warning("DB keep-alive failed: %s", e)


_task: asyncio.Task | None = None


def start() -> None:
    global _task
    _task = asyncio.create_task(_keep_alive_loop())
    logger.info("DB keep-alive scheduler started (interval: %ds)", KEEP_ALIVE_INTERVAL)


def stop() -> None:
    if _task and not _task.done():
        _task.cancel()