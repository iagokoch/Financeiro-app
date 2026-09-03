# Financeiro App

Financeiro App is a personal finance management application focused on helping users organize their income, expenses, categories, and financial overview in a simple and manual way.

The first version of the project is an MVP and does not include real bank integrations. The goal is to validate the core financial flow before adding more advanced features such as Open Finance or third-party banking aggregators.

## Objective

The goal of this project is to allow users to manually manage their financial data, including accounts, categories, and transactions, and visualize a basic dashboard with their financial summary.

## Current Scope

The MVP will be manual and will not include real bank integrations.

In this phase, the user will be able to:

* Create an account
* Create categories
* Create transactions
* View a basic dashboard

Bank integrations through Open Finance or third-party aggregators are planned for a future phase.

## Features

* [ ] Account creation
* [ ] Category creation
* [ ] Transaction creation
* [ ] Basic financial dashboard
* [ ] Open Finance integration
* [ ] Third-party banking integration

## Stack

> Update this section according to the technologies used in the project.

* Front-end:
* Back-end:
* Database:
* Authentication:
* Deploy:
* Other services:

## How to Run Locally

Clone the repository:

```bash
git clone https://github.com/iagokoch/Financeiro-app.git
cd Financeiro-app
```

Install dependencies:

```bash
npm install
```

Run the development server:

```bash
npm run dev
```

## Environment Variables

Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

Then fill in the required environment variables.

Example:

```env
DATABASE_URL=
NEXT_PUBLIC_API_URL=
```

> Do not commit real credentials, tokens, or sensitive data.

## Security

Baseline practices for the MVP:

* **Never commit the real `.env`.** Only `.env.example` belongs in the repository, and it must contain placeholders — never real values.
* **Secrets come from environment variables**, never hardcoded in the source. No credential, key, or token should appear in a `.py` file, in tests, or in logs.
* **`DATABASE_URL` and the JWT key are secrets** and must be treated as such: rotated if leaked, never shared over chat/issues/commits, and different per environment (local, staging, production).
* **Dependencies stay locked.** `uv.lock` is committed and installs are made from it (`uv sync --frozen`) — no loose installs in production.

## Useful Scripts

```bash
npm run dev
npm run build
npm run lint
npm test
```

## Project Structure

```txt
financeiro-app/
  docs/
    diagrams/
    mvp-flow.md
    mvp-data-model.md
  src/
  README.md
```

## Documentation

The `docs/` folder contains the technical and planning documentation for the project.

Files:

* `docs/mvp-flow.md` — Describes the main user flow for the MVP.
* `docs/mvp-data-model.md` — Describes the main entities of the system and their relationships.
* `docs/diagrams/` — Contains the diagrams created with Excalidraw.

Diagrams:

* `docs/diagrams/mvp-flow.png`
* `docs/diagrams/mvp-data-model.png`

## Technical Decisions

* The MVP will start with manual financial data entry.
* Real bank integrations will not be included in the first version.
* Open Finance and third-party aggregators will be considered in a future phase.
* The project documentation will be kept inside the `docs/` folder.

## Deploy

> Add this section when the project is published.

Current deploy:

```txt
Not available yet.
```

## Publication Checklist

* [ ] README updated
* [ ] `.env.example` updated
* [ ] Build working
* [ ] Main flows tested
* [ ] Deploy documented
* [ ] No sensitive data committed
