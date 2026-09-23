from src.drawing import create_drawing


def test_create_drawing():
    drawing = create_drawing()

    assert len(drawing) == 2

    for stroke in drawing:
        assert len(stroke) == 20

        for point in stroke:
            assert len(point) == 2