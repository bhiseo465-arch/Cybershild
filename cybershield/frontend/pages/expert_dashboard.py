import reflex as rx


class ExpertState(rx.State):

    quizzes = [

        {
            "title": "Phishing Awareness",
            "difficulty": "Easy",
            "questions": 10,
        },

        {
            "title": "UPI Scam Detection",
            "difficulty": "Medium",
            "questions": 15,
        },

        {
            "title": "Password Security",
            "difficulty": "Hard",
            "questions": 20,
        },
    ]

    new_quiz_title: str = ""

    new_quiz_difficulty: str = "Easy"

    new_quiz_questions: str = ""

    # -------------------------
    # SETTERS
    # -------------------------

    def set_title(
        self,
        value: str,
    ):

        self.new_quiz_title = value

    def set_difficulty(
        self,
        value: str,
    ):

        self.new_quiz_difficulty = value

    def set_questions(
        self,
        value: str,
    ):

        self.new_quiz_questions = value

    # -------------------------
    # CREATE QUIZ
    # -------------------------

    def create_quiz(self):

        if (
            self.new_quiz_title == ""
            or self.new_quiz_questions == ""
        ):

            return

        self.quizzes.append(

            {
                "title":
                self.new_quiz_title,

                "difficulty":
                self.new_quiz_difficulty,

                "questions":
                int(
                    self.new_quiz_questions
                ),
            }
        )

        self.new_quiz_title = ""

        self.new_quiz_difficulty = "Easy"

        self.new_quiz_questions = ""

    # -------------------------
    # DELETE QUIZ
    # -------------------------

    def delete_quiz(
        self,
        title: str,
    ):

        self.quizzes = [

            quiz
            for quiz in self.quizzes
            if quiz["title"] != title
        ]


# -----------------------------
# QUIZ CARD
# -----------------------------

def admin_quiz_card(
    quiz,
):

    return rx.box(

        rx.vstack(

            rx.heading(
                quiz["title"],
                size="6",
                color="cyan",
            ),

            rx.badge(
                quiz["difficulty"],
                color_scheme="purple",
            ),

            rx.text(
                f"{quiz['questions']} Questions",
                color="#d1d5db",
            ),

            rx.hstack(

                rx.button(

                    "Edit",

                    color_scheme="purple",

                    radius="large",
                ),

                rx.button(

                    "Delete",

                    color_scheme="red",

                    radius="large",

                    on_click=lambda:
                    ExpertState.delete_quiz(
                        quiz["title"]
                    ),
                ),

                spacing="3",
            ),

            spacing="4",

            align="start",
        ),

        padding="2em",

        width="320px",

        border_radius="20px",

        background="#111827",

        border="1px solid cyan",

        transition="all 0.3s ease",

        _hover={
            "transform":
            "translateY(-8px)",

            "box_shadow":
            "0 0 25px cyan",
        },
    )


# -----------------------------
# EXPERT DASHBOARD PAGE
# -----------------------------

def expert_dashboard_page():

    return rx.box(

        # HEADER
        rx.center(

            rx.vstack(

                rx.heading(
                    "Cyber Expert Dashboard",
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
                    "Manage cyber awareness quizzes",
                    size="5",
                    color="#9ca3af",
                ),

                spacing="3",
            ),
        ),

        # CREATE QUIZ SECTION
        rx.center(

            rx.box(

                rx.vstack(

                    rx.heading(
                        "Create New Quiz",
                        size="7",
                        color="cyan",
                    ),

                    rx.input(

                        placeholder="Quiz Title",

                        value=
                        ExpertState.new_quiz_title,

                        on_change=
                        ExpertState.set_title,

                        width="100%",
                    ),

                    rx.select(

                        [
                            "Easy",
                            "Medium",
                            "Hard",
                        ],

                        value=
                        ExpertState.new_quiz_difficulty,

                        on_change=
                        ExpertState.set_difficulty,

                        width="100%",
                    ),

                    rx.input(

                        placeholder=
                        "Number of Questions",

                        value=
                        ExpertState.new_quiz_questions,

                        on_change=
                        ExpertState.set_questions,

                        width="100%",
                    ),

                    rx.button(

                        "Create Quiz",

                        width="100%",

                        color_scheme="cyan",

                        radius="large",

                        on_click=
                        ExpertState.create_quiz,
                    ),

                    spacing="4",

                    width="100%",
                ),

                width="500px",

                padding="2em",

                border_radius="25px",

                background="#111827",

                border="1px solid cyan",

                margin_top="4em",
            ),
        ),

        # QUIZ LIST
        rx.center(

            rx.vstack(

                rx.heading(
                    "Available Quizzes",
                    size="8",
                    color="white",
                ),

                rx.hstack(

                    rx.foreach(
                        ExpertState.quizzes,
                        admin_quiz_card,
                    ),

                    wrap="wrap",

                    spacing="6",

                    justify="center",
                ),

                spacing="6",

                margin_top="5em",
            ),
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