import pytest
from hitting.hit_like_button import LikeState, hit_many


def test_empty_hit():
    assert hit_many(LikeState.empty, '') is LikeState.empty


def test_single_hits():
    assert hit_many(LikeState.empty, 'l') is LikeState.liked
    assert hit_many(LikeState.empty, 'd') is LikeState.disliked


@pytest.mark.parametrize("test_input,expected", [
    ('ll', LikeState.empty),
    ('dd', LikeState.empty),
    ('ld', LikeState.disliked),
    ('dl', LikeState.liked),
    ('ldd', LikeState.empty),
    ('lldd', LikeState.empty),
    ('ddl', LikeState.liked),
])
def test_multi_hits(test_input, expected):
    assert hit_many(LikeState.empty, test_input) is expected


@pytest.mark.skip(reason="regexes not supported yet")
def test_regex_hits():
    assert hit_many(LikeState.empty, '[ld]*ddl') is LikeState.liked


@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


def test_invalid_slap():
    with pytest.raises(ValueError):
        hit_many(LikeState.empty, 'x')


@pytest.mark.xfail
def test_db_slap(db_conn):
    db_conn.read_hits()
    assert ...


def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"


# def test_many_hits():
#     assert hit_many(LikeState.empty, 'll') is LikeState.empty
#     assert hit_many(LikeState.empty, 'dd') is LikeState.empty
#     assert hit_many(LikeState.empty, 'ld') is LikeState.disliked
#     assert hit_many(LikeState.empty, 'dl') is LikeState.liked
#     assert hit_many(LikeState.empty, 'ldd') is LikeState.empty
#     assert hit_many(LikeState.empty, 'lldd') is LikeState.empty
#     assert hit_many(LikeState.empty, 'ddl') is LikeState.liked
