#!/usr/bin/env python3
"""
Show what the tasks look like in the interactive manager
"""

from task_manager_demo import TaskManager, Colors

print(f"\n{Colors.BOLD}{Colors.GREEN}Let me show you your current tasks!{Colors.END}\n")

# Load the demo tasks we created
manager = TaskManager('demo_tasks.json')

# Show all tasks
print(f"{Colors.YELLOW}Here's what you see when you choose option [2] - List All Tasks:{Colors.END}")
manager.list_tasks('all')

# Show statistics
print(f"\n{Colors.YELLOW}And here's what you see when you choose option [8] - Show Statistics:{Colors.END}")
manager.show_stats()

print(f"\n{Colors.BOLD}{Colors.CYAN}What you're seeing:{Colors.END}")
print(f"  ✓ = Completed task (done!)")
print(f"  ○ = Pending task (still to do)")
print(f"  Colors show priority: {Colors.RED}RED = high{Colors.END}, {Colors.YELLOW}YELLOW = medium{Colors.END}, {Colors.GREEN}GREEN = low{Colors.END}")
print(f"  Each task has an ID number [1], [2], etc.")
print(f"  You use these numbers to mark tasks complete or delete them\n")
