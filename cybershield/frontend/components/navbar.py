import reflex as rx


def nav_link(text, url):

    return rx.link(

        rx.text(
            text,
            color="white",
            weight="medium",
        ),

        href=url,

        style={
            "text_decoration": "none",
        },
    )


def navbar():

    return rx.box(

        rx.hstack(

            # LOGO
            rx.hstack(

                rx.box(
                    width="14px",
                    height="14px",
                    border_radius="50%",
                    background="cyan",
                    box_shadow="0 0 15px cyan",
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

            rx.spacer(),

            # NAVIGATION LINKS
            rx.hstack(

                nav_link(
                    "Home",
                    "/",
                ),

                nav_link(
                    "Dashboard",
                    "/dashboard",
                ),

                nav_link(
                    "Quiz",
                    "/quiz",
                ),

                nav_link(
                    "Leaderboard",
                    "/leaderboard",
                ),

                nav_link(
                    "NFT Gallery",
                    "/nft-gallery",
                ),

                spacing="6",
            ),

            # BUTTON
            rx.button(

                "Start Learning",

                color_scheme="cyan",

                radius="large",

                size="3",

                on_click=rx.redirect(
                    "/quiz"
                ),
            ),

            width="100%",
            align="center",
        ),

        position="sticky",

        top="0",

        z_index="999",

        width="100%",

        padding="1.2em 2em",

        background="rgba(3,7,18,0.85)",

        backdrop_filter="blur(10px)",

        border_bottom="1px solid #1f2937",
    )