require File.expand_path('../math.rb', __FILE__)
require 'test/unit'

class MathTest < Test::Unit::TestCase
  def test_negative
    assert_equal(negative(5), -5)
    assert_equal(negative(0), 0)
  end

  def test_power
    assert_equal(power(2, 3), 8)
    assert_equal(power(5, 0), 1)
  end

  def test_absolute
    assert_equal(absolute(3), 3);
    assert_equal(absolute(-3), 3);
    assert_equal(absolute(0), 0);
  end

  def test_area_of_rectangle
    assert_equal(area_of_rectangle(2, 3), 6);
    assert_equal(area_of_rectangle(2, 0), 0);
    assert_equal(area_of_rectangle(0, 3), 0);
  end
end
