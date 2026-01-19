"""Utility functions for shiny-octo-fishstick"""

import datetime
from typing import Optional, List, Dict

def format_date(date: datetime.datetime) -> str:
    """Format date to string.
    
    Args:
        date: Date object to format
        
    Returns:
        Formatted date string
    """
    if not date:
        return ''
    return date.strftime('%Y-%m-%d')

def validate_email(email: str) -> bool:
    """Validate email format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not email:
        return False
    import re
    pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return bool(re.match(pattern, email))

def safe_divide(a: float, b: float) -> Optional[float]:
    """Safely divide two numbers.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Result or None if division by zero
    """
    if b == 0:
        return None
    return a / b

def filter_valid_items(items: List[Dict]) -> List[Dict]:
    """Filter out invalid items from list."""
    return [item for item in items if item and isinstance(item, dict)]


"""
Shiny Octo Fishstick - Bug Fix
Shiny Octo Fishstick
"""

def safe_divide(a, b):
    """Safely divide two numbers with error handling"""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def parse_config(config_str):
    """Parse configuration string with improved error handling"""
    if not config_str:
        return {}
    
    try:
        import json
        return json.loads(config_str)
    except json.JSONDecodeError as e:
        print(f"Warning: Invalid JSON config: {e}")
        return {}


"""
Shiny Octo Fishstick - Feature Enhancement
Shiny Octo Fishstick
"""

def process_data(data):
    """Process and validate input data"""
    if not data:
        raise ValueError("Data cannot be empty")
    
    processed = []
    for item in data:
        if isinstance(item, dict):
            processed.append(validate_item(item))
        else:
            processed.append(str(item).strip())
    
    return processed

def validate_item(item):
    """Validate individual item structure"""
    required_fields = ['id', 'name']
    for field in required_fields:
        if field not in item:
            raise ValueError(f"Missing required field: {field}")
    return item

class DataProcessor:
    """Main data processing class"""
    
    def __init__(self, config=None):
        self.config = config or {}
        self.cache = {}
    
    def process(self, data):
        """Main processing method"""
        cache_key = hash(str(data))
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        result = process_data(data)
        self.cache[cache_key] = result
        return result
