from aiogram import Router

from .gpt_chat import user_gpt_chat_router
from .start import user_start_router
from .context import user_context_router
from .referral import user_referral_router
from .cancel import user_cancel_router
from .profile import user_profile_router
from .gpt_image import user_gpt_image_router
from .promo_code import user_promo_code_router

from bot.middlewares import DatabaseMiddleware, UserMiddleware

user_router = Router(name="User")

user_router.message.middleware(DatabaseMiddleware())
user_router.message.middleware(UserMiddleware())

user_router.callback_query.middleware(DatabaseMiddleware())
user_router.callback_query.middleware(UserMiddleware())

user_router.include_routers(user_start_router, user_context_router, user_cancel_router, user_referral_router,
                            user_profile_router, user_gpt_image_router, user_promo_code_router, user_gpt_chat_router)