# 💰 Cash Flow Management Web Service

## 📘 Description

**Cash Flow (CF)** — is the process of accounting, managing, and analyzing all inflows and outflows of money for a company or an individual.
This web application allows users to manage and track all financial transactions with full CRUD functionality and logical relationships between entities.

The goal of this project is to implement a **user-friendly, intuitive web service** for recording, viewing, and analyzing cash movements.

---

## 🚀 Features

### 💵 Cash Flow Records

Users can **create**, **edit**, **delete**, and **view** financial transaction records.

**Fields:**

* **Creation Date** — automatically filled, but editable (e.g., `01.01.2025`)
* **Status** — predefined values:

  * `Business`
  * `Personal`
  * `Tax`
    *(this list should be extendable)*
* **Type** — predefined values:

  * `Income`
  * `Expense`
    *(this list should be extendable)*
* **Category / Subcategory** — examples:

  * Category **Infrastructure** → Subcategories: `VPS`, `Proxy`
  * Category **Marketing** → Subcategories: `Farpost`, `Avito`
    *(the list should be extendable)*
* **Amount** — amount in RUB, e.g. `1,000 ₽`
* **Comment** — optional free-form text

---

### 📋 Record List

* Displays a **table** with:
  `Date | Status | Type | Category | Subcategory | Amount | Comment`
* Supports **filtering** by:

  * Date range
  * Status
  * Type
  * Category
  * Subcategory

---

### ✏️ Editing Records

* Any field of a record can be modified.

---

### 🗑️ Deleting Records

* Any record can be deleted.

---

### ⚙️ Reference Management

* Ability to **add, edit, and delete**:

  * Statuses
  * Types
  * Categories
  * Subcategories
* Ability to set **logical relationships**:

  * Subcategories belong to Categories
  * Categories belong to Types
    Example:
    `Type: Expense → Category: Marketing → Subcategories: Farpost, Avito`

---

## 🧩 Business Rules

* A **subcategory** cannot be selected if it is not linked to the chosen **category**.
* A **category** cannot be selected if it is not linked to the chosen **type**.
* Fields `amount`, `type`, `category`, and `subcategory` are **required**.
* Client-side and server-side validation must be implemented.