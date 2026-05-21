import reflex as rx


# ---------------------------------
# LEADERBOARD DATA
# ---------------------------------

leaderboard_data = [

    {
        "name": "Omkar",
        "role": "Cyber Expert",
        "score": 980,
    },

    {
        "name": "Alex",
        "role": "Ethical Hacker",
        "score": 870,
    },

    {
        "name": "Sophia",
        "role": "Security Analyst",
        "score": 820,
    },

    {
        "name": "Rahul",
        "role": "Cyber Defender",
        "score": 760,
    },
]


# ---------------------------------
# LEADERBOARD CARD
# ---------------------------------

def leaderboard_card(user: dict):

    return rx.box(

        rx.hstack(

            rx.vstack(

                rx.heading(
                    user["name"],
                    size="6",
                    color="cyan",
                ),

                rx.text(
                    user["role"],
                    color="#9ca3af",
                ),

                align="start",

                spacing="1",
            ),

            rx.spacer(),

            rx.vstack(

                rx.heading(
                    f'{user["score"]}',
                    size="7",
                    color="purple",
                ),

                rx.text(
                    "Awareness Points",
                    color="#d1d5db",
                    size="2",
                ),

                align="end",

                spacing="1",
            ),

            width="100%",
        ),

        width="800px",

        padding="1.5em",

        border_radius="20px",

        background="#111827",

        border="1px solid cyan",

        transition="all 0.3s ease",

        _hover={

            "transform":
            "translateY(-5px)",

            "box_shadow":
            "0 0 20px cyan",
        },
    )


# ---------------------------------
# LEADERBOARD PAGE
# ---------------------------------

def leaderboard_page():

    return rx.box(

        rx.center(

            rx.vstack(

                rx.heading(

                    "Cyber Awareness Leaderboard",

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

                    "Top users ranked by awareness score",

                    size="5",

                    color="#9ca3af",
                ),

                spacing="3",
            ),

            padding_top="2em",
        ),

        rx.center(

            rx.vstack(

                *[
                    leaderboard_card(user)
                    for user in leaderboard_data
                ],

                spacing="5",

                margin_top="4em",
            )
        ),

        background="""
        radial-gradient(circle at top,
        #111827,
        #030712)
        """,

        min_height="100vh",

        padding="3em",
    )