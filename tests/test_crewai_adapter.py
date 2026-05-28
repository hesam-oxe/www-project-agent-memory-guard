"""Tests for CrewAI integration adapter."""
import pytest
from agent_memory_guard.integrations.crewai import GuardedMemory


def test_guarded_memory_imports():
    """Verify the adapter module loads without crewai installed."""
    assert GuardedMemory is not None