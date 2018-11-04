
/* Problem 5
 * 2520 is the smallest number that can be divided by each of the numbers from
 * 1 to 10 without any remainder.
 *
 * What is the smallest positive number that is evenly-divisible by all of the
 * numbers from 1 to 20.
 *
 * https://projecteuler.net/problem=5
 */


import com.mchogardty.euler.Problem

object Problem5 extends Problem {
  lazy val factors = List[Long](11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

  def divisible(n: Long) = factors.forall(n % _ == 0)

  override def calculate = {
    def findNumber(n: Long): Long = divisible(n) match {
      case true => n
      case _ => findNumber(n + 20)
    }

    findNumber(2520)
  }
}
