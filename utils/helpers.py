import logging


def log_user_action(user_id, action):
    logging.info(f"User {user_id} performed action: {action}")
