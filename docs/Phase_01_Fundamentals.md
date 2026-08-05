# MongoDB Bootcamp

# Phase 01 - Fundamentals

**Author:** Syed Ali Ashraf

---

# Table of Contents

- Introduction
- Learning Objectives
- What is MongoDB?
- Why MongoDB?
- SQL vs NoSQL
- MongoDB Architecture
- BSON
- Documents
- Collections
- Databases
- ObjectId
- MongoDB Components
- Internal Working
- Advantages
- Limitations
- Best Practices
- Common Mistakes
- Interview Questions
- Assignment
- Summary

---

# Introduction

MongoDB is an open-source NoSQL document database developed to store and manage large volumes of structured, semi-structured and unstructured data.

Unlike relational databases, MongoDB stores data as flexible BSON documents instead of rows and tables.

---

# Learning Objectives

After completing this phase you should understand:

- MongoDB
- NoSQL
- BSON
- Documents
- Collections
- Databases
- ObjectId
- MongoDB Architecture
- SQL vs MongoDB

---

# What is MongoDB?

MongoDB is a document-oriented NoSQL database.

Characteristics:

- Document Database
- Open Source
- High Performance
- Flexible Schema
- Horizontally Scalable
- Cross Platform

Official Terminology

| SQL | MongoDB |
|------|----------|
| Database | Database |
| Table | Collection |
| Row | Document |
| Column | Field |
| Primary Key | _id |
| JOIN | $lookup |

---

# Why MongoDB?

Traditional relational databases become difficult to scale horizontally when data grows rapidly.

MongoDB solves this by:

- Flexible schema
- JSON-like documents
- Horizontal scaling
- Replica Sets
- Sharding
- Fast development

Common Use Cases

- E-Commerce
- Banking
- Food Delivery
- Healthcare
- IoT
- AI Applications
- Analytics

---

# SQL vs NoSQL

| Feature | SQL | MongoDB |
|----------|-----|----------|
| Schema | Fixed | Flexible |
| Storage | Rows | Documents |
| Scaling | Vertical | Horizontal |
| Joins | Native | $lookup |
| Performance | Excellent for relationships | Excellent for documents |
| Transactions | Yes | Yes |
| Flexibility | Low | High |

---

# MongoDB Architecture

```

Application

↓

PyMongo Driver

↓

MongoDB Server

↓

Database

↓

Collection

↓

Document

```

---

# BSON

BSON stands for

**Binary JSON**

MongoDB stores every document internally in BSON format.

Advantages

- Faster serialization
- Efficient indexing
- More data types
- Smaller storage footprint

Supported Data Types

- String
- Integer
- Double
- Boolean
- Date
- Array
- Object
- ObjectId
- Binary
- Null

---

# Database

A database contains one or more collections.

Example

```

RetailAnalyticsDB

FoodDeliveryDB

BankDB

HospitalDB

```

---

# Collection

A collection stores related documents.

Example

```

customers

restaurants

orders

payments

menu

employees

```

Equivalent to a SQL table.

---

# Document

A document stores actual data.

Example

```json
{
    "customerID":"C00001",
    "name":"Radhika Nanda",
    "email":"abc@gmail.com",
    "premiumMember":false
}
```

Equivalent to a SQL row.

---

# ObjectId

Every MongoDB document automatically contains

```
_id
```

Example

```
66b3ec28f2b5414e82629eaf
```

ObjectId consists of:

- Timestamp
- Machine Identifier
- Process Identifier
- Counter

Benefits

- Globally Unique
- Automatically Generated
- Indexed

---

# MongoDB Components

```

Client

↓

MongoClient

↓

MongoDB Server

↓

Database

↓

Collection

↓

Document

```

---

# Internal Working

When Python executes

```python
collection.insert_one(document)
```

MongoDB performs

```

Python Dictionary

↓

PyMongo

↓

BSON Conversion

↓

Network Packet

↓

MongoDB Server

↓

Validation

↓

Storage Engine (WiredTiger)

↓

Disk

↓

Indexes Updated

↓

Acknowledgement Returned

```

---

# Advantages

- Flexible Schema
- Easy Scaling
- High Performance
- Powerful Aggregation
- Rich Indexing
- Replica Sets
- Transactions
- Excellent Python Integration

---

# Limitations

- Data duplication can occur
- JOINs are limited compared to SQL
- Schema discipline must be maintained by developers
- Large documents reduce performance

---

# Best Practices

- Design collections carefully
- Keep documents small
- Use indexes wisely
- Validate important fields
- Choose embedding vs referencing appropriately
- Avoid unnecessary collections
- Monitor query performance

---

# Common Mistakes

- Treating MongoDB like SQL
- Creating too many collections
- Ignoring indexes
- Embedding excessively
- Storing unnecessary data
- Not validating documents

---

# Interview Questions

### Beginner

1. What is MongoDB?

2. What is BSON?

3. Difference between Collection and Document?

4. Difference between SQL and MongoDB?

5. What is ObjectId?

### Intermediate

6. Why does MongoDB use BSON instead of JSON?

7. Explain MongoDB Architecture.

8. What are MongoDB Components?

9. Explain flexible schema.

10. Why is MongoDB called a Document Database?

---

# Assignment

Answer the following:

1. Why did MongoDB become popular?

2. Explain SQL vs MongoDB.

3. Draw MongoDB Architecture.

4. Explain ObjectId.

5. List five real-world applications of MongoDB.

---

# Summary

After completing Phase 01 you understand:

- MongoDB Fundamentals
- SQL vs NoSQL
- BSON
- Documents
- Collections
- Databases
- ObjectId
- MongoDB Architecture
- Internal Working
- Advantages
- Best Practices

You are now ready to perform CRUD Operations.