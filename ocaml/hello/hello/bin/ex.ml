open Unix

let _ = print_endline "from hello"

(* the trim of string is whether "" *)
let do_str s = String.trim s <> ""
let () = do_str "arm" |> string_of_bool |> print_endline

(* deal with unix command *)
let cmd = Sys.command "ls"

(* get the result of in_channel that is from Unix.open_process_in or open a
   file return as string list *)
let lines_of_channel ch =
  let rec line_of_channel acc =
    let line =
      try In_channel.input_line ch with
      | End_of_file -> None
    in
    match line with
    | Some l -> line_of_channel (l :: acc)
    | None -> acc
  in
  List.rev (line_of_channel [])
;;

let lines_of_channel2 ch =
  let rec line_of_channel acc =
    let line = In_channel.input_line ch in
    match line with
    | Some l -> line_of_channel (l :: acc)
    | None -> acc
  in
  List.rev (line_of_channel [])
;;

let read_file filename =
  let f = open_in filename in
  lines_of_channel2 f
;;

let string_of_channel ch = really_input_string ch (in_channel_length ch)

(* get the output of execution of command *)
let run_command cmd =
  let ps = Unix.open_process_in cmd in
  let out = string_of_channel ps in
  let status = Unix.close_process_in ps in
  match status with
  | Unix.WEXITED 0 -> out
  | _ -> Printf.ksprintf failwith "error: %s\n" cmd
;;

let run_command2 cmd =
  let ps = Unix.open_process_in cmd in
  let out = lines_of_channel ps in
  In_channel.close ps;
  out
;;

let read_file_as_lines file_name =
  let f = open_in file_name in
  let lines = lines_of_channel f in
  close_in f;
  lines
;;

let read_file_as_lines2 file_name =
  let f = open_in file_name in
  let rec read_loop acc =
    try
      let line = In_channel.input_line f in
      match line with
      | Some l -> read_loop (l :: acc)
      | None -> List.rev acc
    with
    | End_of_file ->
      In_channel.close f;
      acc
  in
  read_loop []
;;

let read_file_as_lines3 file_name =
  let f = open_in file_name in
  let rec read_loop acc =
    let line =
      try Some (input_line f) with
      | End_of_file ->
        close_in f;
        None
    in
    match line with
    | Some l -> read_loop (l :: acc)
    | None -> List.rev acc
  in
  read_loop []
;;

let read_file_as_lines4 file_name =
  (* open file for reading *)
  let f = open_in file_name in
  let rec read_loop () =
    try
      let next = input_line f in
      next :: read_loop ()
    with
    | End_of_file ->
      close_in f;
      []
  in
  read_loop ()
;;

let arch =
  match Sys.os_type with
  | "Unix" -> run_command "uname -m"
  | _ -> failwith "windows and other are not supported"
;;

let os =
  match Sys.os_type with
  | "Unix" ->
    (match run_command "uname -s" with
    | "Linux" -> "linux"
    | "Darwin" -> "macOS"
    | s -> s)
  | _ -> failwith "windows and other are not supported"
;;

let os_release file_path =
  let default_path_ls = [ "/etc/os-release"; "/usr/lib/os-release" ] in
  let file_path_ls =
    if Sys.file_exists file_path then file_path :: default_path_ls else default_path_ls
  in
  let parse_os_release_files =
    lazy
      (List.find Sys.file_exists file_path_ls
      |> read_file_as_lines2
      |> List.map (fun s ->
             Scanf.sscanf s "%s@= %s@!" (fun x v ->
                 ( x
                 , try Scanf.sscanf v "\"%s@\"" (fun s -> s) with
                   | Scanf.Scan_failure _ -> v ))))
  in
  fun f -> List.assoc f (Lazy.force parse_os_release_files)
;;

let os_release2 file_path =
  let default_path_ls = [ "/etc/os-release"; "/usr/lib/os-release" ] in
  let file_path_ls =
    if Sys.file_exists file_path then file_path :: default_path_ls else default_path_ls
  in
  let parse_os_release_files =
    lazy
      (List.find Sys.file_exists file_path_ls
      |> read_file_as_lines2
      |> List.map (fun s ->
             try Scanf.sscanf s "%s@= \"%s@\"" (fun k v -> k, v) with
             | Scanf.Scan_failure _ -> Scanf.sscanf s "%s@= %s@!" (fun k v -> k, v)))
  in
  fun key -> List.assoc key (Lazy.force parse_os_release_files)
;;

let os_release file_path =
  let default_path_ls = [ "/etc/os-release"; "/usr/lib/os-release" ] in
  let file_path_ls =
    if Sys.file_exists file_path then file_path :: default_path_ls else default_path_ls
  in
  let parse_os_release_files =
    lazy
      (List.find Sys.file_exists file_path_ls
      |> read_file_as_lines2
      |> List.map (fun s ->
             String.split_on_char '=' s
             |> Array.of_list
             |> fun arr ->
             (* Str.(global_replace (regexp "\"") "" arr.(1)) *)
             arr.(0), Str.global_replace (Str.regexp "\"") "" arr.(1)))
  in
  fun key -> List.assoc key (Lazy.force parse_os_release_files)
;;

let () = print_endline "test"
let () = os_release "/Users/felix/fedora35.txt" "NAME" |> print_endline

let test_os_release s =
  Scanf.sscanf s "%s=%s" (fun x v ->
      ( x
      , try Scanf.sscanf v "\"%s\"" (fun s -> s) with
        | Scanf.Scan_failure _ -> v ))
;;

let parse_integers s =
  let stream = Scanf.Scanning.from_string s in
  let rec parse acc =
    (* ' ' or '\n' are special character. a space inside the format string
       matches any number of tab, space, line feed and carriage return
       characters *)
    try parse (Scanf.bscanf stream "%d " (fun x -> x :: acc)) with
    | Scanf.Scan_failure _ -> acc
    | End_of_file -> acc
  in
  Array.of_list (List.rev (parse []))
;;

let parse_str s =
  (* @ is scanning indication *)
  Scanf.sscanf s "%s@=%s@!" (fun k v -> k, v)
;;

let string_split str ch =
  let rec aux pos =
    try
      let i = String.index_from str pos ch in
      String.sub str pos (i - pos) :: aux (succ i)
    with
    | Not_found | Invalid_argument _ ->
      let l = String.length str in
      [ String.sub str pos (l - pos) ]
  in
  aux 0
;;

let str_split str ch = String.split_on_char ch str

let str_split str ch =
  let open Core in
  String.split_on_chars str ~on:ch
;;

(* x |> f |> g is exactly equivalent to g (f (x)). g @@ f @@ x is exactly
   equivalent to g (f (x)). *)
let dir_is_empty dir = Array.length (Sys.readdir dir) = 0
let dir = "/Users/felix/test-ocaml"

let files_in_current_dir dir =
  Sys.readdir dir
  |> Array.to_list
  |> List.filter (fun x -> not (Sys.is_directory x))
  |> List.map (Filename.concat dir)
;;

open Unix

let files_in_dir dir =
  let rec aux result = function
    | f :: fs when Sys.is_directory f ->
      Sys.readdir f
      |> Array.to_list
      |> List.map (Filename.concat f)
      |> List.append fs
      |> aux result
    | f :: fs -> aux (f :: result) fs
    | [] -> result
  in
  aux [] [ dir ]
;;

let files_in_dir dir =
  let rec aux result temp =
    match temp with
    | f :: fs when Sys.is_directory f ->
      Sys.readdir f
      |> Array.to_list
      |> List.map (Filename.concat f)
      |> List.append fs
      |> aux result
    | f :: fs -> aux (f :: result) fs
    | [] -> result
  in
  aux [] [ dir ]
;;

let files_in_dir dir =
  let rec aux result dir =
    match dir with
    | f :: fs when Sys.is_directory f ->
      let t =
        Sys.readdir f |> Array.to_list |> List.map (Filename.concat f) |> List.append fs
      in
      aux result t
    | f :: fs -> aux (f :: result) fs
    | [] -> result
  in
  aux [] [ dir ]
;;

let files_in_dir dir =
  let rec walk dir acc =
    match dir with
    | [] -> acc
    | dir :: tail ->
      let temp_entries =
        Sys.readdir dir |> Array.to_list |> List.map (Filename.concat dir)
      in
      let dirs, files =
        List.fold_left
          (fun (dirs, files) elem ->
            match (stat elem).st_kind with
            | S_REG -> dirs, elem :: files
            | S_DIR -> elem :: dirs, files
            | _ -> dirs, files)
          ([], [])
          temp_entries
      in
      walk (dirs @ tail) (files @ acc)
  in
  walk [ dir ] []
;;
