**This [template](https://github.com/Sokhatskyi/telegram-bot-template) is used to develop [Telegram bots](https://core.telegram.org/bots/api) using the [`aiogram v3.0+`](https://github.com/aiogram/aiogram/tree/dev-3.x) library.**

### To start using:

1. Copy `.env.dist` to `.env` and fill in the required data.
2. **Docker:**
   1. If you don't have Docker installed, you need to [download and install it](https://docs.docker.com/get-docker/).
   2. Run the project with the `docker-compose up` command.
3. **Without Docker:**
   1. Create and activate [venv](https://docs.python.org/3/library/venv.html).
   2. Update python pip `pip install --upgrade pip setuptools`.
   3. Install dependencies from requirements.txt: `pip install -r requirements.txt`.
   4. Run the project with the `python3 bot.py` command.

### How to make and register handlers:

1. Create the `you_name.py` module in the `handlers` folder.
2. Create a router in `you_name.py`.

```python
from aiogram import Router

user_router = Router()
```

You can make several [routers](https://docs.aiogram.dev/en/dev-3.x/dispatcher/router.html) in one module, and hang handlers on each of them.
You can register handlers as decorators:

```python
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply('Greetings, regular user!')
```

Go to the `handlers/__init__.py` file and add all the routers to it:

```python
from .user import user_router
from .admin import admin_router
from .echo import echo_router

routers_list = [
    user_router,
    admin_router,
    echo_router,
    ...  # Your other routers
]

__all__ = [
    'routers_list'
]
```
