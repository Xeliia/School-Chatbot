from __future__ import annotations

import random
from typing import Iterable


FAQ_POOL = [
    {"id": "general-location", "question": "Where is SCHA located?", "category": "general"},
    {"id": "general-contact", "question": "What is the school's address and contact info?", "category": "contact"},
    {"id": "general-role", "question": "Who are you and what is your role here?", "category": "general"},
    {"id": "admissions-requirements", "question": "What are the requirements for Senior High School?", "category": "admissions"},
    {"id": "admissions-documents", "question": "What documents do I need for SHS admission?", "category": "admissions"},
    {"id": "admissions-online", "question": "How do I enroll online?", "category": "enrollment"},
    {"id": "admissions-process", "question": "Can you explain the online enrollment process?", "category": "enrollment"},
    {"id": "admissions-deadline", "question": "When is the enrollment period for SHS?", "category": "admissions"},
    {"id": "academic-strands", "question": "What are the SHS strands available?", "category": "academics"},
    {"id": "academic-subjects", "question": "What core subjects are included in Grade 11?", "category": "academics"},
    {"id": "academic-activities", "question": "Do students have extracurricular activities?", "category": "culture"},
    {"id": "schedule-registrar-hours", "question": "What are the registrar's office hours?", "category": "schedule"},
    {"id": "schedule-consultation", "question": "Can parents schedule an in-person consultation?", "category": "schedule"},
    {"id": "culture-values", "question": "What are the core values of the school?", "category": "culture"},
    {"id": "culture-identity", "question": "What does SCHA stand for in terms of core values?", "category": "culture"},
    {"id": "support-scholarship", "question": "Are there scholarships or financial aid options?", "category": "admissions"},
    {"id": "support-guidance", "question": "What student support services are available?", "category": "general"},
    {"id": "campus-facilities", "question": "What facilities are available for SHS students?", "category": "general"},
]


def _normalize_exclusions(exclude_ids: Iterable[str] | None) -> set[str]:
    if not exclude_ids:
        return set()
    return {item.strip() for item in exclude_ids if item and item.strip()}


def select_suggestions(
    pool: list[dict] | None = None,
    exclude_ids: Iterable[str] | None = None,
    limit: int = 4,
    rng_seed: int | None = None,
) -> list[dict]:
    """Return up to limit randomized FAQ suggestions excluding provided IDs."""
    source = FAQ_POOL if pool is None else pool
    exclusions = _normalize_exclusions(exclude_ids)

    safe_limit = max(3, min(4, int(limit)))
    candidates = [item for item in source if item.get("id") not in exclusions]

    if not candidates:
        candidates = source.copy()

    rng = random.Random(rng_seed)
    shuffled = candidates.copy()
    rng.shuffle(shuffled)

    # De-duplicate by ID just in case caller pool is malformed.
    seen: set[str] = set()
    unique: list[dict] = []
    for item in shuffled:
        item_id = item.get("id")
        if not item_id or item_id in seen:
            continue
        seen.add(item_id)
        unique.append(item)

    return unique[:safe_limit]
