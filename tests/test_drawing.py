from src.drawing import create_drawing


def test_create_drawing():
    drawing = create_drawing()

    assert len(drawing) == 3

    assert drawing[0].operation_type == "DRAW"
    assert drawing[1].operation_type == "TRAVEL"
    assert drawing[2].operation_type == "DRAW"

    for operation in drawing:
        assert len(operation.points) > 0

        for point in operation.points:
            assert len(point) == 2