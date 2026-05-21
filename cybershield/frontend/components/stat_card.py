import reflex as rx


def stat_card(
    title: str,
    value: str,
    color: str,
):

    return rx.box(

        rx.vstack(

            # TITLE
            rx.text(
                title,
                size="4",
                color="#9ca3af",
            ),

            # VALUE
            rx.heading(
                value,
                size="8",
                color=color,
                weight="bold",
            ),

            spacing="3",

            align="start",
        ),

        padding="2em",

        width="250px",

        border_radius="20px",

        background="#111827",

        border=f"1px solid {color}",

        transition="all 0.3s ease",

        _hover={
            "transform": "translateY(-6px)",
            "box_shadow": f"0 0 25px {color}",
        },
    )