
/* Problem 3
 * The prime factors of 13195 are 5, 7, 13 and 29.
 *
 * What is the largest prime factor of the number 600851475143?
 *
 * https://projecteuler.net/problem=3
 */


import com.mchogardty.euler.Problem

object Problem3 extends Problem {
  def lowestPrimeFactor(n: Long) = {
    def findFactor(current: Long): Long = n % current match {
      case 0 => current
      case _ => findFactor(current + 1)
    }

    findFactor(2)
  }

  def calculate = {
    def findLargest(m: Long): Long = lowestPrimeFactor(m) match {
      case `m` => m
      case x: Long => findLargest(m / x)
    }

    findLargest(600851475143L)
  }
}
