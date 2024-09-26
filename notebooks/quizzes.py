from jupyterquiz import display_quiz

questions = [
    {
        "question": r"""Does the `git merge other_branch` command always create a merge conflict?""",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "yes",
                "correct": False
            },
            {
                "answer": "no",
                "correct": True,
                "feedback": r"""
                    If the branches do not change the same part of the codebase, Git will not create a merge conflict.
                """
            }
        ]
    },
]

def run(selection):
    if selection == 1:
        display_quiz(questions, shuffle_answers=False)