# Medusa fork of the Thematic Screener CLI

This directory is a fork of BigData's Thematic Screener CLI, maintained by Medusa Investment Partners so the Medusa platform can install it as a regular Python package.

- **Upstream:** https://github.com/Bigdata-com/bigdata-cookbook, subdirectory `Thematic_Screener_CLI/`, MIT licence.
- **Forked from commit:** `a25bb6252e26c1898321bc7dc3b4fac1a0b736ae`.
- **Fork branch / tag:** `medusa` / `v0.1.0-medusa` on https://github.com/medusaip/bigdata-cookbook.
- **Install:** `pip install "bigdata-thematic-screener @ git+https://github.com/medusaip/bigdata-cookbook@v0.1.0-medusa#subdirectory=Thematic_Screener_CLI"`.

## The three changes

1. **Package rename `src` → `bigdata_thematic_screener`.** Upstream ships its code as a top-level package literally named `src`, which collides with any other project laid out the same way once installed into a shared environment. The directory was renamed with `git mv` and every `src.` import, monkeypatch target, script entry point (`screener`, `thematic-screener-mcp`), `packages.find` include and `python -m src.cli` snippet (README, notebooks) was rewritten. The distribution name became `bigdata-thematic-screener` to match.
2. **`snowflake-connector-python` dropped from the dependencies.** Only trending-theme discovery (`trending_themes.get_snowflake_connection`) reads Snowflake; the import moved inside that function and raises a clear `ImportError` naming the package when it is absent. Install it yourself if you use that path.
3. **No sampling params for reasoning models.** `openai_parallel.sampling_params_for_model` now returns `{}` for model names starting with `gpt-5`, `gpt-6`, `o1`, `o3` or `o4` (case-insensitive), because those models reject `temperature` and ignore `top_p`/`seed`/penalties. Upstream's `luna` rule is kept; other models still get the non-None params. Covered by `tests/test_openai_parallel_sampling.py`.

Upstream code is otherwise unmodified. The upstream MIT licence and copyright notices apply to this fork.
