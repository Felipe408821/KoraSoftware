"""Backward-compatible import for the dental vertical agent.

The real orchestration logic now lives in app.agent.orchestrator so the
project can evolve beyond one large dental_agent.py file.
"""

from app.agent.orchestrator import DentalAgent
from app.agent.result import AgentResult

__all__ = ["DentalAgent", "AgentResult"]
