import reflex as rx


class LoginState(rx.State):

    selected_role: str = ""

    def set_role(
        self,
        role: str,
    ):

        self.selected_role = role

        if role == "user":

            return rx.redirect(
                "/dashboard"
            )

        return rx.redirect(
            "/expert-dashboard"
        )


def role_card(
    title: str,
    description: str,
    color: str,
    role: str,
):

    return rx.box(

        rx.vstack(

            rx.heading(
                title,
                size="7",
                color=color,
            ),

            rx.text(
                description,
                color="#d1d5db",
                text_align="center",
            ),

            rx.button(

                f"Continue as {title}",

                size="4",

                color_scheme="cyan",

                radius="large",

                width="100%",

                on_click=lambda:
                LoginState.set_role(
                    role
                ),
            ),

            spacing="5",

            align="center",
        ),

        padding="3em",

        width="350px",

        border_radius="25px",

        background="#111827",

        border=f"1px solid {color}",

        transition="all 0.3s ease",

        _hover={
            "transform":
            "translateY(-10px)",

            "box_shadow":
            f"0 0 35px {color}",
        },
    )


def login_page():

    return rx.box(

        rx.center(

            rx.vstack(

                rx.heading(
                    "CyberShield Access Portal",
                    size="9",

                    background="""
                    linear-gradient(
                    90deg,
                    cyan,
                    purple
                    )
                    """,

                    background_clip="text",

                    color="transparent",
                ),

                rx.text(
                    "Choose your access role",
                    size="5",
                    color="#9ca3af",
                ),

                spacing="3",
            ),
        ),

        rx.center(

            rx.hstack(

                role_card(
                    "User",
                    "Solve cyber awareness quizzes and earn NFT rewards.",
                    "cyan",
                    "user",
                ),

                role_card(
                    "Cyber Expert",
                    "Create and manage awareness quizzes for users.",
                    "purple",
                    "expert",
                ),

                spacing="8",

                margin_top="5em",

                wrap="wrap",

                justify="center",
            ),
        ),

        background="""
        radial-gradient(circle at top,
        #111827,
        #030712)
        """,

        min_height="100vh",

        padding="3em",
    )