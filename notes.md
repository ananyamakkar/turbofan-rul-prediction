# Day 1 notes
- FD001: train (20631, 26), test (13096, 26), 100 engines each
- Train lifetimes: 128 to 362 cycles, mean ~206, median 199, right-skewed
- No missing values
- Constant columns to drop: setting_3, s_1, s_5, s_10, s_16, s_18, s_19 (s_6 nearly constant)
- Rising with degradation: s_2, s_3, s_4, s_11, s_15, s_17. Falling: s_7, s_12, s_20, s_21
- Signals are noisy, so use windows, not single rows
- Test engines are cut off early. true_rul + last_cycle gives the full life (~206 mean, same as train)
- Shortest test history is 31 cycles, so a window of ~30 fits all