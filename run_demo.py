#!/usr/bin/env python3
"""
Automated demo of the Task Manager to showcase features
"""

import time
import sys
from task_manager_demo import TaskManager, Colors, print_menu

def slow_print(text, delay=0.03):
    """Print text with a typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def demo_pause(message="", duration=1.5):
    """Pause between demo steps"""
    if message:
        print(f"\n{Colors.CYAN}{message}{Colors.END}")
    time.sleep(duration)

def main():
    print(f"\n{Colors.BOLD}{Colors.HEADER}{'='*70}")
    print("           🎯 TASK MANAGER - AUTOMATED DEMO 🎯")
    print(f"{'='*70}{Colors.END}\n")

    slow_print(f"{Colors.GREEN}Initializing Task Manager...{Colors.END}", 0.05)
    time.sleep(1)

    # Create task manager instance
    manager = TaskManager('demo_tasks.json')

    # Clear any existing tasks for clean demo
    manager.tasks = []
    manager.save_tasks()

    # Demo 1: Add tasks
    slow_print(f"\n{Colors.BOLD}{Colors.BLUE}📝 DEMO 1: Adding Tasks{Colors.END}", 0.05)
    demo_pause("Adding some sample tasks...", 1)

    tasks_to_add = [
        ("Build an awesome Python project", "high"),
        ("Review code documentation", "medium"),
        ("Write unit tests", "high"),
        ("Refactor legacy code", "low"),
        ("Deploy to production", "high")
    ]

    for desc, priority in tasks_to_add:
        print(f"\n{Colors.CYAN}➕ Adding: {Colors.END}{desc} [{priority} priority]")
        manager.add_task(desc, priority)
        time.sleep(0.8)

    # Demo 2: List all tasks
    demo_pause("\n" + "="*70, 1)
    slow_print(f"\n{Colors.BOLD}{Colors.BLUE}📋 DEMO 2: Listing All Tasks{Colors.END}", 0.05)
    demo_pause("", 1)
    manager.list_tasks('all')
    demo_pause("", 2)

    # Demo 3: Complete some tasks
    demo_pause("="*70, 1)
    slow_print(f"\n{Colors.BOLD}{Colors.BLUE}✅ DEMO 3: Completing Tasks{Colors.END}", 0.05)
    demo_pause("Marking some tasks as complete...", 1)

    for task_id in [1, 3, 5]:
        print(f"\n{Colors.CYAN}Completing task #{task_id}...{Colors.END}")
        manager.complete_task(task_id)
        time.sleep(0.8)

    # Demo 4: List pending tasks
    demo_pause("\n" + "="*70, 1)
    slow_print(f"\n{Colors.BOLD}{Colors.BLUE}⏳ DEMO 4: Showing Pending Tasks Only{Colors.END}", 0.05)
    demo_pause("", 1)
    manager.list_tasks('pending')
    demo_pause("", 2)

    # Demo 5: Search functionality
    demo_pause("="*70, 1)
    slow_print(f"\n{Colors.BOLD}{Colors.BLUE}🔍 DEMO 5: Searching Tasks{Colors.END}", 0.05)
    demo_pause("Searching for tasks containing 'code'...", 1)
    manager.search_tasks('code')
    demo_pause("", 2)

    # Demo 6: Statistics
    demo_pause("="*70, 1)
    slow_print(f"\n{Colors.BOLD}{Colors.BLUE}📊 DEMO 6: Task Statistics{Colors.END}", 0.05)
    demo_pause("", 1)
    manager.show_stats()
    demo_pause("", 2)

    # Demo 7: Delete a task
    demo_pause("="*70, 1)
    slow_print(f"\n{Colors.BOLD}{Colors.BLUE}🗑️  DEMO 7: Deleting a Task{Colors.END}", 0.05)
    demo_pause("Deleting task #4...", 1)
    manager.delete_task(4)
    demo_pause("", 1)

    print(f"\n{Colors.CYAN}Updated task list:{Colors.END}")
    manager.list_tasks('all')
    demo_pause("", 2)

    # Final stats
    demo_pause("="*70, 1)
    slow_print(f"\n{Colors.BOLD}{Colors.BLUE}📊 FINAL STATISTICS{Colors.END}", 0.05)
    demo_pause("", 1)
    manager.show_stats()

    # Conclusion
    print(f"\n{Colors.BOLD}{Colors.HEADER}{'='*70}")
    print("                    🎉 DEMO COMPLETE! 🎉")
    print(f"{'='*70}{Colors.END}\n")

    slow_print(f"{Colors.GREEN}✨ Features demonstrated:{Colors.END}", 0.05)
    print(f"  {Colors.CYAN}✓{Colors.END} Task creation with priority levels")
    print(f"  {Colors.CYAN}✓{Colors.END} Color-coded terminal output")
    print(f"  {Colors.CYAN}✓{Colors.END} Task completion tracking")
    print(f"  {Colors.CYAN}✓{Colors.END} Filtering (all/completed/pending)")
    print(f"  {Colors.CYAN}✓{Colors.END} Search functionality")
    print(f"  {Colors.CYAN}✓{Colors.END} Statistics and analytics")
    print(f"  {Colors.CYAN}✓{Colors.END} Data persistence (JSON)")
    print(f"  {Colors.CYAN}✓{Colors.END} Task deletion")

    print(f"\n{Colors.YELLOW}💡 To use the interactive version, run:{Colors.END}")
    print(f"   {Colors.BOLD}python task_manager_demo.py{Colors.END}\n")

    print(f"{Colors.GREEN}Demo data saved to: demo_tasks.json{Colors.END}\n")

if __name__ == "__main__":
    main()
