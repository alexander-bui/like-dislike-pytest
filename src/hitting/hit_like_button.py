import enum


class LikeState(enum.Enum):
    empty = enum.auto()
    liked = enum.auto()
    disliked = enum.auto()


hit_like_transitions = {
    LikeState.empty: LikeState.liked,
    LikeState.liked: LikeState.empty,
    LikeState.disliked: LikeState.liked,
}

hit_dislike_transitions = {
    LikeState.empty: LikeState.disliked,
    LikeState.liked: LikeState.disliked,
    LikeState.disliked: LikeState.empty,
}


def hit_like(s: LikeState) -> LikeState:
    return hit_like_transitions[s]


def hit_dislike(s: LikeState) -> LikeState:
    return hit_dislike_transitions[s]


def hit_many(s: LikeState, hits: str) -> LikeState:
    for c in hits:
        c = c.lower()
        if c == 'l':
            s = hit_like(s)
        elif c == 'd':
            s = hit_dislike(s)
        else:
            raise ValueError('invalid hit')
    return s
