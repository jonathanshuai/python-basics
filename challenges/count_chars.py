            s0 = max(s0_prev, s2_prev)
            s1 = max(s1_prev, s0_prev - prices[day])
            s2 = s1_prev + prices[day]
            
            s0_prev, s1_prev, s2_prev = s0, s1, s2