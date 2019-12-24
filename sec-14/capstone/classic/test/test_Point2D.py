from capstone.classic.point_2d import Point2D


class TestPoint2D:
    def test_init(self):
        p = Point2D(1, 2)
        assert p.x == 1
        assert p.y == 2

    def test_eq(self):
        p1 = Point2D(1, 2)
        p2 = Point2D(1, 2)

        assert p1 == p2

    def test_ne(self):
        p1 = Point2D(1, 2)
        p2 = Point2D(1, 3)

        assert not (p1 == p2)

    def test_lt(self):
        p1 = Point2D(1, 2)
        p2 = Point2D(2, 2)

        assert p1 < p2

    def test_le(self):
        p1 = Point2D(1, 2)
        p2 = Point2D(1, 2)

        assert p1 <= p2

    def test_gt(self):
        p1 = Point2D(2, 2)
        p2 = Point2D(1, 2)

        assert p1 > p2

    def test_ge(self):
        p1 = Point2D(1, 2)
        p2 = Point2D(1, 2)

        assert p1 >= p2

    def test_dist(self):
        p1 = Point2D(1, 2)
        p2 = Point2D(1, 3)

        assert p1.dist(p2) == 1

    def test_str(self):
        p = Point2D(1, 2)

        assert str(p) == "(1, 2)"
