# Library Management System

A comprehensive Python-based library management system developed using Git and GitHub for collaborative development and version control.

## 📋 Project Overview

This project demonstrates a complete team-based software development workflow using GitHub. It implements a Library Management System with modular components assigned to different team members.

### Project Learning Outcomes
- ✅ Understand Git and GitHub version control concepts
- ✅ Practice staging, committing, pushing, and pulling code
- ✅ Handle merge conflicts and synchronization issues
- ✅ Collaborate effectively through GitHub repositories
- ✅ Appreciate GitHub as a professional development tool

## 🏗️ System Architecture

The system is divided into **4 independent modules**, each developed by a separate team member:

### Module 1: User Management (`module-user` branch)
**Developer:** Member A

**Responsibilities:**
- User registration and account management
- User authentication and profile management
- User status tracking (active/inactive)
- Search and filter users

**Key Classes:**
- `User` - Represents a library member
- `UserManager` - Manages all user CRUD operations

**CRUD Operations:**
- **CREATE**: `create_user()` - Add new library members
- **READ**: `read_user()` - Retrieve user by ID
- **UPDATE**: `update_user()` - Modify user information
- **DELETE**: `delete_user()` - Remove users

---

### Module 2: Inventory Management (`module-inventory` branch)
**Developer:** Member B

**Responsibilities:**
- Book catalog management
- Book metadata handling (title, author, ISBN, category)
- Book status tracking (available, borrowed, damaged, etc.)
- Search and filter books by various criteria

**Key Classes:**
- `Book` - Represents a book in the inventory
- `BookManager` - Manages all book CRUD operations

**CRUD Operations:**
- **CREATE**: `create_book()` - Add new books to inventory
- **READ**: `read_book()` - Retrieve book by ID
- **UPDATE**: `update_book()` - Modify book information
- **DELETE**: `delete_book()` - Remove books from inventory

---

### Module 3: Transaction Management (`module-transactions` branch)
**Developer:** Member C

**Responsibilities:**
- Borrow/return operations tracking
- Due date management and fine calculation
- Overdue book tracking
- Transaction history maintenance
- Book renewal functionality

**Key Classes:**
- `Transaction` - Represents a borrow/return event
- `TransactionManager` - Manages all transaction operations

**CRUD Operations:**
- **CREATE**: `borrow_book()` - Record book borrowing
- **READ**: `read_transaction()` - Retrieve transaction details
- **UPDATE**: `update_transaction()` / `return_book()` - Process returns
- **DELETE**: N/A (transactions are historical records)

---

### Module 4: Admin & Reporting (`module-admin` branch)
**Developer:** Member D (Optional)

**Responsibilities:**
- System administration and configuration
- Generate comprehensive reports
- Monitor library operations
- Track performance metrics
- Fine and fee management

**Key Classes:**
- `AdminReport` - Generates various system reports
- `SystemConfiguration` - Manages system settings

**Reporting Features:**
- Inventory status report
- User statistics
- Borrowing activity report
- Overdue books report
- Popular books analysis
- User activity report
- Daily summary

---

## 📁 Project Structure

```
library-management-system/
├── main.py                 # Application entry point
├── user.py                 # User management module
├── book.py                 # Book inventory module
├── transaction.py          # Transaction/borrow-return module
├── admin.py                # Admin and reporting module
├── constants.py            # Configuration constants (to be added)
├── utils.py                # Helper utilities (to be added)
├── README.md               # This file
└── .gitignore              # Git ignore rules (to be added)
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Git
- GitHub account
- GitHub Desktop (optional, for GUI)

### Installation & Setup

#### For Team Lead (Repository Owner)
1. Initialize the repository (already done)
2. Invite team members as collaborators
3. Share the repository link

#### For Team Members

1. **Clone the repository**
   ```bash
   git clone https://github.com/shoaibsatti/library-management-system.git
   cd library-management-system
   ```

2. **Create your module branch**
   ```bash
   # For Member A (User Module)
   git checkout -b module-user
   
   # For Member B (Inventory Module)
   git checkout -b module-inventory
   
   # For Member C (Transaction Module)
   git checkout -b module-transactions
   
   # For Member D (Admin Module)
   git checkout -b module-admin
   ```

3. **Develop your module**
   - Implement CRUD operations
   - Add input validation
   - Include error handling
   - Write meaningful docstrings
   - Test your code

4. **Commit changes regularly**
   ```bash
   git add .
   git commit -m "feat(module-name): description of changes"
   ```
   
   **Commit message format:**
   ```
   feat(module): Add new feature
   fix(module): Fix bug description
   refactor(module): Refactor code
   docs(module): Update documentation
   test(module): Add tests
   ```

5. **Push to your branch**
   ```bash
   git push origin module-your-module-name
   ```

6. **Create a Pull Request**
   - Go to GitHub repository
   - Click "Pull Requests" tab
   - Click "New Pull Request"
   - Select your branch
   - Add description and wait for review
   - Merge after approval

---

## 💻 Running the System

### Basic Usage

```python
# Run the main application
python main.py
```

### Testing Individual Modules

```python
# Test User Module
from user import User, UserManager

manager = UserManager()
manager.create_user("John Doe", "john@example.com", "1234567890")
manager.list_all_users()

# Test Book Module
from book import Book, BookManager

book_mgr = BookManager()
book_mgr.create_book("Python 101", "John Doe", "123-456-789", "Programming")
book_mgr.list_all_books()

# Test Transaction Module
from transaction import TransactionManager

txn_mgr = TransactionManager()
txn_mgr.borrow_book(1, 1)
txn_mgr.list_all_transactions()

# Test Admin Module
from admin import AdminReport, SystemConfiguration

reports = AdminReport(user_manager, book_manager, transaction_manager)
reports.generate_all_reports()
```

---

## ✨ Key Features

### Input Validation
- ✅ Email format validation
- ✅ Phone number validation
- ✅ ISBN validation
- ✅ Name/title non-empty checks
- ✅ Quantity and ID validation

### Error Handling
- ✅ Try-except blocks for all operations
- ✅ User-friendly error messages
- ✅ Duplicate entry prevention
- ✅ Data consistency checks

### User Interface
- ✅ Console-based menu system
- ✅ Clear status indicators (✓, ❌, ⚠️)
- ✅ Formatted output tables
- ✅ Progress indicators

### Data Management
- ✅ In-memory data storage (can be extended to files/databases)
- ✅ Transaction history tracking
- ✅ Status tracking for all entities
- ✅ Timestamp recording

---

## 📊 Example Output

```
📚 Welcome to Library Management System

════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
📚 LIBRARY INVENTORY
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
ID: 1 | Title: Python 101 | Author: John Doe | ISBN: 978-0-123456-78-9 | Category: Programming | Year: 2023 | Qty: 5 | Status: Available
ID: 2 | Title: Web Development Basics | Author: Jane Smith | ISBN: 978-0-987654-32-1 | Category: Web | Year: 2022 | Qty: 3 | Status: Available
ID: 3 | Title: Data Science Guide | Author: Alice Johnson | ISBN: 978-1-234567-89-0 | Category: Data Science | Year: 2023 | Qty: 2 | Status: Available
ID: 4 | Title: Machine Learning | Author: Bob Wilson | ISBN: 978-1-567890-12-3 | Category: AI/ML | Year: 2024 | Qty: 1 | Status: Available
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

✓ Book 'Python 101' borrowed by user 1 successfully
  Due date: 2024-07-01

Available books: 3
  - Web Development Basics
  - Data Science Guide
  - Machine Learning

Borrowed books: 1
  - Python 101
```

---

## 🔄 Git Workflow

### Creating a Branch
```bash
git branch module-your-module-name
git checkout module-your-module-name
```

### Making Changes
```bash
# Create/modify files
git status              # See what changed
git add <filename>      # Stage specific files
git add .              # Stage all changes
git commit -m "message"
```

### Pushing Changes
```bash
git push origin module-your-module-name
```

### Creating a Pull Request
1. Go to GitHub repository
2. You'll see a prompt to create PR
3. Add description
4. Request review from team members
5. Merge after approval

### Syncing with Main
```bash
git fetch origin
git rebase origin/main
# Or
git merge origin/main
```

---

## 🤝 Collaboration Guidelines

### Code Review Process
1. Create Pull Request with clear description
2. Request review from team members
3. Address feedback and suggestions
4. Approve after 2+ reviews
5. Merge to main branch

### Handling Merge Conflicts
```bash
# Update your branch
git fetch origin
git rebase origin/main

# If conflicts occur:
# 1. Open conflicting files
# 2. Resolve conflicts manually
# 3. Mark as resolved
git add <resolved-file>
git rebase --continue
git push origin module-your-module-name
```

### Commit Message Standards
- Use present tense: "Add feature" not "Added feature"
- Be specific: "Add user email validation" not "Update code"
- Reference issues: "Fix #123"
- Use prefixes: feat, fix, refactor, docs, test

---

## 📝 Submission Checklist

- [ ] All 4 module branches created and developed
- [ ] Each module implements complete CRUD operations
- [ ] Input validation implemented in all modules
- [ ] Error handling with try-except blocks
- [ ] Meaningful commit history (at least 5 commits per module)
- [ ] Pull requests created for each module
- [ ] Code reviewed by team members
- [ ] Branches merged to main successfully
- [ ] README documentation complete
- [ ] System tested and working correctly
- [ ] Screenshots of commits and merges saved
- [ ] Repository link shared

---

## 🎓 Learning Resources

### Git & GitHub
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [GitHub Desktop Tutorial](https://docs.github.com/en/desktop)

### Python
- [Python Official Documentation](https://docs.python.org/3/)
- [Python Best Practices](https://pep8.org/)

### Version Control Best Practices
- Keep commits small and focused
- Write clear commit messages
- Review code before merging
- Use branches for features
- Sync frequently with main branch

---

## 📞 Support & Issues

If you encounter issues:
1. Check this README
2. Search existing GitHub issues
3. Create a new issue with details
4. Tag relevant team members
5. Discuss in team meetings

---

## 📜 License

This project is open source and available under the MIT License.

---

## 👥 Team Members

- **Member A (User Module):** [GitHub Username]
- **Member B (Inventory Module):** [GitHub Username]
- **Member C (Transaction Module):** [GitHub Username]
- **Member D (Admin Module):** [GitHub Username]

---

## 🎯 Outcomes Achieved

After completing this project, students will:
✅ Understand Git version control concepts
✅ Proficiently use GitHub for collaboration
✅ Stage, commit, push, and pull code effectively
✅ Handle merge conflicts and synchronization
✅ Implement complete CRUD operations
✅ Write validated and error-handled code
✅ Appreciate GitHub as a professional tool
✅ Work effectively in a team environment

---

**Last Updated:** 2026-06-15  
**Project Status:** 🚀 In Development  
**Repository:** https://github.com/shoaibsatti/library-management-system
