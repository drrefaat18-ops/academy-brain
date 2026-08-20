from swarm import gates
from swarm.gates import boundary_check

CLEAN_STUDENT_TEXT = "الميكروبيت كمبيوتر صغير. جرب تضغط زرار A وشوف بيحصل إيه."
LEAKED_TIMING = "الميكروبيت كمبيوتر صغير.\n\nTrainer note: 5 minutes for this activity."
LEAKED_ANSWER = "شوف بيحصل إيه.\n\nExpected answer: the LED grid lights up."
LEAKED_ARABIC = "شوف بيحصل إيه.\n\nملاحظة للمدرب: اسأل الطلاب الأول."


def test_clean_student_text_passes():
    assert boundary_check.check(CLEAN_STUDENT_TEXT).verdict == gates.PASS


def test_detects_trainer_note():
    result = boundary_check.check(LEAKED_TIMING)
    assert result.verdict == gates.FAIL
    assert "trainer note" in result.evidence["matches"][0].lower()


def test_detects_expected_answer():
    assert boundary_check.check(LEAKED_ANSWER).verdict == gates.FAIL


def test_detects_arabic_trainer_marker():
    assert boundary_check.check(LEAKED_ARABIC).verdict == gates.FAIL


def test_detection_is_case_insensitive():
    assert boundary_check.check("EXPECTED ANSWER: yes").verdict == gates.FAIL


def test_empty_text_is_unverified():
    assert boundary_check.check("").verdict == gates.UNVERIFIED


def test_registered_under_expected_name():
    assert "trainer-boundary" in gates.REGISTRY
