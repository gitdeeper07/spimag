#!/usr/bin/env python3
"""Fix import paths in all test files."""

import os
import glob

def fix_test_file(filepath):
    """Add proper import path handling to test file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Skip if already fixed
    if 'sys.path.insert' in content and 'try:' in content:
        return False
    
    # Find the import line
    lines = content.split('\n')
    new_lines = []
    
    # Add import handling after the initial imports
    import_section = True
    added = False
    
    for i, line in enumerate(lines):
        new_lines.append(line)
        
        if line.startswith('import unittest') or line.startswith('import sys'):
            continue
            
        if not added and 'import' in line and 'from' not in line and i > 5:
            # Add path handling
            new_lines.insert(-1, '')
            new_lines.insert(-1, '# إضافة المسار بشكل صحيح')
            new_lines.insert(-1, 'sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))')
            new_lines.insert(-1, '')
            new_lines.insert(-1, 'try:')
            new_lines.insert(-1, '    from src.smni.parameters.s_yield import SpinQuantumYield')
            new_lines.insert(-1, 'except ImportError:')
            new_lines.insert(-1, '    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))')
            new_lines.insert(-1, '    from smni.parameters.s_yield import SpinQuantumYield')
            new_lines.insert(-1, '')
            added = True
    
    if added:
        with open(filepath, 'w') as f:
            f.write('\n'.join(new_lines))
        return True
    
    return False

# Fix all test files
test_files = glob.glob('tests/unit/parameters/test_*.py')
fixed = 0
for tf in test_files:
    if fix_test_file(tf):
        print(f"✅ Fixed: {tf}")
        fixed += 1

print(f"\n✅ Fixed {fixed} test files")
