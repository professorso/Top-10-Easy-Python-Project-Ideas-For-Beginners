#!/usr/bin/env python3
"""
Quick script to show what the task manager menu looks like
"""

from task_manager_demo import Colors

print(f"\n{Colors.BOLD}{Colors.GREEN}Welcome to Interactive Task Manager!{Colors.END}")
print(f"{Colors.CYAN}This is what you'll see when you run the program:{Colors.END}\n")

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

print(f"\n{Colors.YELLOW}How it works:{Colors.END}")
print(f"  • You type a number (1-9) to choose what to do")
print(f"  • Press Enter after typing your choice")
print(f"  • The program will ask you for more details")
print(f"  • Your tasks are saved automatically!\n")

print(f"{Colors.GREEN}Example walkthrough:{Colors.END}")
print(f"  1. You type '1' to add a task")
print(f"  2. You type 'Buy groceries' as the task")
print(f"  3. You type 'high' for priority")
print(f"  4. Task is saved! ✓")
print(f"  5. You type '2' to see all your tasks")
print(f"  6. Your task appears in a colorful list!\n")
