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


# To Use:
"""
# Task 3: Quizzes  <a id="task-3"></a>

To complete this notebook, you can work through the following quizzes.

*Note: You can select your solutions without running the preceding code.*


import quizzes
quizzes.run("merge_conflict_quizz")

"""