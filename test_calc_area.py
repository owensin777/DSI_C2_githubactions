from calc_area import calc_area_square
from pytest import approx, raises
def test_calc_area_square():
    

    input_numbers = [0,1,4,100]
    output_numbers = [0,1,16,10000]
    
    # option 1
    for input, output in zip(input_numbers, output_numbers):
        assert calc_area_square(input) == output
    # option 2
    for i in range(len(input_numbers)):
        this_input = input_numbers[i]
        this_exp_out = output_numbers[i]

        assert calc_area_square(this_input) == this_exp_out 


# def test_cal_area_negative():
#     assert calc_area_square(-4) == 15
    
def test_calc_area_circle():
    from calc_area import cal_area_circle
    assert cal_area_circle(2) == approx(12.5664, abs=1e-3)



def test_calc_area_circle_errors():
    from calc_area import cal_area_circle

    with raises(ValueError):
        cal_area_circle(-1)

    with raises(TypeError):
        cal_area_circle('This is not a number')


def test_calc_area_rectangle():
    from calc_area import calc_area_rectangle
    assert calc_area_rectangle(2, 2) == 4
    assert calc_area_rectangle(2, 1) == 2
    