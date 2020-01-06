# Noisy voter model for the parliamentary presence

Here you can find Python implementation of the noisy voter model for the
parliamentary presence. This variation of the noisy voter model differs from
the other variations in having two states: the true state (which corresponds to
intent) and the observed state (which corresponds to action).

This model was introduced in forthcoming article "Noisy voter model for the
anomalous diffusion of parliamentary presence" by A. Kononovicius (reference
to the paper will be added later).

You are free to reuse and/or modify this code for your owm purposes. Proper
attribution (e.g., referencing the article) would be quite welcome.

**Note** that here you find two implementations of the model, which are
identical except that `modelNumba.py` has an additional dependency `numba`.
If you have access to `numba`, you might want to use that implementation,
because it gives a preformance boost.
