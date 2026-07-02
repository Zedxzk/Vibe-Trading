"""Offline driver: run backtest.runner.main without the optional swarm/MCP stack.

The only thing the swarm import provides to the backtest path is one extra
allowed run-root (swarm_runs_root). We stub it so the run-root whitelist still
works without pulling in fastmcp. Everything else is the real runner code.
"""
import sys
import types
from pathlib import Path

# Stub src.swarm + src.swarm.store so _default_run_roots() doesn't import fastmcp.
pkg = types.ModuleType("src.swarm")
pkg.__path__ = []  # mark as package
store = types.ModuleType("src.swarm.store")
store.swarm_runs_root = lambda: Path.home() / ".vibe-trading" / "shadow_runs"
sys.modules["src.swarm"] = pkg
sys.modules["src.swarm.store"] = store

from backtest.runner import main  # noqa: E402

main(Path(sys.argv[1]))
