from .general_training import general_training, general_training_router
from .fire_preparation import fire_preparation_router, fire_preparation
from .functional_training import functional_training_router, functional_training
from .tactical_training import tactical_training_router, tactical_training
from .additional_question import additional_question_router

__all__ = ['general_training', 'general_training_router',
           'fire_preparation_router', 'fire_preparation',
           'functional_training_router', 'functional_training',
           'tactical_training_router', 'tactical_training',
           'additional_question_router',
           ]
