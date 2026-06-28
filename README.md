# Secure User Authentication & Relational Database System

A security-focused backend authentication system built using Python and MySQL. This system demonstrates practical implementations of cryptographic user data protection and defenses against common database vulnerabilities like SQL injection.

---

##  Core Security Features

* **SHA-256 Cryptographic Hashing:** User passwords are encrypted using a secure, one-way cryptographic hash before database storage. The system never records or handles plain text passwords within the relational database layer.
* **SQL Injection Defense:** All communication routes utilize parameterized queries (`%s` placeholders), ensuring user inputs are treated strictly as data strings rather than executable database syntax.
* **Relational Schema Constraints:** Leverages structured SQL tables featuring strict indexing, unique username identifiers, and auto-incrementing primary keys to guarantee absolute data integrity.

---

##  Tech Stack Used

* **Language:** Python 3.x
* **Database Engine:** MySQL Server 8.0
* **Libraries:** `hashlib` (Built-in hashing engine), `mysql-connector-python` (Database Driver)

---

## Database Architecture (`schema.sql`)

```sql
CREATE DATABASE SecureAuthDB;
USE SecureAuthDB;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(64) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
