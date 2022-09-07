from lib.lib_a.sample import sample
from lib.lib_a.array import (
    get_zero_array,
    get_zero_tf_array,
    get_zero_torch_array,
    get_test
)

if __name__ == "__main__":
    shape = [3, 3, 3]
    zero_np = get_zero_array(shape)
    zero_tf = get_zero_tf_array(shape)
    zero_torch = get_zero_torch_array(shape)
    sample()
    print(zero_np)
    print(zero_tf)
    print(zero_torch)
    print(get_test("hello"))
