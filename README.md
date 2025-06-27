# Product Dimension

This is a collection of python scripts to calculate the order dimension of posets. They were used to give credence to a conjecture by Reuter [CITE] that $dim(P \times Q) \geq 4$, when $\dim(P), \dim(Q) \geq 3$.

## Dependencies

- A recent version of SageMath
- The kissat SAT solver. [https://github.com/arminbiere/kissat](https://github.com/arminbiere/kissat)

## Contents

- `threeirr.py` Contains SageMath Posets representing all 3-irreducible posets as described by Kelly.
- `dimension.py` Contains the `sat_dimension` function, which uses kissat to calculate the dimension of a SageMath Poset.
- `testdimension.py` Contains the scripts that were used to check small examples for Reuters conjecture. One may run this directly via `sage -python testdimension.py`.
