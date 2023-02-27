"""Test panel app."""
import panel as pn
from dotenv import load_dotenv
from pyprojroot import here

load_dotenv()

pn.extension()


def user_is_authorized(user_info: dict):
    """Check if the user is authorized to access the app.


    :param user_info: The user information.
    :returns: True if the user is authorized, False otherwise.
    """
    with open(here() / "apps/users.txt") as f:
        valid_users = [line.strip("\n") for line in f.readlines()]

    if user_info is not None:
        print(user_info["login"] in valid_users)
        return user_info["login"] in valid_users
    else:
        print("Authentication not working... allowing pass-through.")
        return True


pn.config.authorize_callback = user_is_authorized


pn.Column(pn.pane.Markdown("# Header!")).servable()
