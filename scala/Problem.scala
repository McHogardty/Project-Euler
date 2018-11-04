

package com.mchogardty.euler


abstract class Problem {
  def calculate: Any

  def main(args: Array[String]) = println(calculate)
}
