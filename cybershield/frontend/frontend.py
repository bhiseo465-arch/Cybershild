import reflex as rx

from .pages.dashboard import dashboard_page
from .pages.quiz import quiz_page
from .pages.leaderboard import leaderboard_page
from .pages.nft_gallery import nft_gallery_page
from .pages.expert_dashboard import expert_dashboard_page


# -----------------------------
# LANDING STATE
# -----------------------------

class LandingState(rx.State):

    show_login_modal: bool = False

    def open_modal(self):
        self.show_login_modal = True

    def close_modal(self):
        self.show_login_modal = False


# -----------------------------
# APP THEME
# -----------------------------

app = rx.App(

    theme=rx.theme(

        appearance="dark",

        has_background=True,

        radius="large",

        accent_color="cyan",
    )
)


# -----------------------------
# NAVBAR
# -----------------------------

def navbar():

    return rx.hstack(

        rx.heading(
            "CyberShield",
            size="8",
            color="cyan",
            weight="bold",
        ),

        rx.spacer(),

        rx.hstack(

            rx.link(
                "Dashboard",
                href="/",
                color="white",
                weight="medium",
            ),

            rx.link(
                "Quiz",
                href="/quiz",
                color="white",
                weight="medium",
            ),

            rx.link(
                "Leaderboard",
                href="/leaderboard",
                color="white",
                weight="medium",
            ),

            rx.link(
                "NFT Gallery",
                href="/nft-gallery",
                color="white",
                weight="medium",
            ),

            spacing="6",
        ),

        width="100%",

        padding="1.5em",

        position="sticky",

        top="0",

        z_index="100",

        backdrop_filter="blur(10px)",

        background="rgba(3,7,18,0.8)",

        border_bottom="1px solid #1f2937",
    )


# -----------------------------
# HERO SECTION
# -----------------------------

def hero_section():

    return rx.center(

        rx.vstack(

            rx.heading(
                "Cyber Awareness Through Gamification",
                size="9",
                text_align="center",

                background="linear-gradient(90deg, cyan, purple)",

                background_clip="text",

                color="transparent",
            ),

            rx.text(
                "Solve cyber awareness quizzes, detect phishing scams, and earn simulated NFT rewards powered by UGF concepts.",

                size="5",

                color="#9ca3af",

                text_align="center",

                max_width="900px",
            ),

            rx.hstack(

                rx.button(

                    "Get Started",

                    size="4",

                    color_scheme="cyan",

                    radius="large",

                    on_click=LandingState.open_modal,
                ),

                rx.button(

                    "Leaderboard",

                    size="4",

                    variant="outline",

                    color_scheme="purple",

                    radius="large",

                    on_click=rx.redirect("/leaderboard"),
                ),

                spacing="4",
            ),

            spacing="7",

            align="center",
        ),

        min_height="90vh",

        padding="2em",
    )


# -----------------------------
# FEATURE CARD
# -----------------------------

def feature_card(
    title,
    description,
    color,
):

    return rx.box(

        rx.vstack(

            rx.heading(
                title,
                size="6",
                color=color,
            ),

            rx.text(
                description,
                color="#d1d5db",
            ),

            spacing="4",
        ),

        padding="2em",

        border_radius="20px",

        background="#111827",

        border=f"1px solid {color}",

        width="320px",

        transition="all 0.3s ease",

        _hover={
            "transform": "translateY(-10px)",
            "box_shadow": f"0 0 30px {color}",
        },
    )


# -----------------------------
# LOGIN MODAL
# -----------------------------

def login_modal():

    return rx.cond(

        LandingState.show_login_modal,

        rx.center(

            rx.box(

                rx.vstack(

                    rx.heading(
                        "Choose Your Role",
                        size="7",
                        color="cyan",
                    ),

                    rx.text(
                        "Select how you want to continue",
                        color="#d1d5db",
                    ),

                    rx.button(

                        "Continue as User",

                        width="100%",

                        color_scheme="cyan",

                        radius="large",

                        on_click=[
                            LandingState.close_modal,
                            rx.redirect("/dashboard"),
                        ],
                    ),

                    rx.button(

                        "Continue as Cyber Expert",

                        width="100%",

                        color_scheme="purple",

                        radius="large",

                        on_click=[
                            LandingState.close_modal,
                            rx.redirect("/expert-dashboard"),
                        ],
                    ),

                    rx.button(

                        "Close",

                        width="100%",

                        variant="outline",

                        on_click=LandingState.close_modal,
                    ),

                    spacing="5",

                    align="center",
                ),

                padding="3em",

                width="400px",

                border_radius="25px",

                background="#111827",

                border="1px solid cyan",

                box_shadow="0 0 40px cyan",
            ),

            position="fixed",

            top="0",

            left="0",

            width="100vw",

            height="100vh",

            background="rgba(0,0,0,0.7)",

            z_index="9999",
        ),
    )


# -----------------------------
# LANDING PAGE
# -----------------------------

def landing_page():

    return rx.box(

        navbar(),

        hero_section(),

        login_modal(),

        rx.center(

            rx.hstack(

                feature_card(
                    "Scam Detection",
                    "Learn to identify phishing emails, fake UPI alerts, and online fraud.",
                    "cyan",
                ),

                feature_card(
                    "Gamified Learning",
                    "Improve cyber awareness through interactive challenges and quizzes.",
                    "purple",
                ),

                feature_card(
                    "NFT Reward Simulation",
                    "Experience simulated gasless NFT rewards using UGF concepts.",
                    "green",
                ),

                spacing="6",

                wrap="wrap",

                justify="center",
            ),

            padding="4em",
        ),

        background="#030712",

        min_height="100vh",
    )


# -----------------------------
# ROUTES
# -----------------------------

app.add_page(
    landing_page,
    route="/",
    title="CyberShield",
)

app.add_page(
    dashboard_page,
    route="/dashboard",
)

app.add_page(
    quiz_page,
    route="/quiz",
)

app.add_page(
    leaderboard_page,
    route="/leaderboard",
)

app.add_page(
    nft_gallery_page,
    route="/nft-gallery",
)

app.add_page(
    expert_dashboard_page,
    route="/expert-dashboard",
)