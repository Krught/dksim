from timeit import timeit
import random
import numpy

# test_1 = random.randint(220, 550)
# test_2 = int(random.random()*550) - int(random.random()*220)
# test_3 = numpy.random.randint(220, high=550, size=1000)
import_module = "import random"
import_module2 = "import numpy"

print(timeit('random.randint(220, 550)', setup=import_module, number=7000000))
print("\n")
print(timeit('int(random.random()*550) - int(random.random()*220)', setup=import_module, number=7000000))
print("\n")
print(timeit('numpy.random.randint(220, high=550, size=7000000)', setup=import_module2, number=1))


