
/* Problem 7
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
 * that the 6th prime is 13.
 *
 * What is the 10001st prime number?
 *
 * https://projecteuler.net/problem=7
 */

import scala.collection.mutable.ListBuffer

import com.mchogardty.euler.Problem

object Problem7 extends Problem {
  lazy val maxNum = 105000
  lazy val target = 10001

  def multiples(n: Int): Set[Int] = (n to maxNum by n).toSet

  override def calculate = {
    def accumulatePrimes(
      n: Int,
      primes: ListBuffer[Int],
      sieve: Set[Int]
    ): Int = primes.length match {
      case `target` => primes.last
      case _ => {
        val isCoprime = sieve.contains(n)
        accumulatePrimes(
          n + 1,
          if (isCoprime) primes else primes :+ n,
          if (isCoprime) sieve else sieve ++ multiples(n)
        )
      }
    }

    accumulatePrimes(2, ListBuffer.empty, Set.empty)
  }
}
