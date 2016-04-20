sealed trait List[A]
case object Nil extends List[Nothing]
case class Cons[A](head: A, tail: List[A]) extends List[A]

object List{
  def tail[A](l: List[A]): List[A] =
    l match {
      case Nil => Nil
      case Cons(_, tail) => tail
    }
}
