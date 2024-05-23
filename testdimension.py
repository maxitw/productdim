from dimension import sat_dimension
from threeirr import three_irr_posets

def delete(P, L):
    Ls = set(L)
    V = [x for x in P if not x in Ls]
    return P.subposet(V)

def is_3irreducible(P):
    n = sat_dimension(P)

    if n != 3:
        return False
    
    for x in P:
        nx = sat_dimension(delete(P,[x]))
        if nx == n:
            return False
    
    return True

def test_three_with_flip(n):
    fams = three_irr_posets(n)
    assert all(is_3irreducible(p) for (_, p) in fams)

    dfams = [(name, p.dual()) for (name, p) in fams]
    results = {}
    for (i,(name1, p1)) in enumerate(fams):
        for (name2, p2) in dfams[i:]:
            val = sat_dimension(p1.product(p2))
            results[f"{name1} x {name2}"] = val
    return results

def test_three(n):
    fams = three_irr_posets(n)
    assert all(is_3irreducible(p) for (_, p) in fams)

    results = {}
    for (i,(name1, p1)) in enumerate(fams):
        for (name2, p2) in fams[i:]:
            val = sat_dimension(p1.product(p2))
            results[f"{name1} x {name2}"] = val
    return results

if __name__ == "__main__":
    print(test_three(0))
