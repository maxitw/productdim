from sage.all import Poset

"""The complete List of three irreducible posets. See Kelly "The 3-Irreducible Partially Ordered Sets"""

def A(n):
    d = {}
    m = n+3
    for i in range(1,m+1):
        lo = f"a{i}"
        hi1 = f"b{i}"
        hi2 = f"b{i % m + 1}"
        d[lo] = [hi1, hi2]
    return Poset(d)


def B():
    d = {"b1" : ["c1"],
         "a"  : ["c1","c2","c3"],
         "b2" : ["c2"],
         "b3" : ["c3"]}
    return Poset(d)


def C():
    d = {"a" : ["b1", "b2"],
         "b1"  : ["c1", "c2"],
         "b2" : ["c2", "c3"],
         "b3" : ["c2"]}
    return Poset(d)


def D():
    d = {"a" : ["b1", "b3"],
         "b1"  : ["c1"],
         "b2" : ["c1", "c2"],
         "b3" : ["c2"]}
    return Poset(d)


def E(n):
    d = {}

    d["c"] = ["d"]
    for i in range(1, n+3):
        d[f"a{i}"]=[f"b{i}", f"b{i+1}"]

    d["b1"] = []
    d[f"b{n+3}"] = []
    for i in range(2, n+3):
        d[f"b{i}"] = ["d"]

    return Poset(d)


def F(n):
    d = {}
    d["c"] = [f"a{i}" for i in range(1, n+2)] + ["d"]
    d["d"] = ["e"]

    for i in range(1, n+2):
        d[f"a{i}"]=[f"b{i}", f"b{i+1}"]
    d[f"a{n+2}"] = [f"b{n+2}"]

    for i in range(2, n+3):
        d[f"b{i}"] = ["e"]

    return Poset(d)


def G(n):
    d = {}

    for i in range(1, n+3):
        d[f"a{i}"] = [f"a{i+1}", f"b{i+1}"]
    d["a1"].append("c")

    for i in range(1, n+2):
        d[f"b{i}"] = [f"a{i+2}", f"b{i+1}"]
    d[f"b{n+2}"] = [f"b{n+3}"]

    d["c"] = [f"b{n+3}"]
    return Poset(d)

def H(n):
    d = {}

    for i in range(1, n+2):
        d[f"a{i}"] = [f"a{i+1}", f"b{i+2}"]

    for i in range(1, n+2):
        d[f"b{i}"] = [f"a{i+1}", f"b{i+1}"]
    d["b1"].append("c")
    d[f"b{n+2}"] = [f"b{n+3}"]

    d["d"] = [f"b{n+3}"]
    return Poset(d)


def CX1():
    d = {
            "a1" : ["b1", "c"],
            "a2" : ["b1", "b2", "b3"],
            "a3" : ["b2"],
            "b1" : [],
            "b2" : ["c"],
            "b3" : [],
            "c" : [],
    }
    return Poset(d)


def CX2():
    d = {
            "a1" : ["b1", "b2"],
            "a2" : ["b1", "b2", "b3", "c"],
            "a3" : ["b2", "b3"],
            "b1" : [],
            "b2" : [],
            "b3" : [],
            "c" : [],
    }
    return Poset(d)


def CX3():
    d = {
            "a1" : ["b1", "b2"],
            "a2" : ["b1", "b2", "b3"],
            "a3" : ["b2", "c"],
            "b1" : [],
            "b2" : [],
            "b3" : ["c"],
            "c" : [],
    }
    return Poset(d)


def EX1():
    d = {
                "a1" : ["b1", "b2", "b3"],
                "a2" : ["b2", "b3", "b4"],
                "a3" : ["b3"],
                "b1" : [],
                "b2" : [],
                "b3" : [],
                "b4" : [],
        }
    return Poset(d)


def EX2():
    d = {
            "a1" : ["b1", "b2"],
            "a2" : ["c", "b2", "b3"],
            "a3" : ["b2"],
            "b1" : ["c"],
            "b2" : [],
            "b3" : [],
            "c" : [],
    }
    return Poset(d)


def FX1():
    d = {
            "a1" : ["b1", "b2"],
            "a2" : ["b1", "b2", "b3"],
            "a3" : ["b2"],
            "b1" : [],
            "b2" : ["c"],
            "b3" : ["c"],
            "c" : [],
    }
    return Poset(d)


def FX2():
    d = {
            "a1" : ["b1", "b3", "c"],
            "a2" : ["b1", "b2", "b3"],
            "a3" : ["c", "b3"],
            "b1" : [],
            "b2" : ["c"],
            "b3" : [],
            "c" : [],
    }
    return Poset(d)


def I(n):
    d = {}

    for i in range(1, n+3):
        d[f"a{i}"] = [f"b{i}", f"b{i+1}"]

    for i in range(2, n+3):
        d[f"b{i}"] = ["d1", "d2"]
    d["b1"] = ["d1"]
    d[f"b{n+3}"] = ["d2"]

    d["c"] = ["d1", "d2"]
    return Poset(d)


def J(n):
    d = {}

    for i in range(1, n+3):
        d[f"a{i}"] = [f"a{i+1}", f"b{i+1}"]
    d["a1"].append("d")

    for i in range(1, n+2):
        d[f"b{i}"] = [f"a{i+2}", f"b{i+1}"]
    d[f"b{n+2}"] = [f"b{n+3}"]

    d["c"] = ["d", f"b{n+3}"]

    return Poset(d)

def famsN(n):
    result = [
        ("A", A(n)),
        ("B", B()),
        ("C", C()),
        ("D", D()),
        ("E", E(n)),
        ("F", F(n)),
        ("G", G(n)),
        ("H", H(n)),
        ("CX1", CX1()),
        ("CX2", CX2()),
        ("CX3", CX3()),
        ("EX1", EX1()),
        ("EX2", EX2()),
        ("FX1", FX1()),
        ("FX2", FX2()),
        ("I", I(n)),
        ("J", J(n)),
    ]
    return result
