#!/usr/bin/env python3
"""
Interactive Task Manager with CLI - A Feature-Rich Demo
Features: Add tasks, mark complete, prioritize, search, stats, and data persistence
"""

import json
import os
from datetime import datetime
from typing import List, Dict

class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self) -> List[Dict]:
        """Load tasks from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, description: str, priority: str = 'medium'):
        """Add a new task"""
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'priority': priority,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"{Colors.GREEN}✓ Task added successfully!{Colors.END}")

    def list_tasks(self, filter_type='all'):
        """Display tasks with beautiful formatting"""
        if not self.tasks:
            print(f"{Colors.YELLOW}No tasks found. Add your first task!{Colors.END}")
            return

        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.HEADER}  YOUR TASKS{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'='*70}{Colors.END}\n")

        for task in self.tasks:
            if filter_type == 'completed' and not task['completed']:
                continue
            if filter_type == 'pending' and task['completed']:
                continue

            # Priority colors
            priority_colors = {
                'high': Colors.RED,
                'medium': Colors.YELLOW,
                'low': Colors.GREEN
            }
            priority_color = priority_colors.get(task['priority'], Colors.YELLOW)

            # Status symbol
            status = f"{Colors.GREEN}✓{Colors.END}" if task['completed'] else f"{Colors.RED}○{Colors.END}"

            print(f"{status} [{Colors.BOLD}{task['id']}{Colors.END}] {task['description']}")
            print(f"   {priority_color}Priority: {task['priority'].upper()}{Colors.END} | "
                  f"{Colors.CYAN}Created: {task['created_at']}{Colors.END}")
            print()

    def complete_task(self, task_id: int):
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"{Colors.GREEN}✓ Task #{task_id} marked as complete!{Colors.END}")
                return
        print(f"{Colors.RED}✗ Task #{task_id} not found!{Colors.END}")

    def delete_task(self, task_id: int):
        """Delete a task"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                self.tasks.pop(i)
                self.save_tasks()
                print(f"{Colors.GREEN}✓ Task #{task_id} deleted!{Colors.END}")
                return
        print(f"{Colors.RED}✗ Task #{task_id} not found!{Colors.END}")

    def search_tasks(self, keyword: str):
        """Search tasks by keyword"""
        results = [t for t in self.tasks if keyword.lower() in t['description'].lower()]
        if results:
            print(f"\n{Colors.CYAN}Found {len(results)} task(s) matching '{keyword}':{Colors.END}\n")
            for task in results:
                status = "✓" if task['completed'] else "○"
                print(f"{status} [{task['id']}] {task['description']}")
        else:
            print(f"{Colors.YELLOW}No tasks found matching '{keyword}'{Colors.END}")

    def show_stats(self):
        """Display task statistics"""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t['completed'])
        pending = total - completed

        print(f"\n{Colors.BOLD}{Colors.HEADER}📊 TASK STATISTICS{Colors.END}")
        print(f"{Colors.CYAN}{'─'*40}{Colors.END}")
        print(f"Total Tasks:      {Colors.BOLD}{total}{Colors.END}")
        print(f"Completed:        {Colors.GREEN}{completed}{Colors.END}")
        print(f"Pending:          {Colors.YELLOW}{pending}{Colors.END}")

        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"Completion Rate:  {Colors.BOLD}{completion_rate:.1f}%{Colors.END}")

def print_menu():
    """Display the main menu"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.HEADER}           🎯 INTERACTIVE TASK MANAGER 🎯{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}\n")
    print(f"{Colors.CYAN}[1]{Colors.END} ➕  Add New Task")
    print(f"{Colors.CYAN}[2]{Colors.END} 📋  List All Tasks")
    print(f"{Colors.CYAN}[3]{Colors.END} ✅  List Completed Tasks")
    print(f"{Colors.CYAN}[4]{Colors.END} ⏳  List Pending Tasks")
    print(f"{Colors.CYAN}[5]{Colors.END} ✓   Mark Task as Complete")
    print(f"{Colors.CYAN}[6]{Colors.END} 🗑️   Delete Task")
    print(f"{Colors.CYAN}[7]{Colors.END} 🔍  Search Tasks")
    print(f"{Colors.CYAN}[8]{Colors.END} 📊  Show Statistics")
    print(f"{Colors.CYAN}[9]{Colors.END} 🚪  Exit")
    print(f"{Colors.BLUE}{'─'*70}{Colors.END}")

def main():
    """Main program loop"""
    manager = TaskManager()

    print(f"\n{Colors.BOLD}{Colors.GREEN}Welcome to Interactive Task Manager!{Colors.END}")
    print(f"{Colors.CYAN}Manage your tasks with style 🚀{Colors.END}\n")

    while True:
        print_menu()
        choice = input(f"\n{Colors.BOLD}Enter your choice (1-9): {Colors.END}").strip()

        if choice == '1':
            description = input(f"{Colors.CYAN}Enter task description: {Colors.END}")
            priority = input(f"{Colors.CYAN}Priority (low/medium/high) [medium]: {Colors.END}").strip().lower()
            if priority not in ['low', 'medium', 'high']:
                priority = 'medium'
            manager.add_task(description, priority)

        elif choice == '2':
            manager.list_tasks('all')

        elif choice == '3':
            manager.list_tasks('completed')

        elif choice == '4':
            manager.list_tasks('pending')

        elif choice == '5':
            try:
                task_id = int(input(f"{Colors.CYAN}Enter task ID to complete: {Colors.END}"))
                manager.complete_task(task_id)
            except ValueError:
                print(f"{Colors.RED}Invalid task ID!{Colors.END}")

        elif choice == '6':
            try:
                task_id = int(input(f"{Colors.CYAN}Enter task ID to delete: {Colors.END}"))
                confirm = input(f"{Colors.YELLOW}Are you sure? (y/n): {Colors.END}").lower()
                if confirm == 'y':
                    manager.delete_task(task_id)
            except ValueError:
                print(f"{Colors.RED}Invalid task ID!{Colors.END}")

        elif choice == '7':
            keyword = input(f"{Colors.CYAN}Enter search keyword: {Colors.END}")
            manager.search_tasks(keyword)

        elif choice == '8':
            manager.show_stats()

        elif choice == '9':
            print(f"\n{Colors.GREEN}Thank you for using Task Manager! Goodbye! 👋{Colors.END}\n")
            break

        else:
            print(f"{Colors.RED}Invalid choice! Please select 1-9.{Colors.END}")

if __name__ == "__main__":
    main()
