import reflex as rx


# -----------------------------
# STAT CARD
# -----------------------------

def stat_card(title, value, color):

    return rx.box(

        rx.vstack(

            rx.text(
                title,
                color="#9ca3af",
                size="4",
            ),

            rx.heading(
                value,
                size="8",
                color=color,
            ),

            spacing="2",
        ),

        padding="2em",

        width="260px",

        border_radius="20px",

        background="#111827",

        border=f"1px solid {color}",

        transition="all 0.3s ease",

        _hover={
            "transform": "translateY(-8px)",
            "box_shadow": f"0 0 25px {color}",
        },
    )


# -----------------------------
# ACTIVITY CARD
# -----------------------------

def activity_card(title, desc, color):

    return rx.box(

        rx.vstack(

            rx.heading(
                title,
                size="5",
                color=color,
            ),

            rx.text(
                desc,
                color="#d1d5db",
            ),

            spacing="3",
        ),

        padding="1.5em",

        border_radius="18px",

        background="#1f2937",

        width="100%",

        transition="all 0.3s ease",

        _hover={
            "transform": "scale(1.02)",
            "border": f"1px solid {color}",
        },
    )


# -----------------------------
# DASHBOARD PAGE
# -----------------------------

def dashboard_page():

    return rx.box(

        # HEADER
        rx.vstack(

            rx.heading(
                "CyberShield Dashboard",
                size="9",

                background="""
                linear-gradient(90deg, cyan, purple)
                """,

                background_clip="text",

                color="transparent",
            ),

            rx.text(
                "Track your cyber awareness progress and NFT rewards.",
                size="5",
                color="#9ca3af",
            ),

            spacing="3",

            margin_bottom="3em",
        ),


        # STATS SECTION
        rx.center(

            rx.hstack(

                stat_card(
                    "Quizzes Completed",
                    "12",
                    "cyan",
                ),

                stat_card(
                    "Awareness Score",
                    "92%",
                    "purple",
                ),

                stat_card(
                    "NFT Certificates",
                    "5",
                    "green",
                ),

                spacing="6",

                wrap="wrap",

                justify="center",
            ),
        ),


        # RECENT ACTIVITIES
        rx.vstack(

            rx.heading(
                "Recent Activities",
                size="7",
                color="white",
            ),

            activity_card(
                "Phishing Simulation Passed",
                "You successfully detected a fake banking email scam.",
                "cyan",
            ),

            activity_card(
                "NFT Reward Claimed",
                "Cyber Awareness Certificate NFT minted successfully.",
                "green",
            ),

            activity_card(
                "Leaderboard Rank Improved",
                "You moved to Top 10 cybersecurity learners.",
                "purple",
            ),

            spacing="5",

            margin_top="4em",
        ),

        # CTA SECTION
        rx.center(

            rx.box(

                rx.vstack(

                    rx.heading(
                        "Ready For The Next Challenge?",
                        size="8",
                        color="cyan",
                    ),

                    rx.text(
                        "Improve your scam detection skills through interactive cyber awareness simulations.",
                        color="#d1d5db",
                        text_align="center",
                    ),

                    rx.button(
                        "Start New Quiz",
                        size="4",
                        color_scheme="cyan",
                        radius="large",
                        on_click=rx.redirect("/quiz"),
                    ),

                    spacing="5",
                    align="center",
                ),

                padding="3em",
                border_radius="25px",
                background="#111827",
                border="1px solid cyan",
                width="80%",
                margin_top="5em",
                transition="all 0.3s ease",
                _hover={
                    "box_shadow": "0 0 35px cyan",
                },
            ),
        ),

        background="""
        radial-gradient(circle at top left, #0f172a, #030712)
        """,

        min_height="100vh",

        padding="2em",

        padding_bottom="5em",
    )