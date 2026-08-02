"""
File:
    10_best_practices.py

Purpose:
    MongoDB Schema Design Best Practices.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""


def schema_best_practices():

    print("=" * 100)
    print("MONGODB SCHEMA DESIGN HANDBOOK")
    print("=" * 100)

    print()

    print("=" * 100)
    print("1. EMBED VS REFERENCE")
    print("=" * 100)

    decision_matrix = [

        ("Child data is small", "Embed"),

        ("Always read together", "Embed"),

        ("Rarely updated", "Embed"),

        ("Large child collection", "Reference"),

        ("Frequently updated", "Reference"),

        ("Shared by many documents", "Reference"),

        ("Independent lifecycle", "Reference")

    ]

    for condition, recommendation in decision_matrix:

        print(f"{condition:<40} -> {recommendation}")

    print()

    print("=" * 100)
    print("2. RELATIONSHIP GUIDE")
    print("=" * 100)

    relationships = [

        ("One-to-One", "Embed or Reference"),

        ("One-to-Many (Small)", "Embed"),

        ("One-to-Many (Large)", "Reference"),

        ("Many-to-Many", "Bridge Collection")

    ]

    for relation, recommendation in relationships:

        print(f"{relation:<25} -> {recommendation}")

    print()

    print("=" * 100)
    print("3. DOCUMENT DESIGN")
    print("=" * 100)

    document_rules = [

        "Keep documents focused on one business entity.",

        "Avoid unnecessary nesting.",

        "Do not approach the 16 MB document limit.",

        "Embed only related child data.",

        "Avoid duplicate information whenever possible."

    ]

    for rule in document_rules:

        print(f"• {rule}")

    print()

    print("=" * 100)
    print("4. COLLECTION NAMING")
    print("=" * 100)

    naming = [

        "Use lowercase names.",

        "Use plural collection names.",

        "Avoid spaces.",

        "Use meaningful names."

    ]

    for rule in naming:

        print(f"• {rule}")

    print()

    print("=" * 100)
    print("5. FIELD NAMING")
    print("=" * 100)

    fields = [

        "customerID",

        "restaurantID",

        "orderStatus",

        "grandTotal",

        "createdAt",

        "updatedAt"

    ]

    for field in fields:

        print(f"• {field}")

    print()

    print("=" * 100)
    print("6. VALIDATION")
    print("=" * 100)

    validation = [

        "Use JSON Schema.",

        "Validate required fields.",

        "Validate data types.",

        "Use enums for status fields.",

        "Use regex for phone/email validation."

    ]

    for item in validation:

        print(f"• {item}")

    print()

    print("=" * 100)
    print("7. INDEXING")
    print("=" * 100)

    indexing = [

        "Index frequently queried fields.",

        "Prefer compound indexes when appropriate.",

        "Avoid unnecessary indexes.",

        "Always verify with explain().",

        "Monitor index usage."

    ]

    for item in indexing:

        print(f"• {item}")

    print()

    print("=" * 100)
    print("8. SCALABILITY")
    print("=" * 100)

    scalability = [

        "Reference large collections.",

        "Keep documents small.",

        "Avoid massive arrays.",

        "Design for millions of documents.",

        "Separate frequently changing data."

    ]

    for item in scalability:

        print(f"• {item}")

    print()

    print("=" * 100)
    print("9. COMMON MISTAKES")
    print("=" * 100)

    mistakes = [

        "Embedding huge child collections.",

        "Creating unnecessary indexes.",

        "Ignoring schema validation.",

        "Duplicating business data.",

        "Using $lookup excessively.",

        "Poor field naming.",

        "Not planning for growth."

    ]

    for item in mistakes:

        print(f"• {item}")

    print()

    print("=" * 100)
    print("10. PRODUCTION CHECKLIST")
    print("=" * 100)

    checklist = [

        "Relationship identified",

        "Embedding decision made",

        "References identified",

        "Indexes created",

        "Validation applied",

        "Naming standards followed",

        "Scalability reviewed",

        "Performance tested",

        "Backup strategy defined"

    ]

    for item in checklist:

        print(f"[✓] {item}")

    print()

    print("=" * 100)
    print("11. INTERVIEW CHEAT SHEET")
    print("=" * 100)

    cheat_sheet = [

        "Embed = Read together.",

        "Reference = Shared or growing data.",

        "Bridge Collection = Many-to-Many.",

        "16 MB maximum document size.",

        "Use explain() to verify indexes.",

        "Use JSON Schema for validation.",

        "Time Series for telemetry.",

        "TTL for temporary data.",

        "2dsphere for location.",

        "Compound Index for multi-field queries."

    ]

    for item in cheat_sheet:

        print(f"• {item}")

    print()

    print("=" * 100)
    print("END OF SCHEMA DESIGN PHASE")
    print("=" * 100)


if __name__ == "__main__":

    schema_best_practices()