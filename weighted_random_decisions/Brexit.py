# Leave        17,410,742	51.89%
# Remain       16,141,241	48.11%
# Valid votes  33,551,983	99.9225%
from random import randint


decision_num = randint(0, 33551983)
decision = "leave" if decision_num < 17410742 else "remain"

print("Britain will {} the European Union.".format(decision))
