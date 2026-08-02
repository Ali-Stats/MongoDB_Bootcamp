"""
File:
    14_best_practices.py

Purpose:
    MongoDB Indexing Best Practices.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""


def best_practices():

    print("=" * 100)
    print("MONGODB INDEXING BEST PRACTICES")
    print("=" * 100)

    practices = [

        "1. Create indexes only for frequently queried fields.",

        "2. Avoid creating unnecessary indexes.",

        "3. Every index consumes disk space.",

        "4. Every insert/update/delete also updates indexes.",

        "5. Prefer Compound Indexes over many Single Field indexes.",

        "6. Follow the Left Prefix Rule.",

        "7. Use explain('executionStats') before optimizing queries.",

        "8. Use Text Indexes only for full-text search.",

        "9. Use TTL Indexes for temporary data.",

        "10. Use Sparse Indexes for optional fields.",

        "11. Use Partial Indexes when only a subset of documents is queried.",

        "12. Use Hashed Indexes mainly for sharding.",

        "13. Use Wildcard Indexes only for dynamic schemas.",

        "14. Use Geospatial Indexes for location-based applications.",

        "15. Regularly review unused indexes."

    ]

    for practice in practices:

        print("-" * 100)

        print(practice)

    print("-" * 100)

    print()

    print("=" * 100)
    print("COMMON MISTAKES")
    print("=" * 100)

    mistakes = [

        "Creating indexes on every field.",

        "Ignoring explain().",

        "Creating duplicate indexes.",

        "Wrong field order in compound indexes.",

        "Too many indexes slowing writes.",

        "Using Hashed Indexes for range queries.",

        "Using Wildcard Indexes unnecessarily.",

        "Never checking execution statistics."

    ]

    for mistake in mistakes:

        print("-" * 100)

        print(mistake)

    print("-" * 100)

    print()

    print("=" * 100)
    print("INDEX SELECTION GUIDE")
    print("=" * 100)

    guide = {

        "Equality Search":
            "Single / Compound Index",

        "Range Query":
            "B-Tree Index",

        "Full Text Search":
            "Text Index",

        "Temporary Documents":
            "TTL Index",

        "Optional Fields":
            "Sparse Index",

        "Subset of Documents":
            "Partial Index",

        "Dynamic Schema":
            "Wildcard Index",

        "Nearest Location":
            "2dsphere Index",

        "Sharding":
            "Hashed Index"

    }

    for key, value in guide.items():

        print("-" * 100)

        print(f"{key:<25} : {value}")

    print("-" * 100)


if __name__ == "__main__":

    best_practices()