package fpinscala.errorhandling.workbook

//sealed trait Option[+A]

trait Option[+A]{

case class Some[+A](get: A) extends Option[A]
case object None extends Option[Nothing]

  def map[B](f: A => B): Option[B] = 
    this match {
      case None => None
      case Some(a) => Some(f(a))
    }

  def flatMap[B](f: A => Option[B]): Option[B] =
    map(f) getOrElse None

  def getOrElse[B >: A](default: => B): B =
    this match {
      case None => default
      case Some(a) => a
    }

  def orElse[B >: A](ob: => Option[B]): Option[B] = 
    this map(Some(_)) getOrElse ob

  def filter(f: A => Boolean): Option[A] =
    this match {
      case Some(a) if f(a) => this
      case _ => None
    }

  def mean(xs: Seq[Double]): Option[Double] = 
    if (xs.isEmpty) None
    else Some(xs.sum / xs.length)

  def variance(xs: Seq[Double]): Option[Double] = 
  mean(xs) flatMap (m => mean(xs.map(x => math.pow(x - m, 2))))

  // what does the underscore in the function definition mean?
  def lift[A, B](f: A => B): Option[A] => Option[B] = _ map f

  // what is the order of operations here?
  def map2[A, B, C](a: Option[A], b: Option[B])(f: (A, B) => C): Option[C] =
    a flatMap(aa =>
        b map (bb =>
            f(aa, bb)))
}
