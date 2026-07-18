
import numpy as np
sicks= 9/14
healthies= 5/14

def compute_h(*probs):
    H = 0
    for p in probs:
        if p > 0:
            H -= p*np.log2(p)
    return H

Hs_root = compute_h(sicks, healthies)

#LAYER 1
# A

sick1= 3/6
healthy1= 3/6
sick0= 6/8
healthy0= 2/8
Hav = compute_h(sick1,healthy1) * 6/14 + compute_h(sick0,healthy0) * 8/14
info_gain1 = Hs_root - Hav
print(f'we earned {info_gain1} as gain using A')

# B
sick1= 3/7
healthy1= 4/7
sick0= 6/7
healthy0= 1/7
Hav = compute_h(sick1,healthy1) * 7/14 + compute_h(sick0,healthy0) * 7/14
info_gain2 = Hs_root - Hav
print(f'we earned {info_gain2} as gain using B')

# C
sick1= 3/4
healthy1= 1/4
sick2= 4/6
healthy2= 2/6
sick3= 2/4
healthy3= 2/4
Hav= compute_h(sick1,healthy1) * 4/14 + compute_h(sick2,healthy2) * 6/14 + compute_h(sick3,healthy3) * 4/14
info_gain3 = Hs_root - Hav
print(f'we earned {info_gain3} as gain using C')

# D
sick1= 2/6
healthy1= 4/6
sick2= 1
healthy2= 0
sick3= 3/4
healthy3= 1/4
Hav= compute_h(sick1,healthy1) * 6/14 + compute_h(sick2,healthy2) * 4/14 + compute_h(sick3,healthy3) * 4/14
info_gain4 = Hs_root - Hav
print(f'we earned {info_gain4} as gain using D')
print(f'best feature in the first depth is D\n')
print('The first group of d [D1]')

#LAYER 2
# A

Hs_D1 = compute_h(2/6, 4/6)
sick1= 1/3
healthy1= 2/3
sick0= 1/3
healthy0= 2/3
Hav = compute_h(sick1,healthy1) * 1/2 + compute_h(sick0,healthy0) * 1/2
info_gain1 = Hs_D1 - Hav
print(f'we earned {info_gain1} as gain using A')

# B
sick1= 0
healthy1= 1
sick0= 1
healthy0= 0
Hav = compute_h(sick1,healthy1) * 4/6 + compute_h(sick0,healthy0) * 2/6
info_gain2 = Hs_D1 - Hav
print(f'we earned {info_gain2} as gain using B')
print(f'we reached 1 so we stop, best feature in second depth is B')

print(f'\nthere are no healthy in subgroup [D2] so everyone in it are sick\n')
print('The third group of d [D3]')

# A

Hs_D3 = compute_h(3/4, 1/4)
sick1= 0
healthy1= 1
sick0= 1
healthy0= 0
Hav = compute_h(sick1,healthy1) * 1/4 + compute_h(sick0,healthy0) * 3/4
info_gain1 = Hs_D3 - Hav
print(f'we earned {info_gain1} as gain using A')
print(f'best feature in last depth is A')

print(f'\n the tree ===> D as first, B for [D1] , A for [D3] and C is not used\n')
print('we reached from 1 group to 3 subgroups[D]\nthe first group was divided to a healthy and a sick group [B]\nthe second group is all sick\nthe last group was divided to a healthy and a sick group [A]\nin total there are 5 total leaves and 3 depths(with root)')

print("""
Final Decision Tree

                     D
                /    |    \\
             D=1    D=2    D=3
              |      |      |
              B    Sick     A
            /   \\        /   \\
          B=0   B=1     A=0   A=1
          |      |       |      |
        Sick  Healthy   Sick  Healthy
""")