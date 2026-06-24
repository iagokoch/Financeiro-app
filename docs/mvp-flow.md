# MVP Flow

This document describes the main user flow for the first version of the system.

The goal is to define what the user can do in the MVP, what is intentionally out of scope, and which screens and rules are required to support the basic financial experience.

## MVP Goal

Allow users to manually manage their personal finances by creating accounts, categories, transactions, and viewing a basic financial dashboard.

This phase will not include real bank integrations. All financial data will be entered manually by the user.

## Scope

### Included in the MVP

- User registration and login
- Manual account creation
- Manual category creation
- Manual transaction creation
- Basic dashboard
- Monthly financial summary

### Not included in the MVP

- Real bank integration
- Open Finance integration
- Automatic transaction sync
- Bank consent management
- Payment features
- Investment tracking
- Multi-user or shared accounts

## Main Flow

The main user flow for the MVP is:

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

## Flow Description

### 1. User registration and login

The user must be able to create an account and log in to access the system.

Only authenticated users can access accounts, categories, transactions, and dashboard data.

### 2. Account creation or selection

After logging in, the user can create or select an account.

An account represents a place where the user tracks money. It can be a bank account, digital wallet, cash wallet, credit card, or any other simple manual financial account.

Examples:

- Nubank
- Itaú
- Wallet
- Credit card

### 3. Category creation or selection

The user can create categories to classify transactions.

Examples:

- Food
- Transportation
- Housing
- Salary
- Entertainment
- Healthcare

In the MVP, each transaction must have exactly one category.

### 4. Transaction creation

The user can manually create financial transactions.

A transaction can be either:

- Income
- Expense

Each transaction must belong to:

- One user
- One account
- One category

### 5. Dashboard visualization

The user can view a basic dashboard based on their own transactions.

The dashboard does not store financial data by itself. It only displays calculated information based on accounts, transactions, and categories.

## Main Screens

The MVP will include the following screens:

- Login
- Register
- Dashboard
- Accounts
- Categories
- Transactions
- Create Transaction

The following screen may be added later if needed:

- Settings

## Basic Rules

- Each user can only access their own data.
- Each account belongs to one user.
- Each category belongs to one user.
- Each transaction belongs to one user.
- Each transaction belongs to one account.
- Each transaction must have one category.
- The dashboard must only use data from the authenticated user.
- All transactions in the MVP are created manually.
- No external bank data will be imported in the MVP.
- Total balance is calculated from the account initial balance plus income transactions minus expense transactions.

## Dashboard Data

The dashboard will show a basic financial overview based on the user's transactions.

Initial dashboard cards:

- Total balance
- Monthly income
- Monthly expenses
- Monthly result
- Latest transactions

Initial charts:

- Income vs expenses
- Expenses by category

## MVP Assumptions

- The system is for personal finance management.
- Each user manages only their own financial data.
- There are no shared accounts between users in the MVP.
- There is no automatic bank synchronization in the MVP.
- The first version should prioritize simplicity, security, and clarity.
- The dashboard should be useful but not overly complex.

## Future Considerations

The following features may be considered after the MVP is validated:

- Open Finance integration
- Automatic transaction synchronization
- Bank account consent management
- Transaction import from files
- Recurring transactions
- Transfers between accounts with linked records
- Investment tracking
- Shared accounts
- Advanced reports
- Internal business analytics
