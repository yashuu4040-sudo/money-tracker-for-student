# Project Notes

## Major Functional Modules
1. Income Management
2. Expense Management
3. Budget Management
4. Savings Management
5. Reports and Analytics
6. Data Storage
7. Validation

## Non-Functional Requirements
1. Usability - simple menu-driven interface.
2. Reliability - saved data is loaded when the program starts.
3. Maintainability - features are separated into Python files.
4. Error Handling - invalid numeric input and invalid choices are handled.

## Architecture
User -> main.py -> Feature Modules -> storage.py -> JSON data file

## Workflow
Start -> Load Data -> Display Menu -> User Choice -> Process Request -> Save Data -> Display Result -> Menu -> Exit

## Storage Design
A JSON file stores:
- transactions
- budget
- savings_goal

Each transaction contains:
- type
- amount
- category
- description

## Testing
The test file checks:
- positive amounts
- negative amounts
- valid menu choices
- invalid menu choices

## Future Enhancements
- Transaction dates
- Monthly filtering
- Graphs and charts
- Login/security
- Export to CSV
- Recurring expenses
