from Prog.imaginary_class import Image

if __name__ == "__main__":
    c1 = Image(1, 7)
    c2 = Image(8, 12)

    result_sum = c1.som(c2)
    result_sub = c1.subtr(c2)
    result_mult = c1.mult(c2)
    result_dis = c1.dis()

    print(f"Sum: {result_sum}")
    print(f"Sub: {result_sub}")
    print(f"mult: {result_mult}")
    print(f"dis: {result_dis}")