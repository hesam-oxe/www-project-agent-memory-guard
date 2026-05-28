"""Tests for LlamaIndex integration adapter."""
import pytest
from agent_memory_guard.integrations.llamaindex import GuardedChatStore


def test_guarded_chat_store_imports():
    """Verify the adapter module loads without llama_index installed."""
    assert GuardedChatStore is not None
    assert GuardedChatStore.class_name() == "GuardedChatStore"