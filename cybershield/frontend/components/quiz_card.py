import reflex as rx


def quiz_card(
    title: str,
    description: str,
    difficulty: str,
    color: str,
):

    return rx.box(

        rx.vstack(

            # TITLE
            rx.heading(
                title,
                size="6",
                color=color,
            ),

            # DESCRIPTION
            rx.text(
                description,
                color="#d1d5db",
            ),

            # DIFFICULTY BADGE
            rx.badge(
                difficulty,
                color_scheme="purple",
                size="2",
            ),

            # BUTTON
            rx.button(

                "Start Quiz",

                width="100%",

                color_scheme="cyan",

                radius="large",

                on_click=rx.redirect(
                    "/quiz"
                ),
            ),

            spacing="4",

            align="start",
        ),

        padding="2em",

        width="320px",

        border_radius="20px",

        background="#111827",

        border=f"1px solid {color}",

        transition="all 0.3s ease",

        _hover={
            "transform": "translateY(-8px)",
            "box_shadow": f"0 0 25px {color}",
        },
    )