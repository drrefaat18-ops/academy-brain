from swarm.digest_semantics import Digest, build_digest, check_coverage


def test_definition_is_captured():
    digest = build_digest("LEDs are light emitting diodes on the front of the board.")
    assert digest.key_terms == ["LEDs"]
    assert digest.definitions[0].text.startswith("light emitting diodes")


def test_descriptive_sentence_is_not_a_definition():
    # "Our names are shown scrolling..." describes what happens to names;
    # it does not define "Our names".
    digest = build_digest("Our names are shown scrolling across the display.")
    assert digest.key_terms == []


def test_contrast_is_not_a_definition():
    digest = build_digest("Computers are not just laptops and desktop PCs.")
    assert digest.key_terms == []


def test_mid_sentence_match_is_rejected():
    # Only a line-initial term counts, so an "is" buried in a clause
    # cannot manufacture a term out of the words before it.
    digest = build_digest("Use slide 11 to show a GIF if YouTube is blocked in your school.")
    assert digest.key_terms == []


def test_numbers_are_collected():
    digest = build_digest("Set the pause to 500 ms and run for 30 seconds.")
    assert "500 ms" in digest.numbers
    assert "30 seconds" in digest.numbers


def test_called_definition_uses_the_name_as_the_term():
    digest = build_digest("Information coming out of a computer is called an output.")
    assert digest.key_terms == ["output"]
    assert digest.definitions[0].text == "Information coming out of a computer"


def test_markdown_scaffolding_is_not_a_core_fact():
    source = """---
id: L1-s1
stage: digest
---
# L1-s1
## Slide 1: Recap
**Speaker notes:**
Computers are found in phones, consoles, televisions, and cars.
## Images
- `img-01.png` - from slide 1 (2780 bytes)
"""
    digest = build_digest(source)
    assert digest.core_facts == [
        "Computers are found in phones, consoles, televisions, and cars."
    ]


def test_navigation_and_facilitator_directions_are_not_core_facts():
    source = (
        "Optionally play video: https://example.com/demo\n"
        "Teacher: open completed code in editor\n"
        "What code did you use?\n"
        "A loop keeps the program running continuously.\n"
    )
    assert build_digest(source).core_facts == [
        "A loop keeps the program running continuously."
    ]


def test_coverage_detects_a_dropped_fact():
    source = (
        "An output is information leaving a computer.\n"
        "The output travels to the display grid.\n"
        "A separate battery powers the detachable controller board.\n"
    )
    digest = build_digest(source)
    downstream = "An output is information leaving a computer, shown on the display grid."

    report = check_coverage(digest, downstream)
    assert report.total_facts > 0
    assert any("battery" in fact for fact in report.missing_facts)


def test_coverage_tolerates_rephrasing():
    source = "An output is information leaving a computer.\n"
    digest = build_digest(source)
    # Same fact, different wording — must not be reported missing.
    downstream = "Information leaving a computer is what we call an output."

    report = check_coverage(digest, downstream)
    assert report.missing_facts == []


def test_coverage_matches_whole_words_not_substrings():
    digest = Digest(core_facts=["Motor speed controls movement."])
    report = check_coverage(digest, "A motorway speedometer is mounted here.")
    assert report.present_facts == 0
    assert report.missing_facts == ["Motor speed controls movement."]


def test_coverage_excludes_unmatchable_facts_from_denominator():
    digest = Digest(core_facts=["This is used.", "Battery power drives motors."])
    report = check_coverage(digest, "Battery power drives motors.")
    assert report.total_facts == 1
    assert report.present_facts == 1


def test_empty_source_reports_full_coverage():
    report = check_coverage(build_digest(""), "anything")
    assert report.coverage == 1.0
