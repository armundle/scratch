sealed trait List[A]
case object Nil extends List[Nothing]
case class Cons[A](head: A, tail: List[A]) extends List[A]

object List{
  def drop[A](l: List[A], n: Int): List[A] = 
  {
    if (n <= 0) l
    else l match {
      case Nil => Nil
      case Cons(_, tail) => drop(tail, n-1)
    }
  }
}
