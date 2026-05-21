import reflex as rx


class AppState(rx.State):

    # -------------------------
    # USER DATA
    # -------------------------

    username: str = "Omkar"

    awareness_score: int = 92

    quizzes_completed: int = 12

    nft_rewards: int = 5

    current_rank: str = "Cyber Expert"

    # -------------------------
    # QUIZ STATE
    # -------------------------

    current_question: int = 0

    selected_option: str = ""

    score: int = 0

    quiz_finished: bool = False

    # -------------------------
    # SAMPLE QUESTIONS
    # -------------------------

    questions = [

        {
            "question":
            "Should you share OTP with customer support?",

            "options": [
                "Yes",
                "No",
                "Only if urgent",
                "Only on call",
            ],

            "correct":
            "No",
        },

        {
            "question":
            "What should you do when receiving a suspicious banking link?",

            "options": [
                "Open immediately",
                "Ignore and verify officially",
                "Forward to friends",
                "Enter bank details",
            ],

            "correct":
            "Ignore and verify officially",
        },

        {
            "question":
            "Which password is strongest?",

            "options": [
                "123456",
                "password",
                "Omkar123",
                "X@9kL#2pQ!",
            ],

            "correct":
            "X@9kL#2pQ!",
        },
    ]

    # -------------------------
    # SELECT OPTION
    # -------------------------

    def select_option(
        self,
        option: str,
    ):

        self.selected_option = option

    # -------------------------
    # NEXT QUESTION
    # -------------------------

    def next_question(self):

        correct_answer = self.questions[
            self.current_question
        ]["correct"]

        if (
            self.selected_option
            == correct_answer
        ):

            self.score += 1

        self.selected_option = ""

        if (
            self.current_question
            < len(self.questions) - 1
        ):

            self.current_question += 1

        else:

            self.quiz_finished = True

            self.awareness_score = int(
                (
                    self.score
                    / len(self.questions)
                )
                * 100
            )

    # -------------------------
    # RESET QUIZ
    # -------------------------

    def reset_quiz(self):

        self.current_question = 0

        self.selected_option = ""

        self.score = 0

        self.quiz_finished = False

    # -------------------------
    # NFT SIMULATION
    # -------------------------

    nft_status: str = "Not Minted"

    mint_loading: bool = False

    def simulate_nft_mint(self):

        self.mint_loading = True

        self.nft_status = (
            "UGF Processing..."
        )

    def complete_nft_mint(self):

        self.mint_loading = False

        self.nft_status = (
            "NFT Minted Successfully"
        )