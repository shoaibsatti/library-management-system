"""Admin/Reporting Module for Library Management System."""

from datetime import datetime, timedelta
from typing import List, Dict, Tuple
from collections import defaultdict


class AdminReport:
    """Generates various reports for library administration."""
    
    def __init__(self, user_manager, book_manager, transaction_manager):
        """
        Initialize the admin report generator.
        
        Args:
            user_manager: UserManager instance
            book_manager: BookManager instance
            transaction_manager: TransactionManager instance
        """
        self.user_manager = user_manager
        self.book_manager = book_manager
        self.transaction_manager = transaction_manager
    
    def generate_inventory_report(self) -> Dict:
        """
        Generate inventory status report.
        
        Returns:
            Dict: Inventory statistics
        """
        total_books = len(self.book_manager.books)
        total_copies = sum(book.quantity for book in self.book_manager.books)
        available_books = len(self.book_manager.get_available_books())
        unavailable_books = len(self.book_manager.get_unavailable_books())
        
        report = {
            'total_unique_books': total_books,
            'total_copies': total_copies,
            'available_books': available_books,
            'unavailable_books': unavailable_books,
            'availability_rate': f"{(available_books / total_books * 100):.2f}%" if total_books > 0 else "0%"
        }
        
        print("\n" + "="*60)
        print("📦 INVENTORY REPORT")
        print("="*60)
        print(f"Total Unique Books: {report['total_unique_books']}")
        print(f"Total Copies: {report['total_copies']}")
        print(f"Available Books: {report['available_books']}")
        print(f"Unavailable Books: {report['unavailable_books']}")
        print(f"Availability Rate: {report['availability_rate']}")
        print("="*60 + "\n")
        
        return report
    
    def generate_user_statistics(self) -> Dict:
        """
        Generate user statistics report.
        
        Returns:
            Dict: User statistics
        """
        total_users = len(self.user_manager.users)
        active_users = len(self.user_manager.get_active_users())
        inactive_users = total_users - active_users
        
        # Count active borrowers
        active_borrowers = set()
        for txn in self.transaction_manager.transactions:
            if txn.status == "Active" and txn.return_date is None:
                active_borrowers.add(txn.user_id)
        
        report = {
            'total_users': total_users,
            'active_users': active_users,
            'inactive_users': inactive_users,
            'active_borrowers': len(active_borrowers)
        }
        
        print("\n" + "="*60)
        print("👥 USER STATISTICS")
        print("="*60)
        print(f"Total Users: {report['total_users']}")
        print(f"Active Users: {report['active_users']}")
        print(f"Inactive Users: {report['inactive_users']}")
        print(f"Active Borrowers: {report['active_borrowers']}")
        print("="*60 + "\n")
        
        return report
    
    def generate_borrowing_report(self) -> Dict:
        """
        Generate borrowing activity report.
        
        Returns:
            Dict: Borrowing statistics
        """
        total_transactions = len(self.transaction_manager.transactions)
        active_borrowings = len([t for t in self.transaction_manager.transactions 
                                if t.status == "Active" and t.return_date is None])
        completed_transactions = len([t for t in self.transaction_manager.transactions 
                                     if t.status == "Completed"])
        overdue_books = len(self.transaction_manager.get_overdue_books())
        
        report = {
            'total_transactions': total_transactions,
            'active_borrowings': active_borrowings,
            'completed_transactions': completed_transactions,
            'overdue_books': overdue_books
        }
        
        print("\n" + "="*60)
        print("📚 BORROWING REPORT")
        print("="*60)
        print(f"Total Transactions: {report['total_transactions']}")
        print(f"Active Borrowings: {report['active_borrowings']}")
        print(f"Completed Transactions: {report['completed_transactions']}")
        print(f"Overdue Books: {report['overdue_books']}")
        print("="*60 + "\n")
        
        return report
    
    def generate_overdue_report(self) -> List[Dict]:
        """
        Generate detailed overdue books report.
        
        Returns:
            List[Dict]: List of overdue book details
        """
        overdue_list = self.transaction_manager.get_overdue_books()
        
        report = []
        total_fine = 0
        
        print("\n" + "="*100)
        print("⚠️  OVERDUE BOOKS REPORT")
        print("="*100)
        print(f"{'User ID':<10} {'Book ID':<10} {'Days Overdue':<15} {'Due Date':<15} {'Fine Amount':<15}")
        print("-"*100)
        
        for txn in overdue_list:
            days_overdue = (datetime.now() - txn.due_date).days
            fine = txn.calculate_fine(self.transaction_manager.daily_fine_rate)
            total_fine += fine
            
            entry = {
                'user_id': txn.user_id,
                'book_id': txn.book_id,
                'days_overdue': days_overdue,
                'due_date': txn.due_date.strftime('%Y-%m-%d'),
                'fine_amount': fine
            }
            report.append(entry)
            
            print(f"{txn.user_id:<10} {txn.book_id:<10} {days_overdue:<15} {txn.due_date.strftime('%Y-%m-%d'):<15} ${fine:<14.2f}")
        
        print("-"*100)
        print(f"{'TOTAL OUTSTANDING FINES:':<50} ${total_fine:.2f}")
        print("="*100 + "\n")
        
        return report
    
    def generate_popular_books_report(self, limit: int = 5) -> List[Tuple]:
        """
        Generate report of most borrowed books.
        
        Args:
            limit (int): Number of top books to show
        
        Returns:
            List[Tuple]: List of (book_id, borrow_count) tuples
        """
        book_borrow_count = defaultdict(int)
        
        for txn in self.transaction_manager.transactions:
            book_borrow_count[txn.book_id] += 1
        
        # Sort by borrow count descending
        sorted_books = sorted(book_borrow_count.items(), key=lambda x: x[1], reverse=True)[:limit]
        
        print("\n" + "="*80)
        print("🔝 MOST BORROWED BOOKS REPORT")
        print("="*80)
        print(f"{'Rank':<10} {'Book ID':<15} {'Title':<35} {'Borrow Count':<15}")
        print("-"*80)
        
        for rank, (book_id, count) in enumerate(sorted_books, 1):
            book = self.book_manager.read_book(book_id)
            title = book.title if book else "Unknown"
            print(f"{rank:<10} {book_id:<15} {title:<35} {count:<15}")
        
        print("="*80 + "\n")
        
        return sorted_books
    
    def generate_user_activity_report(self, user_id: int) -> Dict:
        """
        Generate activity report for a specific user.
        
        Args:
            user_id (int): ID of the user
        
        Returns:
            Dict: User activity details
        """
        user = self.user_manager.read_user(user_id)
        if not user:
            print(f"❌ User {user_id} not found")
            return {}
        
        user_transactions = [t for t in self.transaction_manager.transactions 
                            if t.user_id == user_id]
        active_borrowings = [t for t in user_transactions 
                            if t.status == "Active" and t.return_date is None]
        completed_transactions = len([t for t in user_transactions if t.status == "Completed"])
        
        # Calculate total fines
        total_fines = sum(t.calculate_fine(self.transaction_manager.daily_fine_rate) 
                         for t in user_transactions)
        
        report = {
            'user_id': user_id,
            'user_name': user.name,
            'total_transactions': len(user_transactions),
            'active_borrowings': len(active_borrowings),
            'completed_transactions': completed_transactions,
            'total_fines': total_fines,
            'active_books': [t.book_id for t in active_borrowings]
        }
        
        print("\n" + "="*80)
        print(f"👤 USER ACTIVITY REPORT - {user.name} (ID: {user_id})")
        print("="*80)
        print(f"Total Transactions: {report['total_transactions']}")
        print(f"Active Borrowings: {report['active_borrowings']}")
        print(f"Completed Transactions: {report['completed_transactions']}")
        print(f"Total Fines Owed: ${report['total_fines']:.2f}")
        print(f"Currently Borrowed Books: {report['active_books']}")
        print("="*80 + "\n")
        
        return report
    
    def generate_daily_summary(self) -> Dict:
        """
        Generate daily operations summary.
        
        Returns:
            Dict: Daily summary statistics
        """
        today = datetime.now().date()
        today_start = datetime.combine(today, datetime.min.time())
        today_end = datetime.combine(today, datetime.max.time())
        
        today_transactions = [t for t in self.transaction_manager.transactions 
                             if today_start <= t.borrow_date <= today_end]
        
        borrows_today = len([t for t in today_transactions if t.transaction_type.value == "Borrow"])
        returns_today = len([t for t in today_transactions if t.transaction_type.value == "Return"])
        
        summary = {
            'date': today.strftime('%Y-%m-%d'),
            'total_books': len(self.book_manager.books),
            'available_books': len(self.book_manager.get_available_books()),
            'total_users': len(self.user_manager.users),
            'borrows_today': borrows_today,
            'returns_today': returns_today,
            'active_borrowings': len([t for t in self.transaction_manager.transactions 
                                     if t.status == "Active" and t.return_date is None]),
            'overdue_count': len(self.transaction_manager.get_overdue_books())
        }
        
        print("\n" + "="*60)
        print(f"📅 DAILY SUMMARY - {summary['date']}")
        print("="*60)
        print(f"Total Books in System: {summary['total_books']}")
        print(f"Available Copies: {summary['available_books']}")
        print(f"Total Users: {summary['total_users']}")
        print(f"Borrows Today: {summary['borrows_today']}")
        print(f"Returns Today: {summary['returns_today']}")
        print(f"Active Borrowings: {summary['active_borrowings']}")
        print(f"Overdue Books: {summary['overdue_count']}")
        print("="*60 + "\n")
        
        return summary
    
    def generate_all_reports(self):
        """Generate and display all reports."""
        print("\n" + "🔷"*30)
        print("GENERATING ALL SYSTEM REPORTS")
        print("🔷"*30)
        
        self.generate_daily_summary()
        self.generate_inventory_report()
        self.generate_user_statistics()
        self.generate_borrowing_report()
        self.generate_popular_books_report(limit=5)
        self.generate_overdue_report()
        
        print("\n" + "🔷"*30)
        print("REPORT GENERATION COMPLETED")
        print("🔷"*30 + "\n")


class SystemConfiguration:
    """Manages system-wide configuration settings."""
    
    def __init__(self):
        """Initialize system configuration."""
        self.settings = {
            'library_name': 'Central Library',
            'borrow_period_days': 14,
            'daily_fine_rate': 1.0,  # $ per day
            'max_books_per_user': 5,
            'enable_reservations': True,
            'enable_renewals': True
        }
    
    def get_setting(self, key: str):
        """Get a configuration setting."""
        if key in self.settings:
            return self.settings[key]
        print(f"❌ Setting '{key}' not found")
        return None
    
    def update_setting(self, key: str, value) -> bool:
        """Update a configuration setting."""
        if key not in self.settings:
            print(f"❌ Setting '{key}' not found")
            return False
        
        self.settings[key] = value
        print(f"✓ Setting '{key}' updated to {value}")
        return True
    
    def list_all_settings(self):
        """List all configuration settings."""
        print("\n" + "="*60)
        print("⚙️  SYSTEM CONFIGURATION")
        print("="*60)
        for key, value in self.settings.items():
            print(f"{key:<25} : {value}")
        print("="*60 + "\n")
