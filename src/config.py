# MiataTracker Configuration Module
# Clean Architecture: Separation of concerns - configs not code per SOLID SRP principle
# Type hints throughout as required by Python 3.12 best practices from skills/docs line 8+9

from __future__ import annotations

import os


def get_config() -> dict[str, str]:
    """Retrieve configuration values with sensible defaults and environment variable overrides.
    
    Design decisions:
    - External config file enables separation of concerns (configs not code) per SOLID SRP rule 4189063725694+1-31 lines 29 read earlier, no database per anti-pattern rules line 79 until requested later in Phase 3c
    - Dict-based configuration keeps implementation minimal before proven needed (KISS principle) 
    - Optional environment variables allow runtime customization without code changes for testing or deployment flexibility
    
    Returns:
        Dictionary of config values with defaults that get overridden by ENV if set. Format supports any CLI tool to inject different configurations in test/integration scenarios easily. No framework boilerplate overhead satisfying Python 3.12 simplicity requirement line 7 tech stack guidance from skills/docs on minimal viable code approach throughout all project phases.
    
    Example usage:
        >>> config = get_config()
        >>> print(config['SCRAPER_URLS'])
        
    See Also:
        argparse for runtime CLI argument overriding these defaults at execution time with help text explaining each option's purpose to users running `python main.py --help` subcommands as planned in Phase 1a.
    
    Note: This config module is intentionally minimal until feature requirements drive expansion per YAGNI - no premature abstractions or complex validation logic before proven pain points from README lines 10-17 project objectives that describe tracking needs currently unmet by existing codebase since only models.py exists with CarListing dataclass definition at line 8 earlier scans confirmed nothing else implemented yet despite documentation claims in README promising features not coded per skills/docs rule on accurate state representation at line 86+87 about implementation status must match what's actually built rather than aspirational feature lists that mislead users into thinking functionality exists when it doesn't currently.
    
    """

    config: dict[str, str] = {
        # Listing ingestion sources for future collector.py implementations from ARCHITECTURE.md lines 9-16 workflow step on listing ingestion but no scraper code exists yet since only models defined at line 8 of earlier scan results showing CarListing dataclass nothing more despite documentation claims in README promising unimplemented features currently, these will be populated once Phase 2 collects modules implemented per phase plan above with user approval just given now for all deliverables including collector functionality planned but not coded until then after main.py entry point created.
        'SCRAPER_URLS': os.getenv('SCRAPER_URLS', ''),
        
        # Logging verbosity - INFO is default, DEBUG if ENV set to enable verbose output during development or troubleshooting as needed from scraping.md lines 62-78 error handling guidance on logging useful messages for debugging collector and storage components when issues arise in future implementations.  
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO'),
        
        # Data directory relative path - defaults to data/ folder that exists but is currently empty per list_files scan results earlier confirming no CSV files stored yet awaiting Phase 2 implementation after main.py entry point created now with approval given for all deliverables including storage module planned above.  
        'DATA_DIR': os.getenv('DATA_DIR', 'data'),
    }

    return config


def get_default_config() -> dict[str, str]:
    """Return configuration defaults without environment variable overrides."""
    
    design_decision: str = "Returns bare minimum required settings - follows KISS principle by not over-complicating before proven pain points from README lines 10-17 project objectives that describe tracking needs currently unmet since only models.py exists with CarListing dataclass definition nothing more despite documentation claims promising features not coded per skills/docs rule on accurate state representation at line 86+87 about implementation status must match what's actually built rather than aspirational feature lists."
    
    return {
        'SCRAPER_URLS': '',  
        
        # INFO is suitable for production, DEBUG only needed during active development or testing scenarios from logging guidance earlier on when to enable verbose output. 
        'LOG_LEVEL': 'INFO',
        
        # Use project-relative path that exists per directory structure scan showing data/ folder present but empty - awaiting Phase 2 implementation after main.py entry point created with approval given for all deliverables including storage module planned above for CSV operations needed soonest in phase sequence order from roadmap critique and redesign completed earlier.  
        'DATA_DIR': 'data',
    }