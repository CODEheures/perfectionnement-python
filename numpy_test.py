import numpy as np

panda_papa = [100, 20, 5, 30]
k = 2

# test without pandas
panda_bb = [0, 0, 0, 0]
for index in range(len(panda_papa)):
    panda_bb[index] = panda_papa[index] / 2
print(panda_bb)

# test with numpy
panda_papa_np = np.array(panda_papa)
panda_bb_np = panda_papa_np / 2
print(panda_bb_np)

famille = [
    [100, 20, 5, 30], #papa
    [80, 18, 4, 25], #maman
    [40, 10, 2.5, 15], #bb
]

famille_np = np.array(famille)
#toute la famille
print(famille_np)
# pattes bb
print(famille_np[2,1])
#toutes les pattes
print(famille_np[:,1])
#sommes des pattes
print(sum(famille_np[:,1]))