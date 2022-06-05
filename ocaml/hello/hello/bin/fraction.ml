module Math = struct
  let rec gcd a b =
    let a, b = abs a, abs b in
    match a, b with
    | a, 0 -> a
    | 0, b -> b
    | _ -> if a > b then gcd (a mod b) b else gcd a (b mod a)
  ;;
end

module type FractionType = sig
  type t

  val make : int -> int -> t
  val numerator : t -> int
  val denominator : t -> int
  val ( /+ ) : t -> t -> t
  val ( /- ) : t -> t -> t
  val ( /* ) : t -> t -> t
  val ( // ) : t -> t -> t
  val to_string : t -> string
end

module Fraction : FractionType = struct
  type t = int * int

  let rec make a b =
    if b < 0
    then make (-a) (-b)
    else (
      let g = Math.gcd a b in
      a / g, b / g)
  ;;

  let numerator (a, _) = a
  let denominator (_, b) = b

  let ( /+ ) a b =
    let na, da, nb, db = numerator a, denominator a, numerator b, denominator b in
    make ((na * db) + (da * nb)) (da * db)
  ;;

  let ( /- ) a b = a /+ make (-numerator b) (denominator b)

  let ( /* ) a b =
    let na, da, nb, db = numerator a, denominator a, numerator b, denominator b in
    make (na * nb) (da * db)
  ;;

  let ( // ) a b = a /* make (denominator b) (numerator b)
  let to_string a = string_of_int (numerator a) ^ "/" ^ string_of_int (denominator a)
end

module MyNumber = struct
  type number =
    | Real of float
    | Complex of (float * float)

  let add_num a b =
    match a, b with
    | Real a, Real b -> Real (a +. b)
    | Real a, Complex (bx, by) -> Complex (a +. bx, by)
    | Complex (ax, ay), Real b -> Complex (ax +. b, ay)
    | Complex (ax, ay), Complex (bx, by) -> Complex (ax +. bx, ay +. by)
  ;;

  let sub_num a b =
    match a, b with
    | Real a, Real b -> Real (a -. b)
    | Real a, Complex (bx, by) -> Complex (a -. bx, by)
    | Complex (ax, ay), Real b -> Complex (ax -. b, ay)
    | Complex (ax, ay), Complex (bx, by) -> Complex (ax -. bx, ay -. by)
  ;;

  let mul_num a b =
    match a, b with
    | Real a, Real b -> Real (a *. b)
    | Real a, Complex (bx, by) -> Complex (a *. bx, a *. by)
    | Complex (ax, ay), Real b -> Complex (ax *. b, ay)
    | Complex (ax, ay), Complex (bx, by) ->
      Complex ((ax *. bx) -. (ay *. by), (ax *. by) +. (ay *. bx))
  ;;

  let div_num a b =
    match a, b with
    | Real a, Real b -> Real (a /. b)
    | Real a, Complex (bx, by) ->
      Complex
        ( a *. bx /. ((bx ** 2.0) +. (by ** 2.0))
        , -.a *. by /. ((bx ** 2.0) +. (by ** 2.0)) )
    | Complex (ax, ay), Real b -> Complex (ax /. b, ay /. b)
    | Complex (ax, ay), Complex (bx, by) ->
      let n = (bx ** 2.0) +. (by ** 2.0) in
      Complex (((ax *. bx) +. (ay *. by)) /. n, ((ay *. bx) -. (ax *. by)) /. n)
  ;;

  let conj a =
    match a with
    | Real a -> Real a
    | Complex (ax, ay) -> Complex (ax, -.ay)
  ;;

  let real a =
    match a with
    | Real a -> a
    | Complex (ax, ay) -> ax
  ;;

  let imag a =
    match a with
    | Real a -> 0.0
    | Complex (ax, ay) -> ay
  ;;

  div_num (Complex (2.0, 3.0)) (Complex (3.0, 2.0))
end
