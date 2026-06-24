# MVP Data Model

This document describes the initial data model for the MVP.

The goal is to define the minimum entities, responsibilities, relationships, and modeling rules required to support the MVP flow.

This document focuses on the conceptual model, not the final database implementation.

## Modeling Principles

- Keep the model simple.
- Store only what is needed for the MVP.
- Keep each user's data isolated.
- Calculate dashboard values from stored financial data.
- Avoid modeling future features unless they affect current MVP decisions.

## MVP Entities

The MVP has four main entities:

```text
User
Account
Category
Transaction
```

These entities are enough to support the main MVP flow:

```text
User
->
Registers or logs in
->
Creates or selects an account
->
Creates a transaction
->
Selects a category
->
Views the dashboard
```

## User

The `User` represents a person who uses the system to manage their personal finances.

Each user owns their own financial data.

### Possible fields

```text
id
name
email
password_hash
created_at
updated_at
```

### Relationships

```text
User 1 ----- N Account
User 1 ----- N Category
User 1 ----- N Transaction
```

### Rules

- A user can only access their own data.
- Email must be unique.
- Passwords must never be stored as plain text.
- Accounts, categories, and transactions must always be associated with a user.
- The dashboard must only display data from the authenticated user.

## Account

The `Account` represents a manual financial container where the user tracks money.

An account does not necessarily mean a real bank account. In the MVP, accounts are created and managed manually by the user.

Examples:

- Bank account
- Digital wallet
- Physical wallet
- Credit card
- Manual cash account

### Possible fields

```text
id
user_id
name
type
initial_balance
created_at
updated_at
```

### Possible account types

```text
checking
savings
wallet
cash
credit_card
other
```

### Relationships

```text
User 1 ------- N Account
Account 1 ---- N Transaction
```

### Rules

- Each account belongs to one user.
- A user can create multiple accounts.
- Account name is required.
- Initial balance defaults to 0.
- A transaction must belong to one account.
- Account balance is calculated from the account initial balance plus transactions.
- Accounts are not connected to real banks in the MVP.

### Notes

- In the MVP, credit cards are treated as simple manual accounts.
- Credit card invoice closing dates, due dates, limits, and payment workflows are out of scope.
- Investment tracking is out of scope for the MVP, so investment accounts are not modeled as a specific account type yet.

## Category

The `Category` represents the classification of a transaction.

Examples:

- Food
- Transportation
- Housing
- Salary
- Entertainment
- Healthcare

### Possible fields

```text
id
user_id
name
type
created_at
updated_at
```

### Possible category types

```text
income
expense
```

### Relationships

```text
User 1 -------- N Category
Category 1 ---- N Transaction
```

### Rules

- Each category belongs to one user.
- Category name is required.
- Categories are not shared between users in the MVP.
- Each transaction must have exactly one category.
- A category can be used by many transactions.
- The category selected for a transaction must belong to the same user as the transaction.

### Notes

- In the MVP, `Category` and `Transaction` do not have a many-to-many relationship.
- Multiple categories per transaction may be considered in the future.

## Transaction

The `Transaction` represents a manual financial movement.

A transaction can be either:

- Income
- Expense

Examples:

- Salary received
- Grocery purchase
- Rent payment
- App ride
- Cash withdrawal

### Possible fields

```text
id
user_id
account_id
category_id
type
amount
description
transaction_date
created_at
updated_at
```

### Possible transaction types

```text
income
expense
```

### Relationships

```text
User 1 -------- N Transaction
Account 1 ----- N Transaction
Category 1 ---- N Transaction
```

### Rules

- Each transaction belongs to one user.
- Each transaction belongs to one account.
- Each transaction must have exactly one category.
- The selected account and category must belong to the same user as the transaction.
- Type must be either `income` or `expense`.
- Amount must be greater than zero.
- Financial values should use decimal or numeric types, not floating-point types.
- Transaction date is required.
- Transaction date represents when the financial movement happened.
- Transactions are created manually in the MVP.

### Notes

- The transaction type defines whether the amount increases or decreases the account balance.
- The system should not import transactions from banks in the MVP.
- Transfers between accounts are not modeled as a feature in the MVP.

## Relationship Summary

The MVP relationship model is:

```text
User 1 -------- N Account
User 1 -------- N Category
User 1 -------- N Transaction

Account 1 ----- N Transaction
Category 1 ---- N Transaction
```

A simplified representation:

```text
User
-> Accounts
   -> Transactions
-> Categories
   -> Transactions
-> Transactions
```

## Dashboard Is Not an Entity

The dashboard is not a database entity in the MVP.

The dashboard is a screen that reads and summarizes data from:

- Accounts
- Transactions
- Categories

Examples of dashboard data:

- Total balance
- Monthly income
- Monthly expenses
- Monthly result
- Latest transactions
- Expenses by category
- Income vs expenses

### Rules

- The dashboard must only use data from the authenticated user.
- Dashboard values should be calculated from existing data.
- Dashboard data should not be duplicated unless there is a clear performance need in the future.

## Derived Values

The MVP should calculate financial summaries from accounts and transactions.

### Total balance

```text
sum(account.initial_balance) + sum(income transactions) - sum(expense transactions)
```

### Monthly income

```text
sum(income transactions where transaction_date is in the selected month)
```

### Monthly expenses

```text
sum(expense transactions where transaction_date is in the selected month)
```

### Monthly result

```text
monthly income - monthly expenses
```

### Expenses by category

```text
sum(expense transactions grouped by category)
```

## Data Type Guidance

The final database implementation will be defined later, but these decisions should guide it.

### IDs

UUIDs are recommended as identifiers.

Reasons:

- Avoid exposing sequential IDs.
- Safer for public APIs.
- Easier to use across distributed systems in the future.

### Financial values

Use decimal or numeric values for money.

Avoid floating-point values.

Reasons:

- Floating-point numbers can create precision issues.
- Financial systems need exact decimal behavior.

### Dates and timestamps

Use a date type for `transaction_date`.

Use timezone-aware timestamps for `created_at` and `updated_at`.

Reasons:

- `transaction_date` represents the financial event date.
- `created_at` and `updated_at` represent system timestamps.

## Deletion

Deletion behavior does not need to be finalized in the conceptual model.

For the MVP, the application should decide whether users can delete accounts, categories, and transactions based on product behavior.

Important considerations:

- Deleting a transaction affects calculated balances and dashboard values.
- Deleting an account with existing transactions can break historical data.
- Deleting a category with existing transactions can break reports.
- Soft delete with a `deleted_at` field may be considered later if the application needs recoverability or historical visibility.

## Out of Scope for MVP

The following concepts are intentionally not modeled in the MVP:

- Real bank integrations
- Open Finance consent records
- Automatic transaction synchronization
- Payment features
- Investment tracking
- Transfers between accounts
- Recurring transactions
- Transaction imports from files
- Shared accounts
- Multiple categories per transaction
- Budgets
- Goals
- Tags
- Attachments or receipts
- Cached dashboard summaries
- Audit logs

## MVP Decisions Summary

- The system has four main entities: `User`, `Account`, `Category`, and `Transaction`.
- Each user owns their own data.
- Accounts are manual and do not connect to real banks.
- Categories are created manually by each user.
- Transactions are created manually by each user.
- Each transaction belongs to one account.
- Each transaction must have exactly one category.
- The selected account and category must belong to the same user as the transaction.
- Dashboard data is calculated from accounts, transactions, and categories.
- Dashboard is not a database entity.
- Transfers are not modeled as an MVP feature.
- Financial values should use decimal or numeric types.
- UUIDs are recommended as identifiers.
- Timezone-aware timestamps are recommended for system timestamps.
- Open Finance is intentionally out of scope for the MVP.

## Future Considerations

The following improvements may be considered after the MVP:

- Bank integration
- Open Finance consent management
- Automatic transaction synchronization
- Transaction import from CSV or OFX
- Recurring transactions
- Linked transfers between accounts
- Multiple categories per transaction
- Shared accounts
- Investment tracking
- Budgets
- Goals
- Tags
- Attachments or receipts
- Advanced reports
- Cached dashboard summaries
- Audit logs
