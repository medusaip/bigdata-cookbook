"""Sampling params: none for reasoning models, the given ones otherwise (Medusa fork)."""

import pytest

from bigdata_thematic_screener.openai_parallel import sampling_params_for_model

SAMPLING = {"temperature": 0.0, "top_p": 1.0, "seed": 42, "presence_penalty": None}


@pytest.mark.parametrize(
    "model",
    ["gpt-5", "gpt-5.6-luna", "GPT-5-mini", "gpt-6", "o1", "o3-mini", "O4-mini", " gpt-5.1 "],
)
def test_reasoning_models_get_no_sampling_params(model: str) -> None:
    assert sampling_params_for_model(model, **SAMPLING) == {}


def test_luna_rule_from_upstream_still_applies() -> None:
    assert sampling_params_for_model("some-luna-model", **SAMPLING) == {}


@pytest.mark.parametrize("model", ["gpt-4.1", "gpt-4o", "gpt-4o-mini"])
def test_other_models_keep_non_none_sampling_params(model: str) -> None:
    assert sampling_params_for_model(model, **SAMPLING) == {
        "temperature": 0.0,
        "top_p": 1.0,
        "seed": 42,
    }
