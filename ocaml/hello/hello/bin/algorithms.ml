open Z
open Big_int

(* Z.of_int convert int to big int,
   Z.pred subtract 1,
   Z.mul multiply  *)
let egyptian_fractions a b =
  let rec aux acc a b =
    if a = Z.of_int 1
    then List.rev (b :: acc)
    else (
      let biggest_unit_fraction = (b / a) + Z.of_int 1 in
      let a, b = (a * biggest_unit_fraction) - b, b * biggest_unit_fraction in
      aux (biggest_unit_fraction :: acc) a b)
  in
  aux [] a b
;;

let factorial n =
  let rec aux n acc =
    if Z.equal n Z.zero || Z.equal n Z.one then acc else aux (Z.pred n) (Z.mul acc n)
  in
  aux n Z.one
;;

let _ = egyptian_fractions (Z.of_int 5) (Z.of_int 121)
let _ = factorial (Z.of_int 50) |> Z.to_string |> print_endline
