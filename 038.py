# Level 038

#  -------------
#  -- FINED? -- 
#  -------------

import random

speed = random.randint(5, 200)
if speed <20:
    print(f"You were fined for not have a proper speed, your speed was {speed}km/h")
elif speed >80:
    print(f"You were fined for speeding, your speed was {speed}km/h")
elif speed <81:
    print(f"You weren't fined, WOW. your speed was {speed}km/h")