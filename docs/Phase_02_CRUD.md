# MongoDB Bootcamp

# Phase 02 - CRUD Operations

**Author:** Syed Ali Ashraf

---

# Table of Contents

- Introduction
- Learning Objectives
- CRUD Overview
- Insert Operations
- Read Operations
- Update Operations
- Delete Operations
- Projection
- Sorting
- Limit
- Skip
- Internal Working
- Performance Tips
- Best Practices
- Common Mistakes
- Interview Questions
- Assignment
- Summary

---

# Introduction

CRUD stands for

- Create
- Read
- Update
- Delete

These four operations are the foundation of every MongoDB application.

---

# Learning Objectives

After completing this phase you should understand

- insert_one()
- insert_many()
- find()
- find_one()
- update_one()
- update_many()
- delete_one()
- delete_many()
- Projection
- Sorting
- Skip
- Limit

---

# CRUD Overview

```

Application

↓

PyMongo

↓

MongoDB

↓

CRUD Operation

↓

Database Updated

```

---

# Insert Operations

## insert_one()

Adds a single document.

Example

```python
collection.insert_one(
    {
        "name":"John",
        "age":30
    }
)
```

---

## insert_many()

Adds multiple documents.

```python
collection.insert_many(

    [

        {"name":"John"},

        {"name":"Alice"},

        {"name":"Bob"}

    ]

)
```

---

# Read Operations

## find()

Returns multiple documents.

```python
collection.find()
```

---

## find_one()

Returns first matching document.

```python
collection.find_one(

    {

        "name":"John"

    }

)
```

---

# Projection

Projection selects only required fields.

```python
collection.find(

    {},

    {

        "_id":0,

        "name":1,

        "age":1

    }

)
```

---

# Sorting

Ascending

```python
collection.find().sort(

    "age",

    1

)
```

Descending

```python
collection.find().sort(

    "age",

    -1

)
```

---

# Limit

```python
collection.find().limit(10)
```

Returns first 10 documents.

---

# Skip

```python
collection.find().skip(20)
```

Skips first 20 documents.

---

# Update Operations

## update_one()

```python
collection.update_one(

    {

        "name":"John"

    },

    {

        "$set":{

            "city":"Delhi"

        }

    }

)
```

---

## update_many()

```python
collection.update_many(

    {

        "premiumMember":False

    },

    {

        "$set":{

            "discount":5

        }

    }

)
```

---

# Update Operators

### $set

Creates or updates fields.

### $inc

Increment numeric values.

```python
"$inc":{"loyaltyPoints":10}
```

### $unset

Removes a field.

```python
"$unset":{"phone":""}
```

### $rename

Rename field.

### $push

Append to array.

### $pull

Remove from array.

---

# Delete Operations

## delete_one()

```python
collection.delete_one(

    {

        "customerID":"C00001"

    }

)
```

---

## delete_many()

```python
collection.delete_many(

    {

        "city":"Delhi"

    }

)
```

---

# Internal Working

Insert

```

Python Dictionary

↓

PyMongo

↓

BSON

↓

MongoDB

↓

Disk

```

---

Read

```

Application

↓

Index Search

↓

Collection Scan

↓

Documents

↓

Result

```

---

Update

```

Find Document

↓

Modify

↓

Update Index

↓

Write to Disk

```

---

Delete

```

Find Document

↓

Remove

↓

Update Index

↓

Free Storage

```

---

# Performance Tips

- Always use indexes.
- Project only required fields.
- Avoid unnecessary updates.
- Delete carefully.
- Batch inserts using insert_many().
- Prefer update_many() when appropriate.
- Use limit() for testing.

---

# Best Practices

- Validate before inserting.
- Keep updates minimal.
- Use projections.
- Avoid deleting without filters.
- Use transactions for related updates.
- Create indexes on search fields.

---

# Common Mistakes

- Missing filter in update_many().
- Missing filter in delete_many().
- Returning unnecessary fields.
- Forgetting projections.
- Updating entire documents unnecessarily.
- Inserting duplicate data.

---

# Interview Questions

### Beginner

1. What is CRUD?

2. Difference between find() and find_one()?

3. Difference between insert_one() and insert_many()?

4. Difference between update_one() and update_many()?

5. Difference between delete_one() and delete_many()?

---

### Intermediate

6. Explain Projection.

7. Explain sort().

8. Explain skip().

9. Explain limit().

10. Why use update operators?

---

### Advanced

11. Why is projection faster?

12. How does MongoDB perform updates internally?

13. What happens after delete?

14. Why should updates use indexes?

15. Difference between full document replacement and $set?

---

# Assignment

Perform

- 10 insert_one()
- 1 insert_many()
- 5 find()
- 5 find_one()
- 5 update_one()
- 3 update_many()
- 3 delete_one()
- 2 delete_many()

using your Retail Analytics dataset.

---

# Summary

After completing Phase 02 you can

- Insert Documents
- Read Documents
- Update Documents
- Delete Documents
- Sort Results
- Limit Results
- Skip Records
- Use Projection
- Use Update Operators
- Perform Production CRUD Operations

CRUD forms the foundation of every MongoDB application.