@main def hello: Unit =
  println(egyptian_fractions(5, 121))
@main def h2 =
  break_control

def break_control =
  import scala.util.control.Breaks.{breakable, break}
  breakable {
    for i <- 1 to 5 do
      println(i)
      // break the for loop
      if i == 4 then break
  }

def egyptian_fractions(a_ : BigInt, b_ : BigInt): List[BigInt] =
  import scala.util.control.Breaks.{break, breakable}
  var ls = scala.collection.mutable.ListBuffer.empty[BigInt]
  var a: BigInt = a_
  var b: BigInt = b_
  if a == 1 then
    ls += b
    return ls.toList
  breakable {
    while true do
      val x = b / a + 1
      ls += x
      a = a * x - b
      b = b * x
      if a == 1 then
        ls += b
        break
  }
  ls.toList
