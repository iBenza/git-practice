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
end
