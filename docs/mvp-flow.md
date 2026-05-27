# MVP Flow

This document describes the main user flow for the first version of the system.

# MVP Goal

Allow user to manually manage their personal finances by creating accounts, categories, transitions, and by viewing a basic financial dashboard.

This phase will not include real bank integrations.

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
- Multi-user/shared accounts

## Main Flow

User
↓
Logs in
↓
Creates or selects an account
↓
Creates a transaction
↓
Select a category
↓
Views the dashboard

## Main Screens

The MVP will include the following screens:

- Login
- Register
- Dashboard
- Accounts
- Categories
- Transactions
- Create Transaction
- Settings

## Basic Rules

- Each user can only access their own data.
- Each account belongs to one user.
- Each category belongs to one user.
- Each transaction belongs to one user.
- Each transaction belongs to one account.
- Each transaction can have one category.
- The dashboard must only use data from the authenticated user.

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
