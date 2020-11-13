from movement_2d import coordinates_in_direction, normalise_angle, angle_between


def test_normalise_angle():
    assert normalise_angle(0) == 0
    assert normalise_angle(359) == 359
    assert normalise_angle(360) == 0
    assert normalise_angle(360) == 0
    assert normalise_angle(364) == 4


def test_coordinates_in_direction():
    assert coordinates_in_direction(3.0, 3.0, 0) == (3.0, 4.0)
    assert coordinates_in_direction(3.0, 3.0, 90) == (4.0, 3.0)
    assert coordinates_in_direction(3.0, 3.0, 180) == (3.0, 2.0)
    assert coordinates_in_direction(3.0, 3.0, 270) == (2.0, 3.0)


def test_angle_between():
    assert angle_between(0, 0, 0, 0) == 0
    assert angle_between(4, 4, 4, 4) == 0
    assert angle_between(0, 0, 1, 1) == 45
    assert angle_between(1, 1, 2, 1) == 90
    assert angle_between(5, 6, 6, 5) == 135
    assert angle_between(3, 4, 3, 2) == 180
    assert angle_between(-2, -2, -3, -3) == 225
    assert angle_between(0, 8, -2, 8) == 270
    assert angle_between(10, 10, 10, 13) == 0
