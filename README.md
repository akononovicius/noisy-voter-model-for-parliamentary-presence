# Noisy voter model for the parliamentary presence

Here you can find Python implementation of the noisy voter model for the
parliamentary presence. This variation of the noisy voter model differs from
the other variations in having two states: the true state (which corresponds to
intent) and the observed state (which corresponds to action).

This model was introduced in [1].

You are free to reuse and/or modify this code for your owm purposes. Proper
attribution (e.g., referencing [1]) would be quite welcome.

**Note** that here you find two implementations of the model, which are
identical except that `modelNumba.py` has an additional dependency `numba`.
If you have access to `numba`, you might want to use that implementation,
because it gives a preformance boost.

## Reference

1. A. Kononovicius. *Noisy voter model for the anomalous diffusion of parliamentary presence*.
Journal of Statistical Mechanics 2020: 063405 (2020).
doi: [10.1088/1742-5468/ab8c39](https://doi.org/10.1088/1742-5468/ab8c39).
[arXiv:2001.01479 [physics.soc-ph]](https://arxiv.org/abs/2001.01479).
