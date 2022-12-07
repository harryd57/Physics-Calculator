def acceleration(uu: float, ve: float, te: float, ay: float):
    if uu == 0:
        return ve - (ay * te)
    if ve == 0:
        return uu + (ay * te)
    if te == 0:
        return (ve - uu) / ay
    if ay == 0:
        return (ve - uu) / te


def abs_pres(pa: float, pg: float, pat: float):
    if pa == 0:
        return pg + pat
    if pg == 0:
        return pa - pat
    if pat == 0:
        return pa - pg


def electric_field(el: float, fo: float, ch: float):
    if el == 0:
        return fo / ch
    if fo == 0:
        return el * ch
    if ch == 0:
        return fo / el


def force(fo: float, ma: float, ac: float):
    if fo == 0:
        return ma * ac
    if ma == 0:
        return fo / ac
    if ac == 0:
        return fo / ma


def mass(ma: float, de: float, vo: float):
    if ma == 0:
        return de * vo
    if de == 0:
        return ma / vo
    if vo == 0:
        return ma / de


def velocity(ve: float, inv: float, ac: float, ti: float):
    if ve == 0:
        return inv + (ac * ti)
    if inv == 0:
        return ve - (ac * ti)
    if ac == 0:
        return (ve - inv) / ti
    if ti == 0:
        return (ve - inv) / ac


def work(wo: float, fo: float, di: float):
    if wo == 0:
        return fo * di
    if fo == 0:
        return wo / di
    if di == 0:
        return wo / fo


def stress(st: float, fo: float, ar: float):
    if st == 0:
        return fo / ar
    if fo == 0:
        return st * ar
    if ar == 0:
        return fo / st


def power(po: float, wo: float, ti: float):
    if po == 0:
        return wo / ti
    if wo == 0:
        return po * ti
    if ti == 0:
        return wo / po
