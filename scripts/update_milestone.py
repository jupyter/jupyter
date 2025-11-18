#!/usr/bin/env python3
"""
Milestone Tracking Update Script

Update milestone status, completion dates, and metrics.

Usage:
    python scripts/update_milestone.py --milestone M1.1 --status completed
    python scripts/update_milestone.py --phase Phase1 --progress 0.45
    python scripts/update_milestone.py --day 21 --atomizations 21
"""

import json
import argparse
from datetime import datetime
from pathlib import Path


def load_milestones(path: Path = Path('milestones_tracking.json')):
    """Load milestone tracking JSON."""
    with open(path, 'r') as f:
        return json.load(f)


def save_milestones(data: dict, path: Path = Path('milestones_tracking.json')):
    """Save milestone tracking JSON."""
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✓ Updated: {path}")


def update_milestone_status(data: dict, milestone_id: str, status: str, notes: str = None):
    """Update a specific milestone's status."""
    for milestone in data['milestones']:
        if milestone['milestone_id'] == milestone_id:
            milestone['status'] = status
            if status == 'completed':
                milestone['completion_date'] = datetime.now().strftime('%Y-%m-%d')

            # Add update log
            log_entry = {
                'date': datetime.now().strftime('%Y-%m-%d'),
                'action': f"Milestone {milestone_id} status changed to {status}",
                'user': 'researcher',
                'notes': notes or ''
            }
            data['update_log'].append(log_entry)

            print(f"✓ Milestone {milestone_id} ({milestone['name']}) → {status}")
            return data

    print(f"✗ Milestone {milestone_id} not found")
    return data


def update_phase_completion(data: dict, phase: str, progress: float):
    """Update phase completion percentage."""
    metric_key = f"{phase.lower().replace(' ', '')}_completion"
    if metric_key in data['metrics']:
        data['metrics'][metric_key] = progress
        print(f"✓ {phase} completion → {progress*100:.1f}%")

    # Recalculate overall
    total = sum([
        data['metrics']['phase0_completion'],
        data['metrics']['phase1_completion'],
        data['metrics']['phase2_completion'],
        data['metrics']['phase3_completion'],
        data['metrics']['phase4_completion'],
        data['metrics']['phase5_completion']
    ])
    data['metrics']['overall_completion'] = total / 6
    print(f"✓ Overall completion → {data['metrics']['overall_completion']*100:.1f}%")

    return data


def update_day_counter(data: dict, day: int, atomizations: int):
    """Update current day and atomization count."""
    data['current_day'] = day
    data['metrics']['days_elapsed'] = day
    data['metrics']['atomizations_completed'] = atomizations

    print(f"✓ Current day → {day}")
    print(f"✓ Atomizations completed → {atomizations}")

    return data


def generate_progress_report(data: dict):
    """Generate a progress report."""
    print("\n" + "=" * 70)
    print("RECURSIVE RESEARCH FRAMEWORK - PROGRESS REPORT")
    print("=" * 70)

    print(f"\nProject: {data['project']}")
    print(f"Start Date: {data['start_date']}")
    print(f"Current Phase: {data['current_phase']}")
    print(f"Current Day: {data['current_day']}")

    print(f"\nOverall Completion: {data['metrics']['overall_completion']*100:.1f}%")
    print("\nPhase Completion:")
    for phase in ['phase0', 'phase1', 'phase2', 'phase3', 'phase4', 'phase5']:
        key = f"{phase}_completion"
        pct = data['metrics'][key] * 100
        bar_length = int(pct / 2)  # 50 chars max
        bar = "█" * bar_length + "░" * (50 - bar_length)
        print(f"  {phase.upper():8} {bar} {pct:5.1f}%")

    print(f"\nKey Metrics:")
    print(f"  Atomizations Completed: {data['metrics']['atomizations_completed']}")
    print(f"  AI Items Ingested: {data['metrics']['ai_items_ingested']}")
    print(f"  Papers Submitted: {data['metrics']['papers_submitted']}")
    print(f"  Conferences Attended: {data['metrics']['conferences_attended']}")

    # Recent milestones
    completed = [m for m in data['milestones'] if m['status'] == 'completed']
    print(f"\nCompleted Milestones: {len(completed)}/{len(data['milestones'])}")
    if completed:
        print("\nRecent Completions (last 5):")
        for milestone in completed[-5:]:
            print(f"  ✓ {milestone['milestone_id']}: {milestone['name']} ({milestone['completion_date']})")

    # Next milestones
    pending = [m for m in data['milestones'] if m['status'] in ['pending', 'not_started']]
    if pending:
        print(f"\nNext Milestones:")
        for milestone in pending[:3]:
            print(f"  ○ {milestone['milestone_id']}: {milestone['name']} (Target: {milestone['target_date']})")

    print("\n" + "=" * 70)


def main():
    parser = argparse.ArgumentParser(description='Update milestone tracking')
    parser.add_argument('--milestone', help='Milestone ID (e.g., M1.1)')
    parser.add_argument('--status', choices=['pending', 'in_progress', 'completed', 'blocked'],
                       help='New status')
    parser.add_argument('--notes', help='Additional notes')
    parser.add_argument('--phase', help='Phase to update (e.g., Phase1)')
    parser.add_argument('--progress', type=float, help='Completion percentage (0.0-1.0)')
    parser.add_argument('--day', type=int, help='Current day number')
    parser.add_argument('--atomizations', type=int, help='Total atomizations completed')
    parser.add_argument('--ai-items', type=int, help='Total AI items ingested')
    parser.add_argument('--report', action='store_true', help='Generate progress report')

    args = parser.parse_args()

    # Load data
    data = load_milestones()

    # Apply updates
    if args.milestone and args.status:
        data = update_milestone_status(data, args.milestone, args.status, args.notes)

    if args.phase and args.progress is not None:
        data = update_phase_completion(data, args.phase, args.progress)

    if args.day is not None:
        atomizations = args.atomizations if args.atomizations is not None else data['metrics']['atomizations_completed']
        data = update_day_counter(data, args.day, atomizations)

    if args.ai_items is not None:
        data['metrics']['ai_items_ingested'] = args.ai_items
        print(f"✓ AI items ingested → {args.ai_items}")

    # Save if any updates
    if any([args.milestone, args.phase, args.day, args.ai_items]):
        save_milestones(data)

    # Generate report
    if args.report or not any([args.milestone, args.phase, args.day, args.ai_items]):
        generate_progress_report(data)


if __name__ == '__main__':
    main()
