from utils import *

# Map building macros
# u -> up
# d -> down
# l -> left
# r -> right
# [u, d, l, r]

no_wall = [0, 0, 0, 0]

r_wall = [0, 0, 0, 1]

l_wall = [0, 0, 1, 0]

d_wall = [0, 1, 0, 0]

u_wall = [1, 0, 0, 0]

lr_wall = listBitwiseOr(l_wall, r_wall)

dr_wall = listBitwiseOr(d_wall, r_wall)

dl_wall = listBitwiseOr(d_wall, l_wall)

dlr_wall = listBitwiseOr(listBitwiseOr(d_wall, l_wall), r_wall)

ur_wall = listBitwiseOr(u_wall, r_wall)

ul_wall = listBitwiseOr(u_wall, l_wall)

ulr_wall = listBitwiseOr(listBitwiseOr(u_wall, l_wall), r_wall)

ud_wall = listBitwiseOr(u_wall, d_wall)

udr_wall = listBitwiseOr(listBitwiseOr(u_wall, d_wall), r_wall)

udl_wall = listBitwiseOr(listBitwiseOr(u_wall, d_wall), l_wall)

udlr_wall = listBitwiseOr(listBitwiseOr(
    u_wall, d_wall), listBitwiseOr(l_wall, r_wall))

# MAPS
start = [4, 0]
goal = [0, 4]

p1 = [[ulr_wall, ul_wall, u_wall, ur_wall, ulr_wall],
      [l_wall, no_wall, ur_wall, l_wall, dr_wall],
      [l_wall, r_wall, dl_wall, no_wall, ur_wall],
      [l_wall, no_wall, u_wall, no_wall, r_wall],
      [dl_wall, d_wall, d_wall, d_wall, dr_wall]]
p1SolSize = 4

p2 = [[udl_wall, ud_wall, ud_wall, u_wall, udr_wall],
      [ulr_wall, udl_wall, u_wall, no_wall, ur_wall],
      [l_wall, ur_wall, l_wall, r_wall, lr_wall],
      [l_wall, no_wall, d_wall, no_wall, dr_wall],
      [dl_wall, d_wall, ud_wall, d_wall, udr_wall]]
p2SolSize = 4

p3 = [[ul_wall, u_wall, u_wall, ur_wall, ulr_wall],
      [l_wall, r_wall, dl_wall, no_wall, r_wall],
      [l_wall, no_wall, udr_wall, l_wall, r_wall],
      [l_wall, no_wall, udr_wall, l_wall, r_wall],
      [dlr_wall, dl_wall, ud_wall, d_wall, dr_wall]]
p3SolSize = 5

p4 = [[ulr_wall, udl_wall, u_wall, ud_wall, udr_wall],
      [l_wall, ur_wall, dl_wall, u_wall, ur_wall],
      [lr_wall, d_wall, u_wall, r_wall, dlr_wall],
      [l_wall, u_wall, no_wall, no_wall, ur_wall],
      [dl_wall, d_wall, d_wall, d_wall, dr_wall]]
p4SolSize = 5

p5 = [[ulr_wall, ul_wall, u_wall, ur_wall, ulr_wall],
      [l_wall, d_wall, no_wall, d_wall, r_wall],
      [lr_wall, ulr_wall, l_wall, u_wall, dr_wall],
      [l_wall, r_wall, l_wall, no_wall, ur_wall],
      [dl_wall, dr_wall, dl_wall, d_wall, dr_wall]]
p5SolSize = 5

p6 = [[ul_wall, u_wall, ur_wall, ul_wall, udr_wall],
      [dlr_wall, lr_wall, dl_wall, d_wall, ur_wall],
      [ul_wall, no_wall, u_wall, u_wall, r_wall],
      [l_wall, no_wall, no_wall, no_wall, r_wall],
      [dl_wall, dr_wall, dl_wall, d_wall, dr_wall]]
p6SolSize = 5

p7 = [[ul_wall, u_wall, u_wall, ur_wall, ulr_wall],
      [l_wall, no_wall, dr_wall, lr_wall, lr_wall],
      [l_wall, dr_wall, ulr_wall, dl_wall, r_wall],
      [l_wall, ud_wall, dr_wall, udl_wall, r_wall],
      [dl_wall, ud_wall, udr_wall, udl_wall, dr_wall]]
p7SolSize = 6

p8 = [[ul_wall, ur_wall, ulr_wall, ulr_wall, ulr_wall],
      [dl_wall, no_wall, no_wall, no_wall, r_wall],
      [udl_wall, no_wall, dr_wall, l_wall, r_wall],
      [ulr_wall, dl_wall, ur_wall, dl_wall, r_wall],
      [dl_wall, ud_wall, d_wall, udr_wall, dlr_wall]]
p8SolSize = 6

p9 = [[ulr_wall, ul_wall, ud_wall, udr_wall, ulr_wall],
      [l_wall, r_wall, udl_wall, u_wall, dr_wall],
      [l_wall, r_wall, udl_wall, no_wall, udr_wall],
      [lr_wall, dl_wall, ur_wall, l_wall, ur_wall],
      [dl_wall, udr_wall, dl_wall, d_wall, dr_wall]]
p9SolSize = 6

p10 = [[ul_wall, u_wall, u_wall, ud_wall, ur_wall],
       [l_wall, d_wall, no_wall, ur_wall, dlr_wall],
       [l_wall, ur_wall, dlr_wall, dl_wall, ur_wall],
       [dl_wall, dr_wall, ul_wall, udr_wall, lr_wall],
       [udl_wall, ud_wall, d_wall, ud_wall, dr_wall]]
p10SolSize = 6

p11 = [[ulr_wall, ulr_wall, ul_wall, ur_wall, ulr_wall],
       [lr_wall, l_wall, d_wall, r_wall, lr_wall],
       [lr_wall, l_wall, ur_wall, l_wall, dr_wall],
       [l_wall, no_wall, dr_wall, dlr_wall, ulr_wall],
       [dl_wall, d_wall, ud_wall, ud_wall, dr_wall]]
p11SolSize = 6

p12 = [[ul_wall, u_wall, ur_wall, ul_wall, ur_wall],
       [lr_wall, dl_wall, d_wall, d_wall, r_wall],
       [l_wall, ur_wall, udl_wall, ud_wall, r_wall],
       [lr_wall, lr_wall, ulr_wall, ul_wall, r_wall],
       [dl_wall, dr_wall, dl_wall, dr_wall, dlr_wall]]
p12SolSize = 6

p13 = [[ulr_wall, ulr_wall, ulr_wall, ul_wall, udr_wall],
       [lr_wall, lr_wall, lr_wall, lr_wall, ulr_wall],
       [dl_wall, no_wall, r_wall, dl_wall, r_wall],
       [ul_wall, no_wall, no_wall, u_wall, r_wall],
       [dl_wall, d_wall, d_wall, d_wall, dr_wall]]
p13SolSize = 6

p14 = [[ul_wall, u_wall, u_wall, ud_wall, udr_wall],
       [dlr_wall, l_wall, r_wall, ul_wall, ur_wall],
       [ulr_wall, dlr_wall, dl_wall, r_wall, lr_wall],
       [lr_wall, ulr_wall, ulr_wall, l_wall, dr_wall],
       [dl_wall, d_wall, d_wall, d_wall, udr_wall]]
p14SolSize = 6

p15 = [[ul_wall, u_wall, ur_wall, ul_wall, ur_wall],
       [l_wall, dr_wall, l_wall, dr_wall, dlr_wall],
       [l_wall, ur_wall, dl_wall, ud_wall, udr_wall],
       [l_wall, no_wall, ud_wall, u_wall, udr_wall],
       [dl_wall, dr_wall, udl_wall, d_wall, udr_wall]]
p15SolSize = 6

p16 = [[udl_wall, ur_wall, ul_wall, ud_wall, udr_wall],
       [udl_wall, no_wall, no_wall, u_wall, udr_wall],
       [udl_wall, dr_wall, dl_wall, no_wall, ur_wall],
       [ul_wall, udr_wall, ulr_wall, l_wall, dr_wall],
       [dl_wall, ud_wall, d_wall, d_wall, udr_wall]]
p16SolSize = 7

p17 = [[ul_wall, u_wall, ud_wall, udr_wall, ulr_wall],
       [l_wall, d_wall, ud_wall, ur_wall, lr_wall],
       [l_wall, u_wall, ur_wall, l_wall, r_wall],
       [dl_wall, r_wall, lr_wall, dlr_wall, lr_wall],
       [udl_wall, d_wall, dr_wall, udl_wall, dr_wall]]
p17SolSize = 7

p18 = [[ulr_wall, ul_wall, udr_wall, ul_wall, udr_wall],
       [l_wall, no_wall, udr_wall, l_wall, ur_wall],
       [l_wall, no_wall, udr_wall, l_wall, dr_wall],
       [lr_wall, l_wall, ur_wall, l_wall, udr_wall],
       [dlr_wall, dl_wall, d_wall, d_wall, udr_wall]]
p18SolSize = 7

p19 = [[udl_wall, u_wall, u_wall, u_wall, udr_wall],
       [ul_wall, dr_wall, lr_wall, dlr_wall, ulr_wall],
       [lr_wall, udl_wall, dr_wall, ul_wall, r_wall],
       [dl_wall, ud_wall, u_wall, no_wall, dr_wall],
       [udl_wall, ud_wall, d_wall, d_wall, udr_wall]]
p19SolSize = 7

p20 = [[ul_wall, ud_wall, ur_wall, ulr_wall, ulr_wall],
       [l_wall, u_wall, r_wall, l_wall, dr_wall],
       [lr_wall, dlr_wall, lr_wall, l_wall, ur_wall],
       [l_wall, ur_wall, l_wall, d_wall, r_wall],
       [dl_wall, dr_wall, dl_wall, ud_wall, dr_wall]]
p20SolSize = 8
