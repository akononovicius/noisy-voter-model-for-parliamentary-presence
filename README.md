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

1. A. Kononovicius. *Noisy voter model for the anomalous diffusion of parliamentary presence*. [arXiv:2001.01479 [physics.soc-ph]](https://arxiv.org/abs/2001.01479).
