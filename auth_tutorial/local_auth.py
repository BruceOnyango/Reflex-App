"""Main app module to demo local authentication."""
import reflex as rx

from .base_state import State
from .login import require_login
from .registration import registration_page as registration_page


def index() -> rx.Component:
    """Render the index page.

    Returns:
        A reflex component.
    """
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Welcome to my homepage!", font_size="2em"),
            rx.link("Protected Page", href="/protected"),
            spacing="1.5em",
            padding_top="10%",
        ),
    )


@require_login
def protected() -> rx.Component:
    """Render a protected page.

    The `require_login` decorator will redirect to the login page if the user is
    not authenticated.

    Returns:
        A reflex component.
    """
    return rx.vstack(
        rx.heading(
            "Protected Page for ", State.authenticated_user.username, font_size="2em"
        ),
        rx.link("Home", href="/"),
        rx.link("Logout", href="/", on_click=State.do_logout),
    )


app = rx.App()
app.add_page(index)
app.add_page(protected)
