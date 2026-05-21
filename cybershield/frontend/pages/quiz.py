import reflex as rx


# -----------------------------
# QUIZ STATE
# -----------------------------

class QuizState(rx.State):

    questions = [

        {
            "question":
            "You receive an email saying your bank account will be blocked unless you click a link immediately. What should you do?",

            "options": [
                "Click the link quickly",
                "Ignore and verify through official bank app",
                "Share OTP immediately",
                "Forward email to friends",
            ],

            "correct":
            "Ignore and verify through official bank app",
        },

        {
            "question":
            "A stranger asks for your OTP claiming to be from customer support. What should you do?",

            "options": [
                "Share OTP",
                "Ignore and report",
                "Send screenshot",
                "Call them back",
            ],

            "correct":
            "Ignore and report",
        },

        {
            "question":
            "Which password is strongest?",

            "options": [
                "123456",
                "password",
                "Omkar123",
                "T9#xL!2pQ@7",
            ],

            "correct":
            "T9#xL!2pQ@7",
        },
    ]

    current_question = 0

    score = 0

    selected_option = ""

    quiz_finished = False


    # SELECT OPTION
    def select_option(self, option):

        self.selected_option = option


    # NEXT QUESTION
    def next_question(self):

        correct_answer = self.questions[
            self.current_question
        ]["correct"]

        if self.selected_option == correct_answer:

            self.score += 1

        self.selected_option = ""

        if self.current_question < len(self.questions) - 1:

            self.current_question += 1

        else:

            self.quiz_finished = True


    # RESTART QUIZ
    def restart_quiz(self):

        self.current_question = 0

        self.score = 0

        self.selected_option = ""

        self.quiz_finished = False


# -----------------------------
# OPTION BUTTON
# -----------------------------

def option_button(option):

    return rx.button(

        option,

        width="100%",

        padding="1.2em",

        border_radius="15px",

        background=rx.cond(
            QuizState.selected_option == option,
            "purple",
            "#1f2937",
        ),

        color="white",

        border="1px solid #374151",

        transition="all 0.3s ease",

        _hover={
            "transform": "scale(1.02)",
            "background": "#9333ea",
        },

        on_click=lambda: QuizState.select_option(option),
    )


# -----------------------------
# QUIZ PAGE
# -----------------------------

def quiz_page():

    return rx.box(

        # HEADER
        rx.center(

            rx.vstack(

                rx.heading(
                    "Cyber Awareness Quiz",
                    size="9",

                    background="""
                    linear-gradient(90deg, cyan, purple)
                    """,

                    background_clip="text",

                    color="transparent",
                ),

                rx.text(
                    "Test your phishing and scam detection skills.",
                    color="#9ca3af",
                    size="5",
                ),

                spacing="3",
            ),
        ),

        # QUIZ CONTENT
        rx.center(

            rx.cond(

                QuizState.quiz_finished,

                # RESULT SCREEN
                rx.box(

                    rx.vstack(

                        rx.heading(
                            "Quiz Completed",
                            size="8",
                            color="cyan",
                        ),

                        rx.heading(
                            f"{QuizState.score} / 3",
                            size="9",
                            color="green",
                        ),

                        rx.text(
                            "Great job improving your cyber awareness!",
                            color="#d1d5db",
                            size="5",
                        ),

                        rx.button(
                            "Restart Quiz",

                            size="4",

                            color_scheme="cyan",

                            radius="large",

                            on_click=QuizState.restart_quiz,
                        ),

                        rx.button(
                            "Go To Leaderboard",

                            size="4",

                            variant="outline",

                            color_scheme="purple",

                            radius="large",

                            on_click=rx.redirect(
                                "/leaderboard"
                            ),
                        ),

                        spacing="5",

                        align="center",
                    ),

                    padding="4em",

                    margin_top="4em",

                    border_radius="25px",

                    background="#111827",

                    border="1px solid cyan",

                    width="700px",

                    text_align="center",

                    box_shadow="0 0 35px cyan",
                ),

                # QUIZ QUESTIONS
                rx.box(

                    rx.vstack(

                        rx.text(
                            f"Question {QuizState.current_question + 1} of 3",

                            color="cyan",

                            size="4",
                        ),

                        rx.heading(
                            QuizState.questions[
                                QuizState.current_question
                            ]["question"],

                            size="6",

                            color="white",
                        ),

                        rx.vstack(

                            rx.foreach(

                                QuizState.questions[
                                    QuizState.current_question
                                ]["options"],

                                option_button,
                            ),

                            width="100%",

                            spacing="4",
                        ),

                        rx.button(

                            "Next Question",

                            size="4",

                            color_scheme="cyan",

                            radius="large",

                            width="100%",

                            margin_top="1em",

                            on_click=QuizState.next_question,
                        ),

                        spacing="6",

                        width="100%",
                    ),

                    padding="3em",

                    margin_top="4em",

                    border_radius="25px",

                    background="#111827",

                    border="1px solid #1f2937",

                    width="800px",

                    transition="all 0.3s ease",

                    _hover={
                        "box_shadow": "0 0 30px purple",
                    },
                ),
            ),
        ),

        background="""
        radial-gradient(circle at top, #111827, #030712)
        """,

        min_height="100vh",

        padding="3em",
    )