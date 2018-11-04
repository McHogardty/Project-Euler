
/* Problem 4
 * A palindromic number reads the same both ways. The largest palindrome made
 * from the product of two 2-digit numbers is 9009 = 91 x 99.
 *
 * Find the largest palindrome made from the product of two 3-digit numbers.
 *
 * https://projecteuler.net/problem=4
 */


import com.mchogardty.euler.Problem

object Problem4 extends Problem {
  def isPalindrome(word: String) = (word == word.reverse)

  def pairs(start: Int, end: Int) =
    (start to end by -1).toStream.flatMap(
      x => (start to x by -1).map(
        y => (x, y)
      )
    )

  def calculate = pairs(999, 100).map(x => x._1 * x._2).filter(x => isPalindrome(x.toString)).max
}
