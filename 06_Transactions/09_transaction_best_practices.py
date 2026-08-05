"""
File:
    09_transaction_best_practices.py

Purpose:
    Demonstrate MongoDB Transaction Best Practices
    using an executable checklist.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""


def line():

    print("=" * 100)


def print_best_practices():

    practices = [

        (
            "Validate Data Before Transaction",
            "Perform validations before opening the transaction."
        ),

        (
            "Keep Transactions Short",
            "Avoid long-running transactions."
        ),

        (
            "Use One Session",
            "Pass the same session to every CRUD operation."
        ),

        (
            "Retry Only Transient Errors",
            "Do not retry business validation errors."
        ),

        (
            "Avoid External APIs",
            "Email, SMS and Payment APIs should normally be called after commit."
        ),

        (
            "Log Every Transaction",
            "Store transaction id, timestamps and status."
        ),

        (
            "Use Unique IDs",
            "Generate unique order/payment/reference numbers."
        ),

        (
            "Keep Documents Small",
            "Large documents increase transaction duration."
        ),

        (
            "Monitor Performance",
            "Track retries, aborts and commit duration."
        ),

        (
            "Design Idempotent Operations",
            "Safe retries should not create duplicate records."
        )

    ]

    line()

    print("MONGODB TRANSACTION BEST PRACTICES")

    line()

    for index, practice in enumerate(practices, start=1):

        print(f"\n{index}. {practice[0]}")

        print(f"   ➜ {practice[1]}")


def transaction_checklist():

    line()

    print("PRODUCTION READINESS CHECKLIST")

    line()

    questions = [

        "Have you validated all user inputs?",

        "Is the transaction short?",

        "Are all CRUD operations using the same session?",

        "Are external API calls outside the transaction?",

        "Are retryable errors handled?",

        "Are business errors excluded from retry?",

        "Are transaction logs implemented?",

        "Are unique IDs generated?",

        "Have you tested rollback?",

        "Have you tested successful commit?"

    ]

    score = 0

    for question in questions:

        answer = input(

            f"{question} (Y/N): "

        ).strip().upper()

        if answer == "Y":

            score += 1

    line()

    print("RESULT")

    line()

    print(f"Checklist Score : {score}/{len(questions)}")

    print()

    if score == len(questions):

        print("Excellent!")

        print("Your transaction follows production best practices.")

    elif score >= 7:

        print("Good!")

        print("Minor improvements recommended.")

    elif score >= 5:

        print("Average.")

        print("Review transaction design before deployment.")

    else:

        print("Needs Improvement.")

        print("Do not deploy this transaction yet.")

    line()


def transaction_summary():

    line()

    print("TRANSACTION LIFECYCLE")

    line()

    print("""

User Request

    │

    ▼

Validation

    │

    ▼

Start Session

    │

    ▼

Start Transaction

    │

    ▼

CRUD Operations

    │

    ▼

Commit

OR

Abort

    │

    ▼

Close Session

""")

    line()


def main():

    transaction_summary()

    print_best_practices()

    transaction_checklist()


if __name__ == "__main__":

    main()