import reflex as rx


# -----------------------------
# NFT STATE
# -----------------------------

class NFTState(rx.State):

    show_popup: bool = False

    transaction_complete: bool = False

    selected_nft: str = ""

    tx_hash: str = ""

    # OPEN POPUP
    async def mint_nft(
    self,
    nft_name: str,
):

        self.selected_nft = nft_name

        self.show_popup = True

        self.transaction_complete = False

        self.tx_hash = ""

        yield

        import asyncio

        await asyncio.sleep(5)

        self.complete_transaction()

    # COMPLETE TRANSACTION
    def complete_transaction(self):

        self.transaction_complete = True

        self.tx_hash = "0x8f2c9a4e2d91a72f"

    # CLOSE POPUP
    def close_popup(self):

        self.show_popup = False


# -----------------------------
# NFT CARD
# -----------------------------

def nft_card(
    title: str,
    description: str,
    color: str,
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
                text_align="center",
            ),

            rx.button(

                "Mint NFT",

                width="100%",

                color_scheme="cyan",

                radius="large",

                on_click=lambda:
                NFTState.mint_nft(title),
            ),

            spacing="4",

            align="center",
        ),

        padding="2em",

        width="320px",

        border_radius="20px",

        background="#111827",

        border=f"1px solid {color}",

        transition="all 0.3s ease",

        _hover={
            "transform": "translateY(-10px)",
            "box_shadow": f"0 0 30px {color}",
        },
    )


# -----------------------------
# TRANSACTION POPUP
# -----------------------------

def transaction_popup():

    return rx.cond(

        NFTState.show_popup,

        rx.center(

            rx.box(

                rx.vstack(

                    rx.heading(
                        "UGF Transaction",
                        size="7",
                        color="cyan",
                    ),

                    rx.text(
                        NFTState.selected_nft,
                        color="#d1d5db",
                    ),

                    rx.divider(),

                    rx.cond(

                        NFTState.transaction_complete,

                        rx.vstack(

                            rx.text(
                                "Wallet Connected ✅",
                                color="green",
                            ),

                            rx.text(
                                "UGF Sponsored Gas Fee ✅",
                                color="green",
                            ),

                            rx.text(
                                "Mock USD Payment Successful ✅",
                                color="green",
                            ),

                            rx.text(
                                "NFT Minted Successfully ✅",
                                color="green",
                            ),

                            rx.divider(),

                            rx.text(
                                NFTState.tx_hash,
                                color="cyan",
                            ),

                            rx.button(

                                "Close",

                                width="100%",

                                color_scheme="cyan",

                                on_click=
                                NFTState.close_popup,
                            ),

                            spacing="4",
                        ),

                        rx.vstack(

                            rx.spinner(),

                            rx.text(
                                "Processing Gasless Transaction...",
                                color="#d1d5db",
                            ),

                            rx.text(
                                "UGF is sponsoring gas fees",
                                color="cyan",
                            ),

                            

                            spacing="4",
                        ),
                    ),

                    spacing="5",

                    align="center",
                ),

                padding="3em",

                width="450px",

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
# NFT GALLERY PAGE
# -----------------------------

def nft_gallery_page():

  return rx.box(

    transaction_popup(),

    rx.center(

        rx.vstack(

            rx.heading(
                "NFT Reward Gallery",
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
                "Earn NFT rewards through cyber awareness challenges",
                size="5",
                color="#9ca3af",
            ),

            spacing="3",
        ),
    ),

    rx.center(

        rx.hstack(

            nft_card(
                "Phishing Defender",
                "Awarded for identifying phishing attacks.",
                "cyan",
            ),

            nft_card(
                "UPI Scam Hunter",
                "Awarded for detecting fake UPI scams.",
                "purple",
            ),

            nft_card(
                "Cyber Guardian",
                "Awarded for completing awareness challenges.",
                "green",
            ),

            spacing="6",

            wrap="wrap",
        ),

        margin_top="5em",
    ),

    background="""
    radial-gradient(circle at top,
    #111827,
    #030712)
    """,

    min_height="100vh",

    padding="3em",

    padding_bottom="5em",
)