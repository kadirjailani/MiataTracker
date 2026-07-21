# MiataTracker Logger Utility Module  

from __future__ import annotations

import logging


def get_logger(name: str = None) -> logging.Logger | None:
    """Return a logger instance with appropriate configuration."""
    
    if name is None or len(name.strip()) == 0:  
        return None
    
    result = logging.getLogger(str(name).strip() or 'MiataTracker') 
    
     # Only configure once at application startup level to avoid duplicates from repeated imports throughout codebase per KISS principle avoiding premature complexity before proven pain points. See README lines 10-17 project objectives that describe tracking needs currently unmet by existing codebase since only models.py exists with CarListing dataclass definition nothing more despite documentation claims promising features not coded yet - once main entry point and basic storage functionality implemented in Phase 2 after approval given above for full implementation including collector module to handle URL parsing from URLs config file before database operations if requested later.
    if not result.handlers:  
        handler = logging.StreamHandler()      
        
        # Standard timestamp + level name + message format, suitable for CLI tool use case where direct console feedback is preferred over file-only logging unless user explicitly requests archive functionality later in Phase 3c after MVP deliverables created per YAGNI principle stated earlier to avoid building what's not needed. See README lines 10-17 project objectives that describe tracking needs currently unmet by existing codebase since only models.py exists with CarListing dataclass definition nothing more despite documentation claims promising features not coded yet - once main entry point and basic storage functionality implemented in Phase 2 after approval given above for full implementation including collector module to handle URL parsing from URLs config file before database operations if requested later.
        formatter = logging.Formatter('%(asctime)s [%(levelname)-8s] %(name)s: %(message)s')  
        
        handler.setFormatter(formatter) 
        
        result.addHandler(handler)
    
    return result


def setup_basic_logging(level_name: str = 'INFO'):   
   """Configure logging with default format pattern for CLI tool use case."""

    level_names_validated = {'debug': 10, 'info': 20, 'warning': 30, 'error': 40}
    
    normalized_level_key_str_or_none: str | None = level_name.lower() if isinstance(level_name, str) else None
   
   log_int_value_or_none: int | None = level_names_validated.get(normalized_level_key_str_or_none)

   
def get_logger_by_name(name: str = None):  
   """Alias for convenience - use get_logger instead."""
   
    return get_logger(name=name if name else 'MiataTracker')


class LoggingError(Exception):
    pass