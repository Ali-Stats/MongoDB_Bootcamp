# MongoDB Bootcamp

# Phase 03 - Query Operators

**Author:** Syed Ali Ashraf

---

# Table of Contents

- Introduction
- Learning Objectives
- Query Operators Overview
- Comparison Operators
- Logical Operators
- Element Operators
- Evaluation Operators
- Array Operators
- Internal Working
- Performance Tips
- Best Practices
- Common Mistakes
- Interview Questions
- Assignment
- Summary

---

# Introduction

Query Operators allow MongoDB to filter documents based on specific conditions.

Instead of retrieving every document, operators help return only the required records efficiently.

---

# Learning Objectives

After completing this phase you should understand

- Comparison Operators
- Logical Operators
- Element Operators
- Evaluation Operators
- Array Operators
- Combining Operators
- Production Query Design

---

# Query Operators Overview

```

Application

↓

find()

↓

Query Operators

↓

Matching Documents

↓

Results

```

---

# Comparison Operators

## $eq

Equal To

```python
collection.find(

    {

        "city":{

            "$eq":"Delhi"

        }

    }

)
```

---

## $ne

Not Equal

```python
collection.find(

    {

        "city":{

            "$ne":"Delhi"

        }

    }

)
```

---

## $gt

Greater Than

```python
collection.find(

    {

        "price":{

            "$gt":500

        }

    }

)
```

---

## $gte

Greater Than or Equal

```python
collection.find(

    {

        "price":{

            "$gte":500

        }

    }

)
```

---

## $lt

Less Than

```python
collection.find(

    {

        "price":{

            "$lt":500

        }

    }

)
```

---

## $lte

Less Than or Equal

```python
collection.find(

    {

        "price":{

            "$lte":500

        }

    }

)
```

---

## $in

```python
collection.find(

    {

        "city":{

            "$in":[

                "Delhi",

                "Mumbai"

            ]

        }

    }

)
```

---

## $nin

```python
collection.find(

    {

        "city":{

            "$nin":[

                "Delhi",

                "Mumbai"

            ]

        }

    }

)
```

---

# Logical Operators

## $and

```python
collection.find(

{

"$and":[

{"city":"Delhi"},

{"age":{"$gt":25}}

]

}

)
```

---

## $or

```python
collection.find(

{

"$or":[

{"city":"Delhi"},

{"city":"Mumbai"}

]

}

)
```

---

## $not

```python
collection.find(

{

"age":{

"$not":{

"$gt":30

}

}

}

)
```

---

## $nor

```python
collection.find(

{

"$nor":[

{"city":"Delhi"},

{"city":"Mumbai"}

]

}

)
```

---

# Element Operators

## $exists

```python
collection.find(

{

"phone":{

"$exists":True

}

}

)
```

---

## $type

```python
collection.find(

{

"price":{

"$type":"int"

}

}

)
```

---

# Evaluation Operators

## Regular Expression

```python
collection.find(

{

"name":{

"$regex":"^A"

}

}

)
```

---

## Text Search

```python
collection.find(

{

"$text":{

"$search":"Pizza"

}

}

)
```

---

# Array Operators

## $all

```python
collection.find(

{

"tags":{

"$all":[

"veg",

"pizza"

]

}

}

)
```

---

## $size

```python
collection.find(

{

"items":{

"$size":3

}

}

)
```

---

## $elemMatch

```python
collection.find(

{

"scores":{

"$elemMatch":{

"$gt":80

}

}

}

)
```

---

# Combining Operators

Example

```python
collection.find(

{

"$and":[

{

"price":{

"$gte":200

}

},

{

"price":{

"$lte":500

}

},

{

"available":True

}

]

}

)
```

---

# Internal Working

```

find()

↓

Parse Query

↓

Query Planner

↓

Check Index

↓

Collection Scan (if needed)

↓

Matching Documents

↓

Return Result

```

---

# Performance Tips

- Create indexes on frequently searched fields.
- Avoid regex without indexes.
- Prefer equality over inequality.
- Combine filters efficiently.
- Use projection.
- Limit returned documents.

---

# Best Practices

- Use indexes.
- Filter early.
- Avoid unnecessary operators.
- Keep queries readable.
- Test queries using explain().

---

# Common Mistakes

- Using regex on large collections.
- Missing indexes.
- Incorrect operator combinations.
- Querying wrong data types.
- Returning unnecessary fields.

---

# Interview Questions

### Beginner

1. What are Query Operators?

2. Difference between $eq and $ne?

3. Difference between $gt and $gte?

4. Difference between $lt and $lte?

5. Difference between $in and $nin?

---

### Intermediate

6. Explain $exists.

7. Explain $type.

8. Explain $regex.

9. Explain $all.

10. Explain $elemMatch.

---

### Advanced

11. Which operators benefit most from indexes?

12. Why are regex queries slower?

13. Explain MongoDB Query Planner.

14. Difference between Collection Scan and Index Scan.

15. Explain query optimization.

---

# Assignment

Using your Retail Analytics dataset, write queries using

- $eq
- $ne
- $gt
- $gte
- $lt
- $lte
- $in
- $nin
- $exists
- $type
- $regex
- $all
- $size
- $elemMatch
- $and
- $or
- $not
- $nor

---

# Summary

After completing Phase 03 you understand

- Comparison Operators
- Logical Operators
- Element Operators
- Evaluation Operators
- Array Operators
- Query Optimization
- Production Query Design

You can now write efficient MongoDB queries for real-world applications.