import asyncio
import logging
from typing import Union, Optional

from aiogram import Bot, exceptions
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply


async def send_message(
        bot: Bot,
        chat_id: Union[int, str],
        text: str,
        disable_notification: Optional[bool] = False,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
) -> bool:
    """
    Safe messages sender.
    :return: success.
    """
    try:
        await bot.send_message(
            chat_id=chat_id,
            text=text,
            disable_notification=disable_notification,
            reply_markup=reply_markup
        )
    except exceptions.TelegramForbiddenError:
        logging.error(f'Target [ID:{chat_id}]: got TelegramForbiddenError')

    except exceptions.TelegramRetryAfter as e:
        logging.error(f'Target [ID:{chat_id}]: Flood limit is exceeded. Sleep {e.retry_after} seconds.')
        await asyncio.sleep(e.retry_after)
        return await send_message(
            bot=bot, chat_id=chat_id, text=text, disable_notification=disable_notification, reply_markup=reply_markup
        )  # Recursive call

    except exceptions.TelegramAPIError:
        logging.exception(f'Target [ID:{chat_id}]: failed')
    else:
        logging.info(f'Target [ID:{chat_id}]: success')
        return True

    return False


async def broadcast(
        bot: Bot,
        users: list[Union[int, str]],
        text: str,
        delay: float = 0.05,
        disable_notification: Optional[bool] = False,
        reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None
) -> int:
    """
    Simple broadcaster.
    :return: Count of messages.
    """
    count = 0
    try:
        for user_id in users:
            if await send_message(
                    bot=bot,
                    chat_id=user_id,
                    text=text,
                    disable_notification=disable_notification,
                    reply_markup=reply_markup
            ):
                count += 1

            await asyncio.sleep(delay)  # Default 20 messages per second (Limit: 30 messages per second)
    finally:
        logging.info(f'{count} messages successful sent.')

    return count
