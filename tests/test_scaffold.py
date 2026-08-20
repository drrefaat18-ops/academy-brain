def test_swarm_package_importable():
    import swarm
    assert swarm.__version__ == "0.1.0"


def test_office_libraries_available():
    import pptx
    import docx
    assert pptx is not None
    assert docx is not None
