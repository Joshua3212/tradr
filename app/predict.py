from app.core.settings import Settings

_settings = Settings()


def get_difference(l1: list, l2: list) -> float:
    if len(l1) != len(l2):
        return None

    d = []
    for i in range(len(l1)):
        d.append(
            abs(l1[i] - l2[i])
        )

    return sum(d) / len(l1)
