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
