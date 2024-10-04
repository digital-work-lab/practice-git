from jupyterquiz import display_quiz

QUESTIONS = {
    "merge_conflict_quizz": [
        {
            "question": r"""Does the `git merge other_branch` command always create a merge conflict?""",
            "type": "multiple_choice",
            "answers": [
                {"answer": "yes", "correct": False},
                {
                    "answer": "no",
                    "correct": True,
                    "feedback": r"""
                    If the branches do not change the same part of the codebase, Git will not create a merge conflict.
                """,
                },
            ],
        },
    ],
}


def run(selection):
    if selection not in QUESTIONS:
        return
    display_quiz(QUESTIONS[selection], shuffle_answers=False)
