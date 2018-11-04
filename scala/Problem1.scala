
/* Problem 1
 * If we list all of the natural numbers below 10 that are multiples of 3 or 5
 * we get 3, 5, 6 and 9. The sum of these multiples is 23.
 *
 * Find the sum of all of the multiples of 3 or 5 below 1000.
 *
 * https://projecteuler.net/problem=1
 */


import com.mchogardty.euler.Problem

object Problem1 extends Problem {
  override def calculate = (1 until 1000).filter(x => (x % 3 == 0) || (x % 5 == 0)).sum
}
