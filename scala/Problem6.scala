
/* Problem 6
 * The sum of the squares of the first ten natural numbers is 385.
 *
 * The square of the sum of the first ten natural numbers is 3025.
 *
 * Hence the difference between the sum of the squares of the first ten natural
 * numbers and the square of the sum is 2640.
 *
 * Find the difference between the sum of the squares of the first one hundred
 * natural numbers and the square of the sum.
 *
 * https://projecteuler.net/problem=6
 */


import com.mchogardty.euler.Problem

object Problem6 extends Problem {
  lazy val numbers = 1 to 100

  override def calculate = numbers.sum * numbers.sum - numbers.map(x => x * x).sum
}
