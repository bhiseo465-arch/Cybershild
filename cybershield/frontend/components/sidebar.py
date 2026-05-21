import reflex as rx


def sidebar_item(
    text: str,
    icon: str,
    url: str,
):

    return rx.link(

        rx.hstack(

            rx.text(
                icon,
                font_size="22px",
            ),

            rx.text(
                text,
                color="white",
                size="4",
                weight="medium",
            ),

            spacing="3",
            align="center",
        ),

        href=url,

        width="100%",

        padding="0.9em 1em",

        border_radius="14px",

        style={
            "text_decoration": "none",
        },

        transition="all 0.3s ease",

        _hover={
            "background": "#1f2937",
            "transform": "translateX(6px)",
        },
    )


def sidebar():

    return rx.box(

        rx.vstack(

            # LOGO
            rx.vstack(

                rx.box(
                    width="18px",
                    height="18px",
                    border_radius="50%",
                    background="cyan",
                    box_shadow="0 0 20px cyan",
                ),

                rx.heading(
                    "CyberShield",
                    size="7",
                    color="cyan",
                    weight="bold",
                ),

                spacing="3",
                align="center",
            ),

            rx.divider(),

            # MENU ITEMS
            sidebar_item(
                "Dashboard",
                "🏠",
                "/dashboard",
            ),

            sidebar_item(
                "Quiz",
                "🛡️",
                "/quiz",
            ),

            sidebar_item(
                "Leaderboard",
                "🏆",
                "/leaderboard",
            ),

            sidebar_item(
                "NFT Gallery",
                "🎖️",
                "/nft-gallery",
            ),

            sidebar_item(
                "Settings",
                "⚙️",
                "/",
            ),

            rx.spacer(),

            # FOOTER
            rx.box(

                rx.text(
                    "Cyber Awareness Platform",
                    color="#9ca3af",
                    size="2",
                ),

                padding_top="2em",
            ),

            spacing="4",

            width="100%",
        ),

        width="260px",

        min_height="100vh",

        padding="2em",

        background="#0f172a",

        border_right="1px solid #1f2937",

        position="fixed",

        left="0",

        top="0",
    )