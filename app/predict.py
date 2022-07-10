from app.core.settings import Settings

_settings = Settings()


def get_relative_difference(l1: list, l2: list) -> float:
    first_difference_l1_l2_ind_0 = abs(l1[0] - l2[0])
    if len(l1) != len(l2):
        return None

    d = []
    for i in range(len(l1)):
        d.append(
            abs(l1[i] - l2[i])
        )

    return (sum(d) / len(l1)) - first_difference_l1_l2_ind_0
