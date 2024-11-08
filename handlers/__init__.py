from .start import start_router
from .menu import menu_router
from handlers.answers_menu.general_training.general_training import general_training_router
from .info import info_router


routers = [start_router, menu_router, info_router, general_training_router]
